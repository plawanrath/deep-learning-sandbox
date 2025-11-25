
def calculate_median(numbers):
    """Return the median of a numeric iterable or None for empty input."""
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 1:
        return sorted_numbers[mid]

    # Even-sized list: average the two middle elements
    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
