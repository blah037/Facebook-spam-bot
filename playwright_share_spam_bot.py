from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright, usernames, passwords, messages, proxy) -> None:
    for username, password, message in zip(usernames, passwords, messages):
        browser = playwright.chromium.launch(headless=False, proxy=proxy)  # Specify proxy here
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://mbasic.facebook.com")
        page.get_by_label("Phone number or email").click()
        page.get_by_label("Phone number or email").fill(username)
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill(password)
        page.get_by_role("button", name="Log in").click()

        # Handle "Login with one tap" if it appears
        try:
            page.get_by_role("button", name="OK").click()
        except:
            pass
        try:
            page.locator("a.bg:nth-child(8) > strong:nth-child(1)").click()
        except:
            page.locator("a.bf:nth-child(8) > strong:nth-child(1)").click()

        page.get_by_role("link", name="See all").click()

        try:
            page.get_by_role("link", name="СҮХБААТАР АЙМАГ НЭГДСЭН ЗАРЫН ГРУПП").click()
        except:
            page.locator("li.bm:nth-child(11) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()
        # Write and post a message
        page.get_by_placeholder("What's on your mind?").click()
        page.get_by_placeholder("What's on your mind?").fill(message)
        page.get_by_role("button", name="Post").click()

        # ---------------------
        context.close()
        browser.close()

usernames = ['61559686854533', '61559686854533']  # Add your usernames here61559732393722
passwords = ['Bilguun1213', 'Bilguun1213']  # Add your passwords hereBuyka89024
messages = ['https://fb.watch/s0fDUP5mjb/', 'https://fb.watch/s0fHm6VCqO/']

# Specify proxy as a dictionary
proxy = {"server": "104.207.33.94:3128"}

with sync_playwright() as playwright:
    run(playwright, usernames, passwords, messages, proxy)
