from selenium.webdriver.common.by import By
from constants import Test_form_URL

class MainPage:
   def __init__(self, browser, url=Test_form_URL):
       self.browser = browser
       self.url = url
    
   def open(self):
       self.browser.get(self.url)

   def fill_fields(self, v_dict: dict):
       for key, value in v_dict.items():
           selector = f'[name={key}]'
           self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(value)

   def click_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    
   def find_element_property(self, locator):
        background_color = self.browser.find_element(By.ID, locator).value_of_css_property("background-color")
        return background_color     
    


        
