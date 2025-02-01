from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        yield driver
    except Exception as e:
        print(f"Error initializing webdriver: {e}")
        raise # Перепроброс исключения для pytest
    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error quitting webdriver: {e}")

@pytest.fixture(scope="function")
def setup():
    print("\nStart test")
    yield
    print("\nFinish test")

@pytest.fixture(scope="module")
def setup_group():
    print("\nEnter system")
    yield
    print("\nExit system")

