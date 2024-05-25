import time
import logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Booking:
    def __init__(self):
        self.setup_logging()
        self.driver = self.setup_driver()
        self.open_browser()

    def setup_logging(self):
        logging.basicConfig(filename='flight.log', format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%y/%m/%d %H:%M:%S', level=logging.INFO, filemode='w')

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
        return driver

    def open_browser(self):
        self.driver.get('https://katalon-demo-cura.herokuapp.com/')
        self.driver.maximize_window()
        logging.info('ChromeDriver was opened successfully')

    def login(self, username, password):
        element = self.driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
        element.click()
        time.sleep(2)

        username_field = self.driver.find_element(By.ID, "txt-username")
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "txt-password")
        password_field.send_keys(password)
        time.sleep(2)

        login_button = self.driver.find_element(By.ID, "btn-login")
        login_button.click()

    def make_appointment(self, facility, hospital_readmission, program, visit_date, comment):
        sta_drpdwn = Select(self.driver.find_element(By.XPATH, "//select[@id='combo_facility']"))
        sta_drpdwn.select_by_value(facility)
        time.sleep(1)

        if hospital_readmission:
            button = self.driver.find_element(By.NAME, "hospital_readmission")
            button.click()
            time.sleep(1)

        radio_button = self.driver.find_element(By.XPATH, f"//input[@value='{program}']")
        radio_button.click()
        time.sleep(1)

        date_picker = self.driver.find_element(By.ID, "txt_visit_date")
        date_picker.send_keys(visit_date)
        time.sleep(1)

        comment_text = self.driver.find_element(By.NAME, "comment")
        comment_text.send_keys(comment)
        time.sleep(1)

        booking_button = self.driver.find_element(By.ID, "btn-book-appointment")
        booking_button.click()

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    booking = Booking()
    try:
        booking.login("John Doe", "ThisIsNotAPassword")
        booking.make_appointment("Seoul CURA Healthcare Center", True, "Medicaid", "05/05/2024", "Very Important")
    finally:
        booking.close_browser()
