import time
import logging
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoWebShopAutomation:
    def __init__(self):
        self.setup_logging()
        self.driver = self.setup_driver()

    def setup_logging(self):
        logging.basicConfig(
            filename='flight.log',
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%y/%m/%d %H:%M:%S',
            level=logging.INFO,
            filemode='w'
        )

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(executable_path='C:\\Windows\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        return driver

    def open_website(self, url):
        self.driver.get(url)
        logging.info(f"Opened website: {url}")

    def click_link(self, link_text):
        item = self.driver.find_element(By.LINK_TEXT, link_text)
        item.click()
        logging.info(f"Clicked link: {link_text}")
        time.sleep(2)

    def click_checkbox(self, xpath, skip_index=None):
        checkboxes = self.driver.find_elements(By.XPATH, xpath)
        for index, checkbox in enumerate(checkboxes):
            if index == skip_index:
                continue
            checkbox.click()
            logging.info(f"Clicked checkbox at index: {index}")

    def click_element(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        logging.info(f"Clicked element with xpath: {xpath}")

    def run(self):
        self.open_website('https://demowebshop.tricentis.com/')
        self.click_link('Computers')
        self.click_link('Desktops')
        self.click_link('Build your own computer')
        self.click_checkbox("//input[@type='checkbox']", skip_index=1)
        self.click_element("//input[@id='product_attribute_16_3_6_18']")
        self.click_element("//input[@id='add-to-cart-button-16']")


if __name__ == "__main__":
    automation = DemoWebShopAutomation()
    automation.run()
