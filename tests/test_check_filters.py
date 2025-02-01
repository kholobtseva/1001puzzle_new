from pages.login_page import Login_page
from pages.catalog_frame import Catalog_frame
from pages.manufacturers_page import Manufacturers_page
from selenium.webdriver import ActionChains, Keys


def test_check_filters(driver, setup_group, setup):


    print("Start test_check_filters")

    login = Login_page(driver)
    login.authorisation()

    catalog = Catalog_frame(driver)
    catalog.get_into_catalog_click()



    """Выбираем интервал цены с помощью ползунка"""
    action = ActionChains(driver)
    action.click_and_hold(catalog.choose_price()).move_by_offset(-110, 0).release().perform()
    print("Price+")

    manuf_of_puzzle = Manufacturers_page(driver)
    manufact = manuf_of_puzzle.manufacturers()
    manuf_of_puzzle.go_to_manufactures(manufact, 22)
    manuf_of_puzzle.check_filters()

    print("Finish test_check_filters")


