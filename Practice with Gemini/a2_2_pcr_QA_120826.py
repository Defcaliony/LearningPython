
from playwright.sync_api import sync_playwright

def run_checkbox_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/checkboxes")

        checkboxes = page.locator("input[type='checkbox']") # find all checkboxes in the page

        checkboxes.nth(0).check() #work with first ch-box
#find all checkbox↑.↑selected first.↑make action
        checkboxes.nth(1).uncheck() #work with first ch-box, drop bird

        assert checkboxes.nth(0).is_checked() == True #checked this bird stay?
        assert checkboxes.nth(1).is_checked() == False #
        print("Successful, checkboxes are checked")

        browser.close()


run_checkbox_test()