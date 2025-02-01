import allure
import time
import pytest
from pages.login_page import Login_page
from pages.catalog_frame import Catalog_frame
from pages.manufacturers_page import Manufacturers_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page


@pytest.mark.run(order=3)
@allure.description("Test buy product 1 Добавление продуктов в корзину.")
def test_buy_product1(driver, setup):

    driver.delete_all_cookies()
    print("Start test_buy_product1 по добавлению товаров в корзину")

    login = Login_page(driver)
    login.authorisation()

    cart = Cart_page(driver)
    cart.cleaning_cart()

    catalog = Catalog_frame(driver)
    catalog.get_into_catalog_click()

    manuf_of_puzzle = Manufacturers_page(driver)
    manufact = manuf_of_puzzle.manufacturers()

    manuf_of_puzzle.go_to_manufactures(manufact, 0)
    ids = manuf_of_puzzle.dict_of_id()

    i = 1
    for k in list(ids.keys())[0:3]:
        manuf_of_puzzle.add_product_to_cart(i, ids[k][1], ids[k][0])
        i += 1

    print("Finish test_buy_product1")



@pytest.mark.run(order=1)
@allure.description("Test buy product 2 Добавление продуктов в корзину.")
def test_buy_product2(driver, setup_group, setup):

    driver.delete_all_cookies()
    print("Start test_buy_product2 по добавлению товаров в корзину")

    login = Login_page(driver)
    login.authorisation()

    cart = Cart_page(driver)
    cart.cleaning_cart()

    catalog = Catalog_frame(driver)
    catalog.get_into_catalog_click()

    manuf_of_puzzle = Manufacturers_page(driver)
    manufact = manuf_of_puzzle.manufacturers()

    manuf_of_puzzle.go_to_manufactures(manufact, 34)
    ids = manuf_of_puzzle.dict_of_id()

    i = 1
    for k in list(ids.keys())[0:1]:
        manuf_of_puzzle.add_product_to_cart(i, ids[k][1], ids[k][0])
        i += 1

    print("Finish test_buy_product2")



@pytest.mark.run(order=2)
@allure.description("Test buy product 3 Добавление продуктов в корзину.")
def test_buy_product3(driver, setup):

    driver.delete_all_cookies()
    print("Start test_buy_product3 по добавлению товаров в корзину и оформлению заказа с вводом данных пользователя")

    login = Login_page(driver)
    login.authorisation()

    cart = Cart_page(driver)
    cart.cleaning_cart()

    catalog = Catalog_frame(driver)
    catalog.get_into_catalog_click()

    manuf_of_puzzle = Manufacturers_page(driver)
    manufact = manuf_of_puzzle.manufacturers()

    manuf_of_puzzle.go_to_manufactures(manufact, 12)
    ids = manuf_of_puzzle.dict_of_id()

    i = 1
    for k in list(ids.keys())[0:3]:
        manuf_of_puzzle.add_product_to_cart(i, ids[k][1], ids[k][0])
        i += 1

    cip = Client_information_page(driver)
    cip.input_information()

    cart.driver.get("https://1001puzzle.ru/personal/cart/")

    cart.get_order_page_click()

    time.sleep(20)
    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print("Finish test_buy_product3")

