import time


def calculate_average(prices: list) -> str:
    return f"{time.strftime('%d-%m-%Y')} - Average price: {int(sum(prices) / len(prices))} TL"


def write_average_to_file(avg: str) -> None:
    with open("averages.txt", "a+") as f:
        f.write(avg + "\n")
