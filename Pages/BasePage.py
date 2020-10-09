from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://miro.com/login/"

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                      message=f"Can't find elements by locator {locator}")

    def click_button(self, button):
        self.driver.execute_script("arguments[0].click();", button)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def refresh_page(self):
        self.driver.refresh()