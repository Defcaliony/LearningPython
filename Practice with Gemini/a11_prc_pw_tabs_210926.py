import time
from playwright.sync_api import sync_playwright

def run_tab_pract():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo = 2000)
        context = browser.new_context()

        #Our the first (main) page
        page = context.new_page()
        page.goto("https://demoqa.com/browser-windows")

        print("Title first page", page.title())

        #Waiting to open new tab for click on button "#tabButton"
        with context.expect_page() as new_tab_info:
            #page.locator("#tabButton").click()
            page.locator("#windowButton").click()

        #Take new tab
        #new_page = new_tab_info.value
        window_page = new_tab_info.value
        #new_page.wait_for_load_state()
        window_page.wait_for_load_state()

        #Chek text on the new tab
        #heading_text = new_page.locator("#sampleHeading").inner_text()
        heading_text = window_page.locator("#sampleHeading").inner_text()
        print("The text on main tab:", heading_text)

        time.sleep(2)

        #To close new tab, back to first one
        #new_page.close()
        window_page.close()

        time.sleep(1)
        browser.close()

if __name__ == "__main__":
    run_tab_pract()



