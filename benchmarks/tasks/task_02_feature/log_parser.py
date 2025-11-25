
import re

def parse_log_line(line):
    """
    Parses a log line in the format: '[TIMESTAMP] LEVEL: Message'
    Example: '[2023-10-27 10:00:00] INFO: System started'

    Returns:
        dict: {'timestamp': str, 'level': str, 'message': str} or None if invalid
    """
    pattern = r"^\[(?P<timestamp>[^\]]+)\]\s+(?P<level>INFO|ERROR):\s+(?P<message>.+)$"
    match = re.match(pattern, line)
    if not match:
        return None

    return {
        "timestamp": match.group("timestamp"),
        "level": match.group("level"),
        "message": match.group("message"),
    }
