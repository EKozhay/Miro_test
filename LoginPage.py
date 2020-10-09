from Pages.BasePage import BasePage
from Locators import Locators


class LoginPage(BasePage):
    def enter_email(self, email):
        email_field = self.find_element(Locators.email_field)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find_element(Locators.password_field)
        password_field.clear()
        password_field.send_keys(password)

    def click_sing_in(self):
        sing_in_button = self.find_element(Locators.sing_in_button)
        self.click_button(sing_in_button)

    def get_sing_up_error(self):
        errors_text = []
        errors = self.find_elements(Locators.sing_up_error)
        for i in errors:
            error_text = i.text
            errors_text.append(error_text)
        return errors_text

    def check_login_page_is_downloaded(self):
        self.find_element(Locators.sing_in_label)

    def check_page_is_opened_successfully(self, link_part='miro'):
        assert link_part in self.driver.current_url

    def click_forgot_password(self):
        forgot_password_button = self.find_element(Locators.forgot_password_button)
        self.click_button(forgot_password_button)

    def get_value_from_field(self):
        email_field = self.find_element(Locators.email_field)
        prop = email_field.get_property("id")
        print(prop)
        return prop


