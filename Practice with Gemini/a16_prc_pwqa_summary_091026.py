import os
import time
from playwright.sync_api import Dialog, sync_playwright

def run_e2e_sum_prc():
    upload_filename = "e2e_test_upload.txt"
    download_filename = "e2e_test_download.jpeg"

    # Ready: Created file for download on website
    with open(upload_filename, "w", encoding="utf-8") as f:
        f.write("The file for finishing e2e test playwright.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        # __ Stage 1: Navigation and work with files (Upload/Download)__
        print("\n--- Stage 1: Upload/Download --- ")
        page.goto("https://demoqa.com/upload-download")
        print("Page title:", page.title())

        # Upload file
        page.locator("#uploadFile").set_input_files(upload_filename)
        uploaded_path_text = page.locator("#uploadedFilePath").inner_text()
        print("The result Upload:", uploaded_path_text)

        # Download file
        with page.expect_download() as download_info:
            page.locator("#downloadButton").click()

        download = download_info.value
        download.save_as(download_filename)
        print(f"The file '{download_filename}' has been downloaded successfully")

        # __ Stage 2: Interception(перехоплення) JS Dialogs __
        print("\n--- Stage 2:  JS Dialog processing --- ")
        page.goto("https://demoqa.com/alerts")

        def handle_prompt(dialog: Dialog):
            print(f"[Prompt] Take text: '{dialog.message}' ")
            dialog.accept("2E2 Master Student 50|50 or soso")

            page.on("dialog", handle_prompt)
            page.locator("#promptButton").click()
            page.remove_listener("dialog", handle_prompt)

            prompt_result = page.locator("#promptResult").inner_text()
            print("Prompt result:", prompt_result)

            # __ Stage 3: Work with frame (Iframes) __
            print("\n ---Stage 3: Work with Iframe --- ")
            page.goto("https://demoqa.com/frames")

            frame1 = page.frame_locator("#frame1")
            frame_text = frame1.locator("#sampleHeading").inner_text()
            print("Text inside first frame:", frame_text)

            time.sleep(2)
            browser.close()

    # __ Stage 4: Cleaning the text spaces __
    print("\n--- Stage 4: Cleanup --- ")
    for file_path in [upload_filename, download_filename]:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully")

    print("\nE2E test completed successfully!!!")

if __name__ == "__main__":
    run_e2e_sum_prc()








