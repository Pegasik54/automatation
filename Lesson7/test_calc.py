
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from calculatorPage import Calculator


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    calculator = Calculator(browser)
    calculator.set_delay('1')
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')
    result = calculator.get_result()
    assert result, "Expected result to be '15', but got different result"
    