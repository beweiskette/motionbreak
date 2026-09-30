import os
from pathlib import Path
from functools import partial
import http.server
import threading
import pytest
from motionbreak.scenario import validate
from motionbreak.runner import run
from motionbreak.minimize import minimize

def test_reducer_preserves_same_failure():
    assert minimize(['a', 'b', 'c'], lambda seq: 'b' in seq) == ['b']

def test_contract_required():
    with pytest.raises(ValueError): validate({'url': 'http://localhost', 'trigger': '#open'})

@pytest.mark.integration
def test_real_browser_fixed_and_broken():
    executable = os.environ.get('TEST_BROWSER')
    if not executable and not os.environ.get('BROWSER_TEST'):
        pytest.skip('Set TEST_BROWSER or BROWSER_TEST=1')
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args): pass
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(Path(__file__).parents[1] / 'examples')))
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    try:
        spec = {'url': f'http://127.0.0.1:{server.server_port}/fixed.html', 'trigger': '#open',
                'delays_ms': [10], 'settle_ms': 250, 'interruptions': [{'kind': 'escape'}],
                'assertions': [{'kind': 'hidden', 'selector': '#overlay'}, {'kind': 'hidden', 'selector': '#menu'}, {'kind': 'focused', 'selector': '#open'}]}
        assert run(spec, executable)['status'] == 'pass'
        spec['url'] = spec['url'].replace('fixed.html', 'broken.html')
        result = run(spec, executable)
        assert result['status'] == 'fail'
        assert result['cases'][0]['repeatable'] is True
        assert result['cases'][0]['minimal_interruptions'] == [{'kind': 'escape'}]
    finally:
        server.shutdown(); server.server_close(); thread.join()
