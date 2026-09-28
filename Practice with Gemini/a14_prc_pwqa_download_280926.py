import os
import time
from playwright.sync_api import sync_playwright

def run_download_prc():
    download_filename = "download_sample.jpeg"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page=browser.new_page()

        page.goto("https://demoqa.com/upload-download")
        print("The title page of page:", page.title())

        # 1. Prison download action & click button
        with page.expect_download() as download_info:
            page.locator("#downloadButton").click()

        # 2. Getting an object of download file
        download = download_info.value
        print("The original filename from the website:", download.suggested_filename)

        # 3.Download this file in our directory
        download.save_as(download_filename)

        if os.path.exists(download_filename):
            print(f"Congratulate! The File '{download_filename}' successfully saved to disk")

        time.sleep(2)
        browser.close()

    # clear: delete download file after test
    if os.path.exists(download_filename):
        os.remove(download_filename)
        print("makeshift file deleted.")

if __name__=="__main__":
    run_download_prc()