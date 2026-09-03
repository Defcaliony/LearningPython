from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)

    context = browser.new_context()
    page = context.new_page()

    print("Open wiki..")
    page.goto("https://uk.wikipedia.org/")

    #wikimedia_link = page.get_by_text("Фонд Вікімедіа").first v2
    wikimedia_link = page.get_by_role("link", name="Вікіцитати").first

    wikimedia_link.scroll_into_view_if_needed()

    with context.expect_page() as new_page_info:
        #page.get_by_text("Фонд Вікімедіа").first.click() v1
        wikimedia_link.click(button="middle")

    new_page = new_page_info.value

    new_page.wait_for_load_state()

    print(f"Title old page: {page.title()}")
    print(f"Title new tab: {new_page.title()}")

    browser.close()