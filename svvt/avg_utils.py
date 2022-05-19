import time
from typing import List


def calculate_average(prices: List[int]) -> str:
    """
    Calculate average price.

    Args:
        prices: List of prices.

    Returns:
        Average price.
    """
    avg_price = int(sum(prices) / len(prices))
    current_time = time.strftime("%d-%m-%Y")
    return f"{current_time} - Average price: {avg_price} TL"


def write_average_to_file(avg: str) -> None:
    """
    Write average price to file.

    Args:
        avg: Average price.
    """
    with open("averages.txt", "a+") as avg_file:
        avg_file.write(avg + "\n")  # noqa: WPS336
