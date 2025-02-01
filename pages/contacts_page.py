import allure
from utilities.logger import Logger
from selenium.webdriver.common.by import By
from base.base_class import Base

class Contacts_page(Base):
    """ Класс содержащий локаторы и методы для страницы Контакты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    contacts_header = "//h1[contains(text(),'Контакты')]"
    store_address = "//h2[contains(text(),'Адрес магазина')]"
    contact_data = "//h2[contains(text(),'Контакты')]"
    details = "//h2[contains(text(),'Реквизиты')]"
    feedback = "//h2[contains(text(),'Обратная связь')]"

    # Getters

    def get_contacts_header(self):
        return self.driver.find_element(By.XPATH,
                                           self.contacts_header)
    def get_store_address(self):
        return self.driver.find_element(By.XPATH,
                                           self.store_address)
    def get_contact_data(self):
        return self.driver.find_element(By.XPATH,
                                           self.contact_data)
    def get_details(self):
        return self.driver.find_element(By.XPATH,
                                           self.details)
    def get_feedback(self):
        return self.driver.find_element(By.XPATH,
                                           self.feedback)

    # Actions

    def text_contact_header(self):
        return self.get_contacts_header().text

    def text_store_address(self):
        return self.get_store_address().text

    def text_contact_data(self):
        return self.get_contact_data().text

    def text_get_details(self):
        return self.get_details().text

    def text_get_feedback(self):
        return self.get_feedback().text

    # Methods

    def check_contacts(self):
        with allure.step("Check contact information"):

            Logger.add_start_step(method="check_contacts")
            self.assert_url("https://1001puzzle.ru/contacts/")

            assert self.text_contact_header() == "Контакты"
            print("Заголовок страницы 'Контакты' найден")

            assert self.text_store_address() == "Адрес магазина"
            print("Раздел 'Адрес магазина' найден")

            assert self.text_contact_data() == "Контакты"
            print("Раздел с контактными данными 'Контакты' найден")

            assert self.text_get_details() == "Реквизиты"
            print("Раздел  'Реквизиты' найден")

            assert self.text_get_feedback() == "Обратная связь"
            print("Раздел  'Обратная связь' найден")
            Logger.add_end_step(url=self.driver.current_url, method="check_contacts")








