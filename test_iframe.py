from playwright.sync_api import Page, expect

from playwright.sync_api import Page, expect


def test_iframe(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    iframepage = page.frame_locator("#courses-iframe")

    iframepage.get_by_role("link", name="All Access").click()

    expect(iframepage.locator("body")).to_contain_text("All Access Subscription")
