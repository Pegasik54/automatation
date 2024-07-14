import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form_submission(driver):
   
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   driver.maximize_window()
   
   driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
   
   driver.find_element(By.NAME, "first-name").send_keys("Иван")
   driver.find_element(By.NAME, "last-name").send_keys("Петров")
   driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
   driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
   driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
   driver.find_element(By.NAME, "city").send_keys("Москва")
   driver.find_element(By.NAME, "country").send_keys("Россия")
   driver.find_element(By.NAME, "job-position").send_keys("QA")
   driver.find_element(By.NAME, "company").send_keys("SkyPro")

   driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
   
   driver.implicitly_wait(5)

   zip_code_field = driver.find_element(By.ID, "zip-code")
   assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code field is not highlighted in red"
    
  
   fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
   for field in fields:
        input_field = driver.find_element(By.ID, field)
        assert "is-valid" in input_field.get_attribute("class"), f"Field {field} is not highlighted in green"

