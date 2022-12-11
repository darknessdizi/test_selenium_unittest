import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class YandexAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_input_email(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")
        self.assertIn("Авторизация", driver.title)
        btn_login = driver.find_element(By.XPATH, 
            '//div[@class="AuthLoginInputToggle-input"]//input[@class="Textinput-Control"]'
            )
        btn_login.send_keys('rash-jane@mail.ru')
        btn_enter = driver.find_element(By.XPATH, 
            '//button[@class="Button2 Button2_size_l Button2_view_action Button2_width_max Button2_type_submit"]'
            )
        btn_enter.click()
        btn_next = driver.find_element(By.XPATH, 
            '//button[@class="Button2 Button2_size_l Button2_view_action Button2_width_max"]'
            )
        self.assertIn("Далее", btn_next.text)
        # time.sleep(5)

    def test_input_phone(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")
        self.assertIn("Авторизация", driver.title)
        btn_phone = driver.find_element(By.XPATH, '//button[@class="Button2 Button2_size_l Button2_view_clear"]')
        btn_phone.click()
        btn_enter_phone = driver.find_element(By.XPATH, 
            '//input[@class="Textinput-Control Textinput-Control_phone"]'
            )
        btn_enter_phone.send_keys('9062360823')
        btn_enter_phone.send_keys(Keys.RETURN)
        btn_next = driver.find_element(By.XPATH, 
            '//button[@class="Button2 Button2_size_l Button2_view_action Button2_width_max"]'
            )
        self.assertIn("Далее", btn_next.text)   
        # time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


