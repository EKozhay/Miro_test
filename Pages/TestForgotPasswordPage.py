from Pages.BasePage import BasePage
from Locators import Locators


class TestForgetPasswordPage(BasePage):
    def click_continue(self):
        continue_button = self.find_element(Locators.forgot_password_continue)
        self.click_button(continue_button)

    def click_back_to_sing_in(self):
        back_to_sing_in_button = self.find_element(Locators.back_to_sing_in_button)
        self.click_button(back_to_sing_in_button)