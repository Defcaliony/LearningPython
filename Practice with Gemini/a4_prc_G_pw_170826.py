from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()

    print("Open website")
    page.goto("https://example.com")

    title = page.title()
    print(f"Title website: {title} ")

    page.screenshot(path="example.png")
    print("Screenshot 'Example.png' saved")

    browser.close()