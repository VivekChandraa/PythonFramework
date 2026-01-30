
from playwright.sync_api import Page


def test_newtabtest(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator(".blinkingText").click()
    with page.expect_popup() as new_tabopen:
        secondtab = new_tabopen.value
        linktext1 = secondtab.locator(".red").text_content()
        print(linktext1)
        assert "mentor@rahulshettyacademy.com" in linktext1