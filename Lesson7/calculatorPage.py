
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    
    def driver(self):
       yield self.driver
       self.driver.quit()
    
    

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def set_delay(self, delay_time):
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()  
        delay_input.send_keys('45')

    def click_button(self, value):

        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()


    def get_result(self,):
        return WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
        )

    