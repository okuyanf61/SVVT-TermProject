from playwright.sync_api import sync_playwright

from svvt.avg_utils import calculate_average, write_average_to_file
from svvt.parser import parse_html_into_prices
from svvt.sahibinden import get_data


def run() -> None:
    """Run the main script."""
    # Get data from Sahibinden
    with sync_playwright() as playwright:
        html_data = get_data(playwright, "coday39633@doerma.com", "QUvdQ87XHk6UYqe")

    # Parse data into prices
    prices = parse_html_into_prices(html_data)

    # Calculate average
    avg = calculate_average(prices)

    # Write average to file
    write_average_to_file(avg)

    # Print average
    print(avg)  # noqa: WPS421


run()
