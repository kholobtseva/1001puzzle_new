from pages.login_page import Login_page
from pages.contacts_page import Contacts_page
from pages.cart_page import Cart_page

def test_contacts(driver, setup_group, setup):

    print("Start test_contacts")

    login = Login_page(driver)
    login.authorisation()

    driver.get("https://1001puzzle.ru/contacts/")

    cp = Contacts_page(driver)
    cp.check_contacts()

    print("Finish test_contacts")

    print("Очищаем корзину после тестов")
    ct = Cart_page(driver)
    ct.cleaning_cart()
    print("Очиcтили корзину после тестов")


