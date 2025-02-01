import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.manufacturers_page import Manufacturers_page
import time
from utilities.logger import Logger

class Cart_page(Base):
    """ Класс содержащий локаторы и методы для Корзины"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    basket_clear = "//button[@name= 'BasketClear']"
    basket_item = "//tr[@data-entity='basket-item']"
    basket = "//a[./i[@class='ph-bold ph-tote'] and ./span[text()='Корзина']]"
    empty_cart = "/html/body/div[2]/div[6]/div[2]/div[2]"
    clear_cart = "//span[@class='basket-item-actions-remove visible-xs']"
    list_item_remove = "//td[@class='basket-items-list-item-remove hidden-xs']"
    basket_item_actions_remove = "basket-item-actions-remove"
    basket_total_price = "div[data-entity='basket-total-price']"
    total_weight = "//div[@class='basket-checkout-block-total-description']"
    order = "//button[@data-entity='basket-checkout-button']"

    # Getters

    def get_wait_for_clear_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.basket_clear)))

    def get_products_basket_item(self):
        return self.driver.find_elements(By.XPATH, self.basket_item)

    def get_cart_link(self):
        return self.driver.find_element(By.XPATH, self.basket)

    def get_empty_cart(self):
        return self.driver.find_element(By.XPATH, self.empty_cart)

    def get_clean_cart(self):
        return self.driver.find_element(By.XPATH, self.clear_cart)

    def get_remove_cell(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.list_item_remove)))

    def get_remove_cell_f(self):
        return self.driver.find_element(By.XPATH, self.list_item_remove)

    def get_total_price_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.basket_total_price)))

    def get_total_weight_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.total_weight)))

    def get_total_price(self):
        return self.get_total_price_element().text.split(' р.')[0].replace(' ', '')

    def get_total_weight(self):
        return self.driver.find_element(By.XPATH, self.total_weight).text.split(': ')[1].split()[0].replace(' ', '')

    def get_order_page(self):
        return self.driver.find_element(By.XPATH, self.order)

    # Actions

    def cart_link_click(self):
        self.get_cart_link().click()

    def empty_cart_click(self):
        self.get_empty_cart().click()

    def clean_cart_click(self):
        self.get_clean_cart().click()

    def get_order_page_click(self):
        self.driver.execute_script("arguments[0].click();", self.get_order_page())

    # Methods
    def get_to_cart(self):
        with allure.step("Get to cart"):
            Logger.add_start_step(method="get_to_cart")
            """Переходим в корзину"""
            url = "https://1001puzzle.ru/personal/cart/"
            self.driver.execute_script(f"window.location.href = '{url}'")
            self.get_wait_for_clear_cart()
            Logger.add_end_step(url=self.driver.current_url, method="get_to_cart")

    def products_in_cart(self):
        with allure.step("Products in cart (Adding products in cart to dictionary products_in_cart)"):
            Logger.add_start_step(method="products_in_cart")
            """Добавляем товары из корзины в словарь  products_in_cart: ключ - имя, вес товара - 1, цена за штуку - 2, стоимость - 5,
            количество - стоимость/цена за штуку"""

            products_in_cart = {}
            for i in self.get_products_basket_item():
                products_in_cart[i.text.split('\n')[0]] = i.text.split('\n')[1:7]
            print(f"Продукты в корзине:")
            for k, v in products_in_cart.items():
                print(k, *v)
            for k, v in products_in_cart.items():
                products_in_cart[k][1] = float(products_in_cart[k][1].split()[0])  # Вес товара в граммах
                products_in_cart[k][2] = int(
                    products_in_cart[k][2].replace(' ', '').replace('р.', ''))  # Цена товара за штуку в рублях
                products_in_cart[k][5] = int(
                    products_in_cart[k][5].replace(' р.', '').replace(' ', ''))  # Стоимость товара в рублях
            print(f"В корзине {len(products_in_cart)}")
            Logger.add_end_step(url=self.driver.current_url, method="products_in_cart")
            return products_in_cart

    def cleaning_cart(self):
        with allure.step("Cleaning cart"):
            Logger.add_start_step(method="cleaning_cart")
            mn = Manufacturers_page(self.driver)

            cart_start = mn.count_adding_products()
            print(f"Состояние корзины {cart_start}")

            if int(cart_start) != 0:
                self.cart_link_click()
                print("Заходим в корзину, чтобы очистить")
                time.sleep(2)
                try:
                    self.empty_cart_click()
                except:
                    cart_start = int(mn.count_adding_products())
                    for i in range(0, cart_start):
                        try:
                            try:
                                self.clean_cart_click()
                            except:
                                try:
                                    # Находим родительский элемент <td>
                                    remove_cell = self.get_remove_cell()
                                except:
                                    print(f"Error removing item: Нет родительского элемента. Нет товаров.")
                                # JavaScript для удаления класса 'hidden-xs'
                                self.driver.execute_script("arguments[0].classList.remove('hidden-xs');", remove_cell)
                                # Теперь крестик должен быть виден и кликабелен
                                remove_button = remove_cell.find_element(By.CLASS_NAME, self.basket_item_actions_remove)
                                remove_button.click()
                                time.sleep(2)

                        except Exception as e:
                            print(f"Error removing item: Корзина пустая")

                print("Очистили корзину")
                self.driver.back()
                Logger.add_end_step(url=self.driver.current_url, method="cleaning_cart")

    def get_cart_total_price(self):
        with allure.step("Get the total_price of products in the cart"):
            Logger.add_start_step(method="get_cart_total_price")
            print(f"Итого в корзине товаров на сумму (элемент корзины):  {self.get_total_price()} руб.")
            Logger.add_end_step(url=self.driver.current_url, method="get_cart_total_price")
            return int(self.get_total_price())

    def get_cart_total_weight(self):
        with allure.step("Get the total weight of products in the cart"):
            Logger.add_start_step(method="get_cart_total_weight")
            print(f"Вес товаров в корзине (элемент корзины):  {self.get_total_weight()} кг.")
            Logger.add_end_step(url=self.driver.current_url, method="get_cart_total_weight")
            return float(self.get_total_weight())

    def count_cart_total_price(self, dict_products_in_cart):
        with allure.step("Count the total price of products in the cart"):
            Logger.add_start_step(method="count_cart_total_price")
            summa = 0
            for prod in dict_products_in_cart.keys():
                summa += round(dict_products_in_cart[prod][5] / dict_products_in_cart[prod][2]) * \
                         dict_products_in_cart[prod][
                             2]
            print(f"Итоговая стоимость товаров в корзине в результате вычисления: {summa} руб.")
            Logger.add_end_step(url=self.driver.current_url, method="count_cart_total_price")
            return summa

    def count_cart_total_weight(self, dict_products_in_cart):
        with allure.step("Count the total weight of products in the cart"):
            Logger.add_start_step(method="count_cart_total_weight")
            summa = 0
            for prod in dict_products_in_cart.keys():
                summa += dict_products_in_cart[prod][1] * (
                    round(dict_products_in_cart[prod][5] / dict_products_in_cart[prod][2]))
            print(f"Суммарный вес товаров в корзине в результате вычисления: {summa} кг")
            Logger.add_end_step(url=self.driver.current_url, method="count_cart_total_weight")
            return summa
