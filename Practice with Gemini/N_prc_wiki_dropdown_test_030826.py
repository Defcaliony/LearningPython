import os
from playwright.sync_api import sync_playwright

def run_wiki_dropdown():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://wikipedia.org")

        search_field = page.get_by_role("searchbox")
        search_field.press_sequentially("Playwrig", delay=200) #search_field.fill("Playwright")

        #search_field.press("ArrowDown") #don't work because click first link witch don't needed
        #search_field.press("Enter")

        #suggestion = page.locator(".cdx-menu-item, .suggestion-link").first
        #suggestion.click()

        #last test - dropdown_item = page.locator("a.suggestion-link").filter(has_text="Playwright")  #find helpful this word
        #last test - dropdown_item.click()

        suggestion = page.locator(".suggestion-link, .cdx-menu-item").all_text_contents()

        #last test -heading = page.get_by_role("heading", level=1)   #remind
        #last test - assert "Playwright" in heading.text_content()

        print("\n What is really appeared in the dropdown list ")
        for index, item in enumerate(suggestion, 1):
            print(f"{index}. {item.strip()}")
        #page.screenshot(path="wiki_python.png")

        browser.close()

run_wiki_dropdown()