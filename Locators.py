class Locators(object):

    '''Login Page'''
    email_field = "//input[@name='email'][@id='email']"
    password_field = "//input[@name='password'][@id='password']"
    sing_up_error = "//div[@class='signup__error-item']"
    sing_in_button = "//button[@class='signup__submit']"
    sing_in_label = "//h1[@class='signup__title-form']"
    forgot_password_button = "//div[@class='signup__recovery']//a"
    forgot_password_continue = "//button[@class='signup__submit']"
    back_to_sing_in_button = "//button[@class='signup__submit signup__submit--shrink']"