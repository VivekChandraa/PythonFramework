from playwright.sync_api import Page

fakePayloadOrderResponse= {"data": [], "message": "No Order"}

def intercept_response(route):
    route.fulfill(
        json= fakePayloadOrderResponse
    )

def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)   # * I'll put star here because for every ID it changes.So you cannot hardcode this like using this ID because tomorrow if another one testing this with their own data then they will have their own ID here.So instead what I am doing is I know until this piece it's a constant. So I put slash star so that it considers it as a regular expression and it accepts any alphanumeric
    page.get_by_placeholder("email@example.com").fill("vivekchandra@yopmail.com")
    page.get_by_placeholder("enter your passsword").fill("Vivek@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)