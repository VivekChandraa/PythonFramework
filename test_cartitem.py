import time

from playwright.sync_api import Page, expect


def test_filterproduct(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    # page.get_by_role("checkbox").click()
    page.locator("#terms").check()
    page.get_by_role("button").click()
    iphoneprod = page.locator("app-card").filter(has_text="iphone X")
    iphoneprod.get_by_role("button").click()
    nokiaprod = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaprod.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
