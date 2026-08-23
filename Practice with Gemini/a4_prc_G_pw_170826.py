from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()

    #print("Open website")
    page.goto("https://uk.wikipedia.org")

    #title = page.title()
    #print(f"Title website: {title} ")
    #search_input = page.locator("input[type='search']")
    search_input = page.get_by_placeholder("Пошук у Вікіпедії").first  #search

    search_input.fill("Python")
    search_input.press("Enter")

    page.screenshot(path="Python test.png")
    print(f"New title: {page.title()}")

    browser.close()