import os
from playwright.sync_api import sync_playwright

def run_duckduckgo_prc(): #create the function
    #1. Open browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://duckduckgo.com")

        search_field = page.get_by_role("combobox")

        search_field.fill("Playwright")

        #search_button = page.get_by_role("button", name= "Пошук") # WHY DONT WORK??????
        #button = span (don't work, because span it is HTML teg)
        #search_button.click()
        search_field.press("Enter")

        #page.get_by_text("Пошук").first.click() # TEST after enter, it is working



        assert "Playwright" in page.title() # new function chek test!
        print("\n Test passed successfully! The word Playwright was found in the page title")


        full_path = os.path.abspath("duckduckgo_prc_result.png")
        page.screenshot(path=full_path)

        browser.close()

run_duckduckgo_prc()