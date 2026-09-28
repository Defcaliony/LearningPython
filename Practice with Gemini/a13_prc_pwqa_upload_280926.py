import os
import time
from playwright.sync_api import sync_playwright

def run_upload_prc():
    # 1. Create a temporary txt for download
    file_name = "test_upload.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("This is testfile for checking Upload in Playwright.")

    # Getting the full path to the created file
    file_path = os.path.abspath(file_name)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://demoqa.com/upload-download")
        print("The title of page:", page.title())

        # 2. Locate the file upload element and pass the path
        upload_input = page.locator("#uploadFile")
        upload_input.set_input_files(file_path)

        # 3.Checking the text
        uploaded_path_text = page.locator("#uploadedFilePath").inner_text()
        print("Getting ok for website", uploaded_path_text)

        time.sleep(2)
        browser.close()

    if os.path.exists(file_name):
        os.remove(file_name)

if __name__ == "__main__":
    run_upload_prc()