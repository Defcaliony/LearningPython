import os
from playwright.sync_api import sync_playwright

def run_browser(): #create the function
    #1. Open browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5000)
        page = browser.new_page()

        # 2. Go to the website
        page.goto("https://time.is/uk/Kyiv")

        # 3. Taking a screenshot for verification
        full_path = os.path.abspath("time_is_kyiv_page.png")
        page.screenshot(path=full_path)

        print("\n" + "="*50)
        print(f"File saved this: {full_path}")
        print("="*50 + "\n")

        # 4. Closed the browser
        browser.close()

run_browser()