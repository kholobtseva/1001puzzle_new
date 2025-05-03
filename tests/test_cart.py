import allure
from pages.login_page import Login_page
from pages.catalog_frame import Catalog_frame
from pages.manufacturers_page import Manufacturers_page
from pages.cart_page import Cart_page
import time


@allure.title("Проверка корзины")
@allure.description("Тест проверяет соответствия названий, итоговой суммы и веса добавленных товаров в корзине.")
def test_cart(driver, setup, setup_group):

    """Запускать, когда в корзине уже есть добавленные продукты"""
    print("Start test_cart Проверка соответствия названий, итоговой суммы и веса добавленных товаров в корзине.")

    with allure.step("Залогиниваемся на сайте"):
        login = Login_page(driver)
        login.authorisation()

    with allure.step("Переходим в каталог."):
        catalog = Catalog_frame(driver)
        catalog.get_into_catalog_click()

    with allure.step("Получаем словарь из всех товаров на сайте"):
        manuf_of_puzzle = Manufacturers_page(driver)
        manufact = manuf_of_puzzle.manufacturers()

    with allure.step("Получаем словарь из всех товаров выбранного производителя."):
        manuf_of_puzzle.go_to_manufactures(manufact, 0)
        products = manuf_of_puzzle.dict_of_products()

    with allure.step("Переходим в корзину."):
        cart = Cart_page(driver)
        cart.get_to_cart()
        time.sleep(1)
        print(f"Количество товаров в корзине {manuf_of_puzzle.number_text()}\n")

    with allure.step("Получаем словарь добавленных в корзину продуктов, суммарный вес продуктов, стоимость товаров в корзине."):
        dict_products_in_cart = cart.products_in_cart()
        tot_price_get = cart.get_cart_total_price()
        tot_weight_get = cart.get_cart_total_weight()

    with allure.step(
            "Вычисляем суммарный вес продуктов, стоимость товаров в корзине."):
        tot_price_count = cart.count_cart_total_price(dict_products_in_cart)
        tot_weight_count = cart.count_cart_total_weight(dict_products_in_cart)

    with allure.step(
                "Сравниваем подсчитанную стоимость товаров в корзине  с отображаемой в корзине"):
        cart.assertion(tot_price_get, tot_price_count,
                  'Итоговая сумма в корзине равна подсчитанной сумме товаров с учетом их количества. Test GOOD!')

    with allure.step(
                "Сравниваем подсчитанный вес товаров в корзине  с отображаемым в корзине"):
        cart.assertion(tot_weight_get, tot_weight_count,
                   'Итоговый вес товаров в корзине равен подсчитанному весу товаров с учетом их количества. Test GOOD!')

    with allure.step(
            "Сравниваем названия товаров в каталоге с отображаемыми в корзине"):
        n = 0
        for k in list(dict_products_in_cart.keys()):
            assert k in list(products.keys())
            n += 1
            print(f"Название товара {n} в корзине соответствует названию этого товара в каталоге. Test GOOD!")

    print("Finish test_cart")


