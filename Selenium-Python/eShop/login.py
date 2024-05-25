import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObject.loginPage import LoginData,LoginPage


def setUp(self):
    global browser
    browser = self.driver

def test_login(self,inputemail,inputpassw):
    browser.get(LoginData.url)
    self.assertIn(LoginData.title, browser.title)
    browser.find_element(By.CLASS_NAME, LoginPage.login_btn).click()
    self.assertEqual(browser.current_url , LoginData.url_login)
    browser.find_element(By.ID, LoginPage.email).send_keys(inputemail)
    browser.find_element(By.ID, LoginPage.passw).send_keys(inputpassw)
    browser.find_element(By.ID, LoginPage.remember_me).click()
    browser.find_element(By.CLASS_NAME, LoginPage.login_klik).click()

def test_msg_login_success(self): 
    self.assertEqual(browser.current_url , LoginPage.successlogin_url)

def test_msg_login_failed(self,message):
    error = browser.find_element(By.CLASS_NAME, LoginPage.error_false_pass).text
    self.assertIn(message, error)

if __name__ == '__main__':
    unittest.main()
