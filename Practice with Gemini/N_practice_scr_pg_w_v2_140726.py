import os
from playwright.sync_api import sync_playwright

def run_browser(): #create the function
    #1. Open browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        # 2. Go to the website
        page.goto("https://google.com")

        # 3. Find the search field by its name (the aria-label attribute)
        # end enter the text. Google calls this field "Search"
        # Let's find it by type "combobox" (this is an input field with prompts)

        search_field = page.get_by_role("combobox")

        # Enter this word "Python"
        search_field.fill("Python")

        # 4.Press the Enter on the keyboard
        search_field.press("Enter")

        # 5. Taking a screenshot for verification
        full_path = os.path.abspath("search_result_140726.png")
        page.screenshot(path=full_path)

        #print("\n" + "="*50)
        #print(f"File saved this: {full_path}")
        #print("="*50 + "\n")

        # 4. Closed the browser
        browser.close()

run_browser()