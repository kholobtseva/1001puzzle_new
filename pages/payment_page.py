import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Payment_page(Base):
    """ Класс содержащий локаторы и методы для страницы оформления заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    order_order = "//*[@id='bx-soa-total']/div[2]/div[5]/a"

    # Getters

    def get_order_button(self):
        return self.driver.find_element(By.XPATH, self.order_order)

    # Actions
    def click_order_button(self):
        self.get_order_button().click()

    # Methods

    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            print("""Чтобы не делать реальный заказ, не кликаем на кнопку оформить""")
            #self.click_order_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment")




