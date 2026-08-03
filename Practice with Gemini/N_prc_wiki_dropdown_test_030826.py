import os
from playwright.sync_api import sync_playwright

def run_wiki_dropdown():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://wikipedia.org")

        search_field = page.get_by_role("searchbox")
        search_field.press_sequentially("Pyth", delay=200) #search_field.fill("Playwright")

        #search_field.press("ArrowDown") #don't work because click first link witch don't needed
        #search_field.press("Enter")

        #suggestion = page.locator(".cdx-menu-item, .suggestion-link").first
        #suggestion.click()

        dropdown_item = page.locator("a.suggestion-link, cdx-menu-item").filter(has_text="Python").first  #find helpful this word
        dropdown_item.wait_for(state="visible")
        dropdown_item.click()

        #suggestion = page.locator(".suggestion-link, .cdx-menu-item").all_text_contents()

        heading = page.get_by_role("heading", level=1)   #remind
        print(f"\n Title open page: '{heading.text_content()}' ")

        assert "Python" in heading.text_content()
        print("Successful take Python with Title open page")

        #print("\n What is really appeared in the dropdown list ")
        #for index, item in enumerate(suggestion, 1):
        #    print(f"{index}. {item.strip()}")
        #page.screenshot(path="wiki_python.png")

        browser.close()

run_wiki_dropdown()