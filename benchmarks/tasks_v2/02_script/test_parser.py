
from log_parser import parse_log_line
def test_valid():
    r = parse_log_line("[2023-01-01 10:00] INFO: msg")
    assert r['level'] == 'INFO' and r['message'] == 'msg'
def test_error():
    r = parse_log_line("[2023-01-01 10:00] ERROR: fail")
    assert r['level'] == 'ERROR'
def test_invalid():
    assert parse_log_line("garbage") is None
