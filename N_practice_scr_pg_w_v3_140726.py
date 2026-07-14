import os
from playwright.sync_api import sync_playwright

def run_wikipedia_prc(): #create the function
    #1. Open browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        # 2. Go to the website
        page.goto("https://uk.wikipedia.org")

        # 3. Find the search field by its name (the aria-label attribute)
        # end enter the text. Google calls this field "Search"
        # Let's find it by type "searchbox" (this is an input field with prompts)

        search_field = page.get_by_role("searchbox")

        # Enter this word "Python"
        search_field.fill("Python")

        # 4.Press the Enter on the keyboard
        #search_field.press("Enter")
        search_button = page.get_by_role("button", name= "Знайти")
        search_button.click()

        # New lvl: automatic chek
        # We take the tab title(when is written on the tab at the top)
        # and check if the word "Python"
        assert "Python" in page.title() # new function chek test!
        print("\n Test passed successfully! The word Python was found in the page title")

        # 5. Taking a screenshot for verification
        full_path = os.path.abspath("wikipedia_prc_result.png")
        page.screenshot(path=full_path)

        #print("\n" + "="*50)
        #print(f"File saved this: {full_path}")
        #print("="*50 + "\n")

        # 4. Closed the browser
        browser.close()

run_wikipedia_prc()