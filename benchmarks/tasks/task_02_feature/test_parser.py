
from log_parser import parse_log_line

def test_valid_info():
    line = "[2023-10-27 10:00:00] INFO: System started"
    result = parse_log_line(line)
    assert result['timestamp'] == '2023-10-27 10:00:00'
    assert result['level'] == 'INFO'
    assert result['message'] == 'System started'

def test_valid_error():
    line = "[2023-11-01 09:15:22] ERROR: Connection failed"
    result = parse_log_line(line)
    assert result['level'] == 'ERROR'

def test_invalid_format():
    assert parse_log_line("Invalid log line") is None
