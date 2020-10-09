import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_experimental_option('prefs', {
        'profile.default_content_setting_values.notifications': 2})
    driver = webdriver.Chrome(options=chrome_options, executable_path=r'/Users/jk/chromedriver')
    yield driver
    driver.quit()