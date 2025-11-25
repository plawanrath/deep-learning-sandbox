
def calculate_median(numbers):
    """Calculates the median of a list of numbers."""
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 1:
        return sorted_numbers[mid]

    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
