from .validate import integer, assertions

def validate(spec):
    if not isinstance(spec, dict) or not isinstance(spec.get('url'), str):
        raise ValueError('A scenario URL is required')
    if not isinstance(spec.get('trigger'), str) or not 1 <= len(spec['trigger']) <= 500:
        raise ValueError('A trigger selector is required')
    delays = spec.get('delays_ms')
    if not isinstance(delays, list) or not 1 <= len(delays) <= 12:
        raise ValueError('Specify 1 to 12 interruption times')
    for delay in delays: integer(delay, 0, 5000)
    integer(spec.get('settle_ms', 250), 0, 5000)
    events = spec.get('interruptions')
    if not isinstance(events, list) or len(events) > 8:
        raise ValueError('Specify at most 8 interruptions; an empty list checks the baseline')
    for event in events:
        if event.get('kind') not in ('escape', 'retrigger', 'resize'):
            raise ValueError('Unknown interruption')
        if event['kind'] == 'resize':
            integer(event.get('width'), 200, 3000); integer(event.get('height'), 200, 3000)
    assertions(spec.get('assertions'))
    return spec
