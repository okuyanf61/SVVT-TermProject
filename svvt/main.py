from playwright.sync_api import sync_playwright

from svvt.sahibinden import get_data
from svvt.parser import parse_html_into_prices
from svvt.utils import calculate_average, write_average_to_file


def run() -> None:
    # Get data from Sahibinden
    with sync_playwright() as playwright:
        data = get_data(playwright, "coday39633@doerma.com", "QUvdQ87XHk6UYqe")

    # Parse data into prices
    prices = parse_html_into_prices(data)

    # Calculate average
    avg = calculate_average(prices)

    # Write average to file
    write_average_to_file(avg)

    # Print average
    print(avg)


run()
