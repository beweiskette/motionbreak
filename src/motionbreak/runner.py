from .browser import session, assertions
from .scenario import validate
from .minimize import minimize

def attempt(spec, delay, events, executable, allow_remote):
    with session(spec['url'], executable, allow_remote) as (page, context, proxy):
        try:
            page.goto(spec['url'], wait_until='domcontentloaded')
            page.locator(spec['trigger']).click()
            page.wait_for_timeout(delay)
            for event in events:
                if event['kind'] == 'escape': page.keyboard.press('Escape')
                elif event['kind'] == 'retrigger': page.locator(spec['trigger']).click()
                else: page.set_viewport_size({'width': event['width'], 'height': event['height']})
            page.wait_for_timeout(spec.get('settle_ms', 250))
            failures = assertions(page, spec['assertions'])
            return {'failures': failures, 'error': None}
        except Exception:
            return {'failures': [], 'error': 'navigation-or-action-failed'}

def run(spec, executable=None, allow_remote=False):
    validate(spec)
    cases = []
    for delay in spec['delays_ms']:
        original = attempt(spec, delay, spec['interruptions'], executable, allow_remote)
        case = {'delay_ms': delay, **original, 'repeatable': None}
        if original['error'] is None and original['failures']:
            def reproduces(events):
                return all(attempt(spec, delay, events, executable, allow_remote) == original for _ in range(2))
            case['repeatable'] = reproduces(spec['interruptions'])
            if case['repeatable']:
                case['minimal_interruptions'] = minimize(spec['interruptions'], reproduces)
                case['repro'] = {**spec, 'delays_ms': [delay], 'interruptions': case['minimal_interruptions']}
        cases.append(case)
    status = 'error' if any(c['error'] for c in cases) else 'fail' if any(c['failures'] for c in cases) else 'pass'
    return {'schema': 1, 'status': status, 'cases': cases, 'scope': 'Only the declared end-state assertions are checked. Fresh browser storage for every attempt.'}
