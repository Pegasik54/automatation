import allure
from LoginPage import LoginPage
from ProductsPage import ProductsPage
from CheckoutPage import CheckoutPage

user_name = "standard_user"
password = "secret_sauce"

first_name = "Alex"
last_name = "Strend"
postal_code = "11222314"

sum = "$58.29"


@allure.epic("Saucedemo")
@allure.severity(severity_level='normal')
@allure.title("Оформление заказа в магазине")
@allure.description("Оформление заказа с необходимыми товарами с последующеим сравнением стоимости")
@allure.feature("Тест №3")
def test_purchase(chrome_browser):
    with allure.step("Авторизация на странице сервиса"):
        login_Page = LoginPage(chrome_browser)
        login_Page.open()
        login_Page.sign_in(user_name, password)

    with allure.step("Добавляем товары в корзину"):
        products_page = ProductsPage(chrome_browser)
        products_page.add_to_cart()
        products_page.go_to_cart()
        products_page.checkout_click()

    with allure.step("Оформляем заказ"):
        checkout_page = CheckoutPage(chrome_browser)
        checkout_page.make_checkout(first_name, last_name, postal_code)

    with allure.step("Сравниваем итоговую сумму с ожидаемой"):
        txt = checkout_page.check_total()
    assert sum in txt