from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()

    print("Go to website after alerts")
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # 1.Create function for dialog
    def handle_dialog(dialog):
        print(f"Take dialog type: {dialog.type}")
        print(f"Text in dialog:{dialog.message}")
        #click ok
        #dialog.click() 1v
        #dialog.accept() 2v
        dialog.accept("Playwright Maaaaastaaar")

    # 2. Active event dialog
    page.on("dialog", handle_dialog)

    #3. Click for button, which coll Confirm
    #page.get_by_role("button", name="Click for JS Confirm").click()
    # name="Click for LS Confirm" The name must be looks like button on website
    page.get_by_role("button", name="Click for JS Prompt").click()

    # 4. look for text result
    result_text = page.locator("#result").inner_text()
    print(f"Result on the page: {result_text}")

    browser.close()
