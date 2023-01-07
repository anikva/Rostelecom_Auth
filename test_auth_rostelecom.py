from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestLogin:

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru")

    def setup(self):
        self.email = "ilchenkoqa@gmail.com"
        self.password = "QUWSZhy5Xn8fXPk"
        self.phone = "+7 949 325-01-61"
        self.login = "rtkid_1670079455122"

    def close(self):
        self.driver.quit()

    def login_by_email(self, email, password):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 5)

    def login_by_phone(self, phone, password):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(phone)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 5)

    def login_by_login(self, login, password):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(login)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 5)

    def login_by_email_positive(self):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(self.email)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 5)

    def login_by_phone_positive(self):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(self.phone)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 5)

    def login_by_login_positive(self):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(self.login)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 5)

    def test_login_by_email_positive(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.setup()
        WebDriverWait(self.driver, 10)
        self.login_by_email_positive()
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='lk-btn']")))
        self.close()

    def test_login_by_phone_positive(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.setup()
        WebDriverWait(self.driver, 10)
        self.login_by_phone_positive()
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='lk-btn']")))
        self.close()

    def test_login_by_login_positive(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.setup()
        WebDriverWait(self.driver, 10)
        self.login_by_login_positive()
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='lk-btn']")))
        self.close()

    @pytest.mark.parametrize("email", ["ilchenkoqa@gmaill.com"],
                             ids=["email_negative"])
    @pytest.mark.parametrize("password", ["QUWSZhy5Xn8fXPk", "QUWSZhy5Xn8fXP"],
                             ids=["password_positive", "password_negative"])
    def test_login_by_email_neg(self, email, password):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.login_by_email(email, password)
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='form-error-message']")))
        self.close()

    @pytest.mark.parametrize("phone", ["+7 949 325-01"],
                             ids=["phone_negative"])
    @pytest.mark.parametrize("password", ["QUWSZhy5Xn8fXPk", "QUWSZhy5Xn8fXP"],
                             ids=["password_positive", "password_negative"])
    def test_login_by_phone_neg(self, phone, password):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.login_by_phone(phone, password)
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='form-error-message']")))
        self.close()

    @pytest.mark.parametrize("login", ["rtkid"],
                             ids=["login_negative"])
    @pytest.mark.parametrize("password", ["QUWSZhy5Xn8fXPk", "QUWSZhy5Xn8fXP"],
                             ids=["password_positive", "password_negative"])
    def test_login_by_login_neg(self, login, password):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.login_by_login(login, password)
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='form-error-message']")))
        self.close()

    @pytest.mark.parametrize("id", [""],
                             ids=["id_null"])
    @pytest.mark.parametrize("password", ["QUWSZhy5Xn8fXPk", "QUWSZhy5Xn8fXP"],
                             ids=["password_positive", "password_negative"])
    def test_login_by_null_negative(self, id, password):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='kc-login']")))
        self.login_by_email(id, password)
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']")))
        self.close()

    def teardown(self
                 ):
        self.close
