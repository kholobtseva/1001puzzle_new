import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from utilities.logger import Logger


class Manufacturers_page(Base):
    """ Класс содержащий локаторы и методы для страницы производителей"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    category_list = ".category_list__item_in ul"
    brand_puzzle1 = f"//a[@data-range-baselink='/pazly/proizvoditeli/"
    brand_puzzle2 = "/']"
    brand_title = "//h1[@class='title']"
    product_slider_card_item = ".product-slider__card_item"
    product_parent_element_bx = ".//div[starts-with(@id, 'bx_')]"
    cart_title = ".//div[@class='card_title']"
    data_id = ".//button[starts-with(@data-id, '4')]"
    product_id1 = ".//button[@data-id="
    product_id2 = "]"
    element_cart = "//a[./i[@class='ph-bold ph-tote'] and ./span[text()='Корзина']]"
    number = "./following-sibling::span[@class='number']"
    detailes_filter = "//label[@for='arrFilter_228_2561098286']"
    cart_link_elem = "//a[./i[@class='ph-bold ph-tote'] and ./span[text()='Корзина']]"
    topic_filter = "//label[@for='arrFilter_134_1807530521']"
    combo_box_filter = "//*[@id='kombox-filter']/form/ul/li[11]/div[1]"
    clarifying_filter = "//*[@id='kombox-filter']/form/ul/li[11]/div[2]/div[1]/label"
    element_locator = (By.XPATH, "//span[@class='number']")

    # Getters

    def manufacturer_lists_element_present(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.category_list)))

    def get_all_located_manufacturers(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, self.category_list)))

    def brand_puzzle(self, mun):
        return self.driver.find_element(By.XPATH,
                                        self.brand_puzzle1 + mun + self.brand_puzzle2)

    def get_brand_title(self):
        return self.driver.find_element(By.XPATH, self.brand_title)

    def get_div_id(self, id_bx):
        return self.driver.find_element(By.ID, id_bx)

    def cart_element_link(self):
        return self.driver.find_element(By.XPATH, self.element_cart)

    def number_element(self):
        return self.cart_element_link().find_element(By.XPATH, self.number)

    def number_products_in_cart(self, n):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                    f"//*[contains(text(), {n})]")))

    def get_detailes_filter(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.detailes_filter)))
        return self.driver.find_element(By.XPATH, self.detailes_filter)

    def cart_link(self):
        return self.driver.find_element(By.XPATH, self.cart_link_elem)

    def get_number_element(self):
        return self.cart_link().find_element(By.XPATH, self.number_element)

    def get_topic_filter(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.topic_filter)))
        return self.driver.find_element(By.XPATH, self.topic_filter)

    def get_combo_box_filter(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.combo_box_filter)))
        return self.driver.find_element(By.XPATH, self.combo_box_filter)

    def get_clarifying_filter(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.clarifying_filter)))
        return self.driver.find_element(By.XPATH, self.clarifying_filter)

    # Actions

    def brand_puzzle_click(self, num):
        self.brand_puzzle(num).click()

    def brand_title_text1(self):
        return (' '.join(self.get_brand_title().text.split()[1:]))

    def brand_title_text0(self):
        return self.get_brand_title().text.split()[0]

    def get_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.product_slider_card_item)

    def get_id_products(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.product_slider_card_item)

    def product_add_to_cart(self, id, id_bx):
        return self.get_div_id(id_bx).find_element(By.XPATH, self.product_id1 + id + self.product_id2)

    def product_title_element(self, id_bx):
        return self.get_div_id(id_bx).find_element(By.XPATH, self.cart_title)

    def product_title(self, id_bx):
        return self.product_title_element(id_bx).text.split('\nАртикул:')[0]

    def product_add_to_cart_click(self, id, id_bx):
        self.product_add_to_cart(id, id_bx).click()

    def detailes_filter_click(self):
        self.get_detailes_filter().click()

    def number_text(self):
        return self.number_element().text

    def click_topic_filter(self):
        time.sleep(5)
        self.get_topic_filter().click()

    def click_combo_box_filter(self):
        self.get_combo_box_filter().click()

    def click_get_clarifying_filter(self):
        time.sleep(5)
        self.get_clarifying_filter().click()

    # Methods

    def manufacturers(self):
        with allure.step("Manufacturers"):
            Logger.add_start_step(method="manufacturers")
            # Находим все списки ul в контейнере category_list__item_in
            manufactur = []
            for manufacturer_list in self.get_all_located_manufacturers():  # Перебираем каждый список ul
                for link in manufacturer_list.find_elements(By.TAG_NAME, "a"):
                    manufactur.append(link.text.strip())
            Logger.add_end_step(url=self.driver.current_url, method="manufacturers")

            return manufactur

    def go_to_manufactures(self, manufacturers, num_in_manufactures):
        with allure.step("Go to manufactures"):
            """Переход на страницу производителя"""
            Logger.add_start_step(method="go_to_manufactures")
            num = manufacturers[num_in_manufactures].lower()
            if num == "cherry pazzi":
                num = "cherry_pazzi"
                self.brand_puzzle_click(num)
                brand_title_text = "cherry pazzi"
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

            elif num == "cobble hill":
                num = "cobble-hill"
                self.brand_puzzle_click(num)
                brand_title_text = "cobble hill"
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

            elif num == "step puzzle":
                num = "step"
                self.brand_puzzle_click(num)
                brand_title_text = "step puzzle"
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

            elif num == "рыжий кот":
                num = "ryzhiy_kot"
                self.brand_puzzle_click(num)
                brand_title_text = "рыжий кот"
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

            elif num == "art puzzle (heide)":
                num = "art_puzzle"
                self.brand_puzzle_click(num)
                brand_title_text = "art puzzle (heide)"
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

            elif num == "winning moves":
                num = "winning_moves"
                self.brand_puzzle_click(num)
                brand_title_text = "winning moves"
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

            else:
                self.brand_puzzle_click(num)

                try:
                    brand_title_text = self.brand_title_text1()
                except:
                    brand_title_text = self.brand_title_text0()

                print(brand_title_text)
                self.assert_word(brand_title_text.upper(), manufacturers[num_in_manufactures])
                Logger.add_end_step(url=self.driver.current_url, method="go_to_manufactures")

    def dict_of_products(self):
        with allure.step("Adding products from the main page of a brand to the dictionary dict_of_products"):
            "Добавляем карточки продуктов в словарь products: Цена - 3"
            Logger.add_start_step(method="dict_of_products")
            products = {}
            for i in self.get_cards():
                products[i.text.split('\n')[0]] = i.text.split('\n')[1:6]
            for k, v in products.items():
                products[k][3] = int(products[k][3].split()[0].replace(' ', ''))  # Цена товара за штуку в рублях
                products[k][1] = products[k][1].split()[0].replace(' ', '')  # Вес товара единицы товара в кг
            """Для проверки заполнения словаря и для отладки"""
            # for k, v in products.items():
            #     print(k, *v)
            Logger.add_end_step(url=self.driver.current_url, method="dict_of_products")
            return products

    def dict_of_id(self):
        with allure.step("Adding id to the dictionary ids"):
            """Заполняем словарь ids где ключ - название товара, а значение список из id товара и id карточки товара"""
            Logger.add_start_step(method="dict_of_id")
            ids = {}
            for id in self.get_id_products():
                try:
                    product_parent_element = id.find_element(By.XPATH, self.product_parent_element_bx)
                    bx_id = product_parent_element.get_attribute("id")  # id карточки товара
                    product_name = product_parent_element.find_element(By.XPATH, self.cart_title).text.split('\n')[
                        0]  # Ключ словаря
                    try:
                        id_element = product_parent_element.find_element(By.XPATH, self.data_id)
                        data_id = id_element.get_attribute("data-id")  # id товара
                        ids[product_name] = [data_id, bx_id]
                    except:
                        ids[product_name] = ['', '']
                except Exception as e:
                    print(f"Ошибка при обработке карточки: {e}")
            """Для проверки заполнения словаря и для отладки"""
            # for k, v in ids.items():
            #     print(k, *v)
            # print(len(ids))
            Logger.add_end_step(url=self.driver.current_url, method="dict_of_id")
            return ids

    def count_adding_products(self):
        with allure.step("Count adding products"):
            Logger.add_start_step(method="count_adding_products")
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method="count_adding_products")
            return self.number_text()

    def add_product_to_cart(self, n, id_bx, id):
        with allure.step("Add product to cart"):
            Logger.add_start_step(method="add_product_to_cart")
            """ Добавляем в корзину товар"""
            action = ActionChains(self.driver)
            print(f"Название товара {n}:   {self.product_title(id_bx)}")
            action.move_to_element(self.product_add_to_cart(id, id_bx)).perform()
            self.product_add_to_cart_click(id, id_bx)

            def wait_for_cart_number_change(locator):
                """Ожидает изменения числа в корзине."""

                try:
                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                    initial_count = element.text  # Запоминаем начальное значение
                    print(f"Начальное количество товаров в корзине: {initial_count}")

                    WebDriverWait(self.driver, 30, poll_frequency=1).until(
                        lambda driver: driver.find_element(*locator).text != initial_count
                    )
                    updated_element = self.driver.find_element(*locator)
                    updated_count = updated_element.text
                    print(f"Количество товаров в корзине изменилось на: {updated_count}")
                    return updated_count  # Возвращаем обновленное значение

                except TimeoutException:
                    print("Таймаут ожидания! Количество товаров в корзине не изменилось.")
                    return None  # Возвращаем None, если таймаут
                except StaleElementReferenceException:
                    print("Элемент стал устаревшим! Попробуйте другой локатор или подход.")
                    return None  # Возвращаем None, если элемент устарел
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
                    return None  # Возвращаем None, если другая ошибка

            """Подтверждение добавления товара"""
            updated_cart_count = wait_for_cart_number_change(self.element_locator)
            if updated_cart_count:
                self.number_products_in_cart(n)
                print(f"{n}-й товар добавлен в корзину.")
                print(f"Количество товаров в корзине {self.number_text()}\n")
                Logger.add_end_step(url=self.driver.current_url, method="add_product_to_cart")

    def products_in_cart_number(self):
        Logger.add_start_step(method="products_in_cart_number")
        print(f"Количество товаров в корзине {self.count_adding_products()}\n")
        Logger.add_end_step(url=self.driver.current_url, method="products_in_cart_number")

    def wait_for_filter_update(self, filter_label_for):
        with allure.step("Wait for filter update"):
            """Ожидает, пока span внутри label с указанным 'for' атрибутом станет невидимым."""

            Logger.add_start_step(method="wait_for_filter_update")

            wait = WebDriverWait(self.driver, 100)  # Уменьшили время ожидания для этого конкретного случая
            try:
                wait.until(EC.invisibility_of_element_located(
                    (By.XPATH, f"//label[@for='{filter_label_for}']//span[@class='kombox-cnt']")))
            except TimeoutException:
                print(f"Таймаут ожидания: span внутри label с for='{filter_label_for}' не стал невидимым.")
                self.get_screenshot()  # Сделайте скриншот для анализа
            Logger.add_end_step(url=self.driver.current_url, method="wait_for_filter_update")

    def check_filters(self):
        with allure.step("Check_filters"):
            """ Проверка работы фильтров """

            Logger.add_start_step(method="check_filters")
            try:
                wait = WebDriverWait(self.driver, 100)
                self.detailes_filter_click()
                wait.until(EC.invisibility_of_element_located(
                    (By.XPATH, "//label[@for='arrFilter_228_2561098286']/span[@class='kombox-cnt']")))
                self.click_topic_filter()
                self.wait_for_filter_update("arrFilter_228_2561098286")
                self.driver.execute_script("window.scrollTo(0, 600)")

                try:
                    # Ожидание загрузки элемента
                    wait = WebDriverWait(self.driver, 30)
                    paysage_element = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "li[data-id='peyzazh-191'] .kombox-filter-property-name")))

                    # Клик по элементу с помощью JavaScript
                    self.driver.execute_script("arguments[0].parentNode.click();", paysage_element)  # Click on parent <div>
                    self.click_get_clarifying_filter()
                    self.wait_for_filter_update("arrFilter_191_3622229225")
                    self.driver.execute_script("window.scrollTo(0, -600)")
                    time.sleep(5)
                    self.get_screenshot()
                    print("Скриншот выполнен")
                    self.driver.quit()
                    return True
                except (TimeoutException, NoSuchElementException) as e:
                    print(f"Ошибка при клике на 'Пейзаж': {e}")
                    return False
            except TimeoutException:
                print("Таймаут ожидания превышен.")
                self.get_screenshot()  # Сделайте скриншот для анализа ошибки
            Logger.add_end_step(url=self.driver.current_url, method="check_filters")
