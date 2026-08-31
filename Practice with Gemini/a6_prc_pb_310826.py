from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()

    #print("Open Wiki...")
    page.goto("https://uk.wikipedia.org")

    #print("Click button 'Вікіпедія:Проєкти'...")
    #page.get_by_text("Проєкти").first.click()
    search_input = page.locator("#searchInput")
    search_input.fill("Python")
    search_input.press("Enter")

    current_title = page.title()
    print(f"This Title: {current_title}")

    assert "Python" in current_title, "Error: Title not found!"
    print("Test success: Title correct")

    browser.close()