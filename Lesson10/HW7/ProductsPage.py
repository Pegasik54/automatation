import allure
from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, browser):
        self.browser = browser
    
    @allure.step("Добавление товара в корзину")
    def add_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    @allure.step("Нажимаем кнопку оформления заказа")
    def checkout_click(self):
        self.browser.find_element(By.CSS_SELECTOR, '#checkout').click()