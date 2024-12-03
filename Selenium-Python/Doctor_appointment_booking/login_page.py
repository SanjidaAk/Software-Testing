import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TestCuraApplication:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get('https://katalon-demo-cura.herokuapp.com/')
       

    def button_click(self):
        make_appointment = self.driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
        make_appointment.click()
        time.sleep(2)

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "txt-username")
        password_field = self.driver.find_element(By.ID, "txt-password")
        login_button = self.driver.find_element(By.ID, "btn-login")

        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        time.sleep(2)

    @pytest.mark.order(1)
    def test_button(self):
        """Test Case - Make Appointment button is clickable."""
        self.button_click()

    @pytest.mark.order(2) #login 1
    def login_valid(self):
        """Test Case - Login with valid input."""
        self.button_click()
        self.login("John Doe", "ThisIsNotAPassword")    
        
    @pytest.mark.order(3) #login 2
    def login_invalid(self):
        """Test Case - Login with invalid input."""
        self.button_click()
        self.login("NotFound", "Invalid")

    @pytest.mark.order(4)
    def login_empty(self):
        """Test Case - Login with empty feilds."""
        self.button_click()
        self.login(" ", "Invalid")    
        
