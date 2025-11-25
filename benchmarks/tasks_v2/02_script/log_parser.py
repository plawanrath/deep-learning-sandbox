
def parse_log_line(line):
    """Parse a log line like `[2023-01-01 10:00] INFO: message`.

    Returns a dict with keys `timestamp`, `level`, and `message` when the line
    matches the expected format; otherwise returns None.
    """
    import re

    # Accept timestamps inside brackets, uppercase level, and any message text.
    pattern = r"^\[(?P<timestamp>[^\]]+)\]\s+(?P<level>[A-Z]+):\s*(?P<message>.*)$"
    match = re.match(pattern, line.strip())
    if not match:
        return None

    return {
        "timestamp": match.group("timestamp"),
        "level": match.group("level"),
        "message": match.group("message"),
    }
