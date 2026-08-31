from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()

    print("Open Wiki...")
    page.goto("https://uk.wikipedia.org")

    print("Click button 'Вікіпедія:Проєкти'...")
    page.get_by_text("Проєкти").first.click()

    print(f"New Title: {page.title()}")

    browser.close()