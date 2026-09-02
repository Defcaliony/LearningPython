from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()

    print("Open Wiki")
    page.goto("https://uk.wikipedia.org/")

    #menu_items = page.locator(".mw-sidebar-action a").all() 1v
    #links_locator = page.locator("nav a") 2v
    #links_locator = page.locator("#mp-upper a") v3
    links_locator = page.locator("main a")
    #links_locator.first.wait_for(state="attached") v3
    links_locator.first.wait_for()

    menu_items = links_locator.all()
    #menu_items = page.locator("#main-itn a").all()

    print(f"{len(menu_items)} items found in <main>")

    count = 0
    for item in menu_items:
        text = item.text_content().strip()
        if text:
            print(f"Text of element: {text.strip()}")
            count += 1
            if count == 10:
                break

    browser.close()
