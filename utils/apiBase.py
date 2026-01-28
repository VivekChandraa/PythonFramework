from playwright.sync_api import Playwright
api_payload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright: Playwright,user_credentials):
        userEmail = user_credentials['userEmail']
        userPass = user_credentials['userPassword']
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response =api_request_context.post("/api/ecom/auth/login",
                                           data={"userEmail": userEmail, "userPassword": userPass})
        assert response.ok
        print(response.json())
        responseBody= response.json()
        return responseBody["token"]

    def createOrder(self,playwright: Playwright,user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                             data=api_payload,
                                              headers={"Authorization": token,
                                                         "Content-Type": "application/json"
                                                          })
        print(response.json())
        response_body = response.json()
        OrderID = response_body["orders"][0]
        return OrderID