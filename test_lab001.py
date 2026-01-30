from playwright.sync_api import Page, expect, Playwright  # calling Page class

def test_lab001(playwright): #initiate browser method 2
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.udemy.com")

def test_lab002(page: Page): #initiate browser method 2
    page.goto("https://www.udemy.com")

def test_lab003(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    # page.get_by_role("checkbox").click()
    page.locator("#terms").check()
    page.get_by_role("button").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefox_browser(playwright: Playwright):
    browser_fire = playwright.firefox.launch(headless=False)
    context = browser_fire.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    # page.get_by_role("checkbox").click()
    page.locator("#terms").check()
    page.get_by_role("button").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


