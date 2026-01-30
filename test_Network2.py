from playwright.sync_api import Playwright, Page, expect

from utils.apiBase import APIUtils

#-> api call from the browser-> api call contact server return back response to browser-> browser use response to generate html

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


def test_network2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)    # * I'll put star here because for every ID it changes.So you cannot hardcode this like using this ID because tomorrow if another one testing this with their own data then they will have their own ID here.So instead what I am doing is I know until this piece it's a constant. So I put slash star so that it considers it as a regular expression and it accepts any alphanumeric
    page.get_by_placeholder("email@example.com").fill("vivekchandra@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Vivek@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)



#session set in browser
def test_session_store(playwright:Playwright):
    api_util = APIUtils()
    get_token = api_util.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

