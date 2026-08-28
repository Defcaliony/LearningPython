from playwright.sync_api import sync_playwright

def run_login_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login") #Go to website

        #1. filling in the lines
        page.locator("#username").fill("tomsmith") #Locate the field and enter the login
        page.locator("#password").fill("SuperSecretPassword!") #Locate the field and enter the pass

        #2. click to the button
        page.locator("button[type='submit']").click() #Locate the button and click

        #3. reading the text
        flash_massage = page.locator("#flash").text_content()

        #4. check
        assert "You logged into a secure area!" in flash_massage
        print("✅ Success!")

        browser.close()

run_login_test()