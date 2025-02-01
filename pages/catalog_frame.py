import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Catalog_frame(Base):
    """ Класс содержащий локаторы и методы для каталога"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    cabinet_pick = "//*[contains(text(), 'Кабинет')]"
    catalog_button_pick = "//button[@class='catalog_btn']"
    polzunok = "//input[@id='range']"

    # Getters

    def get_into_catalog(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.cabinet_pick)))
        return  self.driver.find_element(By.XPATH, self.catalog_button_pick)

    def choose_price(self):
        return self.driver.find_element(By.XPATH, self.polzunok)

    # Actions
    def get_into_catalog_click(self):
        with allure.step("Get into catalog"):
            self.get_into_catalog().click()


