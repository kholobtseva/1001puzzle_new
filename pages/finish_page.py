import allure
from base.base_class import Base
from pages.cart_page import Cart_page
from utilities.logger import Logger


class Finish_page(Base):
    """ Класс содержащий локаторы и методы для страницы оформления заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        with allure.step("Finish ordering"):
            Logger.add_start_step(method="check_contacts")
            print(self.get_current_url())
            self.assert_url("https://1001puzzle.ru/personal/order/make/")
            """Чтобы не делать реальный заказ на сайте, не кликаем на кнопку Оформить"""
            self.get_screenshot()
            print("Скриншот выполнен")
            print("Очищаем корзину после тестов")
            ct = Cart_page(self.driver)
            ct.cleaning_cart()
            print("Очиcтили корзину после тестов")
            Logger.add_end_step(url=self.driver.current_url, method="finish")




