import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time
from utilities.logger import Logger


class Login_page(Base):
    """ Класс содержащий локаторы и методы для формы Авторизации"""

    url = 'https://1001puzzle.ru/'
    name = '************'
    password = '*******'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    enter_pick = "/html/body/div[2]/header/div/div[2]/ul/li[1]/a/span"
    email_login_link = 'a[href="#auth_by_login"]'
    wait_for_login_form2 = "#auth_by_login"
    user_name = "USER_LOGIN_POPUP"
    user_password = "//div[@id='auth_by_login']//input[@id='USER_PASSWORD_POPUP']"
    login_button = "button[data-type='login']"
    cabinet = "//span[contains(text(),'Кабинет')]"

    # Getters

    def get_into(self):
        return  self.driver.find_element(By.XPATH, self.enter_pick)

    def get_email_login(self):
        # Ждем, пока ссылка станет кликабельной
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.email_login_link))
        )

    def get_into_email_login(self):
        # Ждем появления формы вход
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.wait_for_login_form2))  # или другой селектор формы
        )

    def get_user_name(self):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button)))

    def get_cabinet_word(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, self.cabinet)))

    # Actions
    def get_into_click(self):
        self.get_into().click()

    def click_email_enter(self):
        self.get_email_login().click()

    def go_to_enter(self):
        self.get_into_email_login().click()

    def input_user_name(self, name):
        self.get_user_name().send_keys(name)
        print("Ввели имя пользователя")

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print("Ввели пароль")

    def click_login_button(self):
        self.get_login_button().click()
        print("Кликнули на кнопку, чтобы залогиниться")

    # Methods
    def accept_cookies(self):
        with allure.step("Accept cookies"):
            """Соглашаемся и принимаем куки """
            try:
                accept_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cookie-block-wrap button.cookie-block-button"))
                )
                accept_button.click()
                print("Кликнули на кнопку, чтобы принять куки")
            except Exception as e:
                print(f"Ошибка: не удалось нажать на кнопку 'Принять': {e}")

    def authorisation(self):
        """ Авторизация на сайте """
        with allure.step("Authorisation"):
            Logger.add_start_step(method="authorisation")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.accept_cookies()
            time.sleep(10)
            self.get_into_click()
            try:
                self.click_email_enter()
                self.get_into_email_login()
            except Exception as e:
                print(f"Ошибка при переключении на вкладку входа по email: {e}")

            self.input_user_name(self.name)
            self.input_user_password(self.password)
            self.click_login_button()
            self.assert_word(self.get_cabinet_word(), "Кабинет")
            Logger.add_end_step(url=self.driver.current_url, method="authorisation")