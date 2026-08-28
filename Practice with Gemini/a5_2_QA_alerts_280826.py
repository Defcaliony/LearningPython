from playwright.sync_api import sync_playwright

def run_alert_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/javascript_alerts") #Go to website


        page.on("dialog", lambda dialog: dialog.accept())
               #L write ,under, after page = browser.new_page()
                   # def handle_dialog(dialog):
                        #print(f"Повідомлення в alert: {dialog.text()}")
                        #dialog.accept()
                    # page.on("dialog", handle_dialog)

        page.locator("button").nth(0).click() #Locate the button and click

        result_text = page.locator("#result").text_content()
        #flash_massage = page.locator("#flash").text_content()
        print(f"result_text: '{result_text}'")
        #4. check
        assert "You successfully clicked an alert" in result_text
        print("✅ Success!")

        browser.close()

run_alert_test()