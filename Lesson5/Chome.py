from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# # ЗАДАЧА 1

# driver.maximize_window()
# driver.get("http://the-internet.herokuapp.com/add_remove_elements/.")

# add_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
# for _ in range(5):
#     add_button.click()

# delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')

# print(len(delete_buttons))

# sleep(10)


# # ЗАДАЧА 2

driver.maximize_window()
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")

    add_button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    add_button.send_keys(Keys.RETURN)
    sleep(3)

# sleep(3)



# # ЗАДАЧА 3

# driver.maximize_window()
# for i in range(3):
#     driver.get("http://uitestingplayground.com/classattr")

   
#     blue_button = driver.find_element(By.XPATH, '//button[contains(@class, "btn-primary")]')
#     blue_button.send_keys(Keys.RETURN)

#     alert = driver.switch_to.alert
#     alert.accept()
        
#     sleep(3)
    
# sleep(3)


# # ЗАДАЧА 4

# driver.maximize_window()
# driver.get("http://the-internet.herokuapp.com/entry_ad")
# sleep(3)

# close_button = driver.find_element(By.CSS_SELECTOR, '.modal-footer > p')
# close_button.click()
# sleep(3)


# # ЗАДАЧА 5

# driver.maximize_window()
# driver.get("http://the-internet.herokuapp.com/inputs")

# search_input = driver.find_element(By.CSS_SELECTOR,'input')
# search_input.send_keys("1000")

# sleep(3)

# search_input.clear()

# search_input.send_keys("999")

# sleep(3)

# # ЗАДАЧА 6

# driver.maximize_window()
# driver.get("http://the-internet.herokuapp.com/login")

# search_input_username = driver.find_element(By.ID,'username')
# search_input_username.send_keys("tomsmith")

# search_input_password = driver.find_element(By.ID,'password')
# search_input_password.send_keys("SuperSecretPassword!")

# sleep(2)

# login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
# login_button.click()

# sleep(5)