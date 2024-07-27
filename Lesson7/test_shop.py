from LoginPage import LoginPage
from ProductsPage import ProductsPage
from CheckoutPage import CheckoutPage

user_name = "standard_user"
password = "secret_sauce"

first_name = "Alex"
last_name = "Strend"
postal_code = "11222314"

sum = "$58.29"

def test_purchase(chrome_browser):
    login_Page = LoginPage(chrome_browser)
    login_Page.open()
    login_Page.sign_in(user_name, password)

    products_page = ProductsPage(chrome_browser)
    products_page.add_to_cart()
    products_page.go_to_cart()
    products_page.checkout_click()

    checkout_page = CheckoutPage(chrome_browser)
    checkout_page.make_checkout(first_name, last_name, postal_code)

    txt = checkout_page.check_total()
    assert sum in txt