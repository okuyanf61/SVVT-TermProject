import random
import time

from playwright.sync_api import Playwright


def get_data(playwright: Playwright, email: str, password: str) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.sahibinden.com/
    page.goto("https://www.sahibinden.com/")

    # Click text=Kabul Et
    page.locator("text=Kabul Et").click()

    # Click a:has-text("Giriş Yap")
    page.locator("a:has-text(\"Giriş Yap\")").click()
    # expect(page).to_have_url("https://secure.sahibinden.com/giris")

    # Fill [placeholder="E-posta"]
    time.sleep(random.randint(1, 3))
    page.locator("[placeholder=\"E-posta\"]").type(email)

    # Click [placeholder="Şifre"]
    page.locator("[placeholder=\"Şifre\"]").click()

    # Fill [placeholder="Şifre"]
    page.locator("[placeholder=\"Şifre\"]").type(password)

    # Press Enter
    # with page.expect_navigation(url="https://secure.sahibinden.com/giris"):
    time.sleep(random.randint(1, 3))
    with page.expect_navigation():
        page.locator("[placeholder=\"Şifre\"]").press("Enter")

    # Click a:has-text("sahibinden.com") >> nth=1
    page.locator("a:has-text(\"sahibinden.com\")").nth(1).click()
    # expect(page).to_have_url("https://www.sahibinden.com/")

    # This waits for the "networkidle"
    page.wait_for_load_state("networkidle")

    # Click [placeholder="Kelime\, ilan no veya mağaza adı ile ara"]
    time.sleep(random.randint(3, 5))
    page.locator("[placeholder=\"Kelime\\, ilan no veya mağaza adı ile ara\"]").click()

    # Fill [placeholder="Kelime\, ilan no veya mağaza adı ile ara"]
    time.sleep(random.randint(1, 3))
    page.locator("[placeholder=\"Kelime\\, ilan no veya mağaza adı ile ara\"]").type("Raspberry Pi 4 4GB")

    # Click text=No search results. Detaylı Arama >> button
    # with page.expect_navigation(url="https://www.sahibinden.com/ikinci-el-ve-sifir-alisveris?query_text_mf=Raspberry+Pi+4+4GB&query_text=Raspberry+Pi+4+4GB"):
    time.sleep(random.randint(1, 3))
    with page.expect_navigation():
        page.locator("text=No search results. Detaylı Arama >> button").click()
    # expect(page).to_have_url("https://www.sahibinden.com/ikinci-el-ve-sifir-alisveris?query_textUnmodified=Raspberry+Pi+4+4GB&query_text=Raspberry+Pi+4+4GB&query_text_mf=Raspberry+Pi+4+4GB")

    # Click text=Aramayı Kaydet >> nth=2
    page.locator("text=Aramayı Kaydet").nth(2).click()

    # Click #saveSearchResultLink
    page.locator("#saveSearchResultLink").click()

    # Click input[name="favoriteSearchTitle"]
    page.locator("input[name=\"favoriteSearchTitle\"]").click()

    # Fill input[name="favoriteSearchTitle"]
    page.locator("input[name=\"favoriteSearchTitle\"]").type("svvt" + time.strftime("-%H:%M-%d-%m-%Y"))

    # Click div[role="dialog"] button:has-text("Kaydet")
    time.sleep(random.randint(3, 5))
    page.locator("div[role=\"dialog\"] button:has-text(\"Kaydet\")").click()

    # Click #advancedSorting
    page.locator("#advancedSorting").click()
    # expect(page).to_have_url("https://www.sahibinden.com/ikinci-el-ve-sifir-alisveris?query_text_mf=Raspberry+Pi+4+4GB&query_text=Raspberry+Pi+4+4GB#!")

    # Click text=Fiyata göre (Önce en düşük)
    # with page.expect_navigation(url="https://www.sahibinden.com/ikinci-el-ve-sifir-alisveris?query_text_mf=Raspberry+Pi+4+4GB&query_text=Raspberry+Pi+4+4GB&sorting=price_asc"):
    with page.expect_navigation():
        page.locator("text=Fiyata göre (Önce en düşük)").click()

    content = page.content()

    # ---------------------
    context.close()
    browser.close()
    return content