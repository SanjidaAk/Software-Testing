import time
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class FlightBooking:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        logging.basicConfig(filename='flight.log', format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%y/%m/%d %H:%M:%S', level=logging.INFO, filemode='w')

    def open_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info('ChromeDriver was opened successfully')

    def select_round_trip(self):
        round_trip = self.driver.find_element(By.ID, 'RoundTrip')
        round_trip.click()
        time.sleep(2)

    def select_city(self, element_id, city_code):
        city_input = self.driver.find_element(By.ID, element_id)
        city_input.click()
        city_input.send_keys(city_code)
        time.sleep(4)
        city_list = self.driver.find_elements(By.XPATH, '//li[@class="list"]')
        for city in city_list:
            if city_code.upper() in city.text:
                city.click()
                break
        time.sleep(3)
        logging.info(f'{city_code.upper()} was selected')

    def select_date(self, month, day):
        date_element = self.driver.find_element(By.XPATH, f'//td[@data-month="{month}"]/a[text()="{day}"]')
        date_element.click()
        time.sleep(2)

    def select_travel_details(self, adults, children, travel_class):
        adults_dropdown = Select(self.driver.find_element(By.ID, 'Adults'))
        adults_dropdown.select_by_index(adults - 1)
        time.sleep(2)

        children_dropdown = Select(self.driver.find_element(By.ID, 'Childrens'))
        children_dropdown.select_by_value(str(children))
        time.sleep(2)
        logging.info(f'{adults} adults and {children} children were selected')

        more_options = self.driver.find_element(By.ID, 'MoreOptionsLink')
        more_options.click()
        time.sleep(1)

        class_dropdown = Select(self.driver.find_element(By.ID, 'Class'))
        class_dropdown.select_by_visible_text(travel_class)
        time.sleep(2)
        logging.info(f'{travel_class} Class was selected')

    def search_flights(self):
        search_flights = self.driver.find_element(By.ID, 'SearchBtn')
        search_flights.click()
        wait = WebDriverWait(self.driver, 20)
        non_stop_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[text()="Non-stop"]')))
        non_stop_checkbox.click()
        time.sleep(2)

    def change_currency(self, currency_name):
        currency = self.driver.find_element(By.XPATH, '//span[@class="fs-2 c-inherit"]')
        currency.click()
        time.sleep(2)
        selected_currency = self.driver.find_element(By.XPATH, f'//span[text()="{currency_name}"]')
        selected_currency.click()
        time.sleep(2)
        logging.info(f'Currency changed to {currency_name}')

    def select_flight(self):
        first_flight = self.driver.find_element(By.XPATH,
                                                '//div[@class="col-19"]/div[2]/div[7]/div[1]/div[1]/div[2]/div[4]/button')
        first_flight.click()
        time.sleep(2)
        child_window = self.driver.window_handles[1]
        self.driver.switch_to.window(child_window)
        time.sleep(10)

    def continue_booking(self):
        continue_booking = self.driver.find_element(By.ID, 'itineraryBtn')
        continue_booking.location_once_scrolled_into_view
        time.sleep(2)
        continue_booking.click()
        time.sleep(2)
        continue_booking_2 = self.driver.find_element(By.ID, 'LoginContinueBtn_1')
        continue_booking_2.click()
        time.sleep(2)

    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        logging.info('Screenshot was captured')

    def close_driver(self):
        self.driver.close()
        logging.info('The Driver was closed successfully')
