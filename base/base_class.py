import datetime
#import allure

class Base():
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    """ Method get current url """
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        if type(word) != str:
            value_word = word.text
        else:
            value_word = word
        assert value_word == result
        print(f"Good value {result}")

    """Method assetion"""
    def assertion(self, val1, val2, assert_text):
        assert val1 == val2
        print(assert_text)

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "C:\\Users\\kholo\\PycharmProjects\\1001puzzle_new\\screen\\screenshot_" + now_date + ".png"
        self.driver.save_screenshot(name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"Good value url: {result}")