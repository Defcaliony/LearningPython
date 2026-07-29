#assert for h1
from playwright.sync_api import sync_playwright

def run_wiki_prc():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://wikipedia.org")

        search_field = page.get_by_role("searchbox")
        search_field.fill("Python")
        search_field.press("Enter")

        heading = page.get_by_role("heading", level=1)
        assert "Python" in heading.text_content()

        print("\n The article title contains the word Python")
        page.screenshot(path="wiki_python.png")

        browser.close()

run_wiki_prc()