from typing import List

from bs4 import BeautifulSoup


def parse_html_into_prices(html: str) -> List[int]:
    """
    Parses the HTML string into a list of prices.

    Args:
        html: The HTML string to parse.

    Returns:
        A list of prices.
    """
    # Get table contents from html variable with BeautifulSoup
    table = BeautifulSoup(html, "html.parser").find(
        "table", {"id": "searchResultsTable"}
    )
    table_data = table.contents[3]

    # Get prices into a list and calculate average
    return [
        int(td.text.strip().replace(".", "").split(" ")[0])
        for td in table_data.find_all("td", {"class": "searchResultsPriceValue"})
    ]
