import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from calculatorPage import Calculator

@allure.epic("Calculator")
@allure.severity(severity_level='normal')
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных и вывод результата")
@allure.feature("Тест №1")
def test_calculator():
    with allure.step("Открываем калькулятор, вводим значения и ожидаем результат"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    calculator = Calculator(browser)
    calculator.set_delay('1')
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')
    with allure.step("Сравниваем получившийся результат с ожидаемым"):
        result = calculator.get_result()
    assert result, "Expected result to be '15', but got different result"