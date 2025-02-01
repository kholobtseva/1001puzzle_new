import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Client_information_page(Base):
    """ Класс содержащий информацию о клиенте"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://1001puzzle.ru/personal/private/"

    # locators

    last_name = "//input[@name='LAST_NAME']"
    first_name = "//input[@name='NAME']"
    middle_name = "//input[@name='SECOND_NAME']"
    phone = "//input[@name='PERSONAL_PHONE']"
    emale = "//input[@name='EMAIL']"
    save_button = "//button[@name='save']"
    changes = "//font[@class='notetext']"
    personal_data = "//li[@aria-current='page']"

    # Getters

    def get_last_name(self):
        return self.driver.find_element(By.XPATH, self.last_name)

    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.first_name)

    def get_middle_name(self):
        return self.driver.find_element(By.XPATH, self.middle_name)

    def get_phone(self):
        return self.driver.find_element(By.XPATH, self.phone)

    def get_emale(self):
        return self.driver.find_element(By.XPATH, self.emale)

    def get_save_button(self):
        return self.driver.find_element(By.XPATH, self.save_button)

    def get_str_changes(self):
        return self.driver.find_element(By.XPATH, self.changes)

    def get_str_changes_text(self):
        return self.get_str_changes().text

    def get_personal_data_elem_text(self):
        return self.driver.find_element(By.XPATH, self.personal_data).text

    # Actions

    def clear_last_name(self):
        self.get_last_name().clear()

    def input_last_name(self, user_last_name):
        self.get_last_name().send_keys(user_last_name)

    def clear_first_name(self):
        self.get_first_name().clear()

    def input_first_name(self, user_first_name):
        self.get_first_name().send_keys(user_first_name)

    def clear_middle_name(self):
        self.get_middle_name().clear()

    def input_middle_name(self, user_middle_name):
        self.get_middle_name().send_keys(user_middle_name)

    def clear_phone(self):
        self.get_phone().clear()

    def input_phone(self, user_phone):
        self.get_phone().send_keys(user_phone)

    def clear_emale(self):
        self.get_emale().clear()

    def input_emale(self, user_emale):
        self.get_emale().send_keys(user_emale)

    def click_save_button(self):
        self.get_save_button().click()

    # Methods

    def input_information(self):
        with allure.step("Input information about a client"):
            Logger.add_start_step(method="input_information")
            self.driver.get(self.url)
            assert self.get_personal_data_elem_text() == "Персональные данные"
            print("Успешно перешли на страницу 'Персональные данные'")
            self.clear_last_name()
            self.input_last_name('Иванова')
            print('Ввели фамилию')
            self.clear_first_name()
            self.input_first_name("Елена")
            print('Ввели имя')
            self.clear_middle_name()
            self.input_middle_name("Петровна")
            print('Ввели отчество')
            self.clear_phone()
            self.input_phone("+7 (926) 305-06-22")
            print('Ввели телефон')
            self.clear_emale()
            self.input_emale("xxxxx@gmail.com")
            self.click_save_button()
            print('Ввели e-mail')
            assert self.get_str_changes_text() == "Изменения сохранены"
            print("Данные успешно сохранились, получили надпись 'Изменения сохранены'")
            Logger.add_end_step(url=self.driver.current_url, method="input_information")
