import time
#from playwright.sync_api import sync_playwright
from playwright.sync_api import Dialog, sync_playwright

def run_alerts_prc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://demoqa.com/alerts")
        print("Page title:", page.title())

        # 1. Simple alert (button OK)
        def handle_alert(dialog: Dialog):
            print(f"[Alert] The text: '{dialog.message}'")
            dialog.accept() #click OK

        page.on("dialog", handle_alert)
        page.locator("#alertButton").click()
        page.remove_listener("dialog",handle_alert) # leave from the event

        time.sleep(2)

        # 2. Confirm box (OK/Cancel)
        def handle_confirm(dialog: Dialog):
            print(f"[Confirm] The text: '{dialog.message}'")
            dialog.accept() # Click OK (or dialog.dismiss() for Cancel)

        page.on("dialog", handle_confirm)
        page.locator("#confirmButton").click()
        page.remove_listener("dialog", handle_confirm)

        # Check the selection result on the page
        confirm_result = page.locator("#confirmResult").inner_text()
        print("The result Confirm:", confirm_result)

        time.sleep(2)

        # 3. Prompt box (the text input)
        def handle_prompt(dialog: Dialog):
            print(f"[Prompt] The text: '{dialog.message}'")
            dialog.accept("Playwright student") # Input the text & click OK

        page.on("dialog", handle_prompt)
        page.locator("#promtButton").click() # error on the html #promPtButton
        page.remove_listener("dialog", handle_prompt)

        # Check the output text on the page
        prompt_result = page.locator("#promptResult").inner_text()
        print("Prompt result:", prompt_result)

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    run_alerts_prc()





