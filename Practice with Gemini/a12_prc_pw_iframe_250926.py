import time
from playwright.sync_api import sync_playwright

def run_iframe_prc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://demoqa.com/frames")

        print("The Title of main page:", page.title())

        first_frame = page.frame_locator("#frame1")

        text_in_frame1 = first_frame.locator("#sampleHeading").inner_text()
        print("The Text of within frame1:", text_in_frame1)

        second_frame = page.frame_locator("#frame2")
        text_in_frame2 = second_frame.locator("#sampleHeading").inner_text()
        print("The Text of within frame2:", text_in_frame2)

        time.sleep(3)
        browser.close()

if __name__ == "__main__":
    run_iframe_prc()
