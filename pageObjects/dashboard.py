from pageObjects.orderHistory import OrderHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        OrderHistory = OrderHistoryPage(self.page)
        return OrderHistory

