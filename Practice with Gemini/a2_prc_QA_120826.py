import os #So why I'm importing this thing when this one not work?

from playwright.sync_api import sync_playwright

def run_dropdown_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/dropdown")

        #search_field = search_field.select_option("dropdown")
        #search_field.press_sequentially("Pyth", delay=200)

        dropdown = page.locator("#dropdown") # find drop title for his ID (#dropdown)
        dropdown.select_option("2") # chose "Option 2"

        selected_value = dropdown.input_value() # reading the selected value
        print(f"\n Selected dropdown: {selected_value}")

        assert selected_value == "2"
        print("Successful")

        browser.close()


run_dropdown_test()