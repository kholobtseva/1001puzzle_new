import allure
from pages.login_page import Login_page
from pages.catalog_frame import Catalog_frame
from pages.manufacturers_page import Manufacturers_page
from pages.cart_page import Cart_page
import time

def test_cart(driver, setup, setup_group):

    """Запускать, когда в корзине уже есть добавленные продукты"""
    print("Start test_cart Проверка соответствия названий, итоговой суммы и веса добавленных товаров в корзине.")

    login = Login_page(driver)
    login.authorisation()

    catalog = Catalog_frame(driver)
    catalog.get_into_catalog_click()

    manuf_of_puzzle = Manufacturers_page(driver)
    manufact = manuf_of_puzzle.manufacturers()

    manuf_of_puzzle.go_to_manufactures(manufact, 0)
    products = manuf_of_puzzle.dict_of_products()

    cart = Cart_page(driver)
    cart.get_to_cart()
    time.sleep(1)
    print(f"Количество товаров в корзине {manuf_of_puzzle.number_text()}\n")

    dict_products_in_cart = cart.products_in_cart()
    tot_price_get = cart.get_cart_total_price()
    tot_weight_get = cart.get_cart_total_weight()
    tot_price_count = cart.count_cart_total_price(dict_products_in_cart)
    tot_weight_count = cart.count_cart_total_weight(dict_products_in_cart)
    cart.assertion(tot_price_get, tot_price_count,
              'Итоговая сумма в корзине равна подсчитанной сумме товаров с учетом их количества. Test GOOD!')

    cart.assertion(tot_weight_get, tot_weight_count,
                   'Итоговый вес товаров в корзине равен подсчитанному весу товаров с учетом их количества. Test GOOD!')

    n = 0
    for k in list(dict_products_in_cart.keys()):
        assert k in list(products.keys())
        n += 1
        print(f"Название товара {n} в корзине соответствует названию этого товара в каталоге. Test GOOD!")

    print("Finish test_cart")


