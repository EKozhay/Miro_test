import pytest
from LoginPage import LoginPage
from Pages.TestForgotPasswordPage import TestForgetPasswordPage

'''To execute the tests firstly you need to specify correct email and password for Miro user.'''
email = ''
password = ''


@pytest.mark.run(order=1)
def test_sunny_login(browser):
    login_page = LoginPage(browser)

    login_page.go_to_site()
    login_page.enter_email(email=email)
    login_page.enter_password(password=password)
    login_page.click_sing_in()
    login_page.check_page_is_opened_successfully(link_part='app')


@pytest.mark.run(order=2)
def test_email_field_empty_after_refresh(browser):
    login_page = LoginPage(browser)

    login_page.go_to_site()
    login_page.enter_email(email=email)
    login_page.refresh_page()
    actual_value = login_page.get_value_from_field()
    assert actual_value == 'email'


@pytest.mark.run(order=3)
def test_forgot_password(browser):
    login_page = LoginPage(browser)
    forgot_password = TestForgetPasswordPage(browser)

    login_page.go_to_site()
    login_page.enter_email(email=email)
    login_page.click_forgot_password()
    login_page.check_page_is_opened_successfully(link_part='recover')
    login_page.enter_email(email=email)
    forgot_password.click_continue()
    login_page.check_page_is_opened_successfully(link_part='success')
    forgot_password.click_back_to_sing_in()
    login_page.check_page_is_opened_successfully(link_part='login')


@pytest.mark.run(order=4)
@pytest.mark.parametrize('email, password, expected_message',
                        [('', '123', ['Please enter your email address.']),
                         ('123', '', ['Please enter your password.']),
                         ('', '', ['Please enter your email address.', 'Please enter your password.']),
                         ('123', '123', [f'The email or password you entered is incorrect.\nPlease try again.'])],
                         ids=['Empty email.', 'Empty login.', 'Empty email and login.', 'Email and login are field'])
def test_sing_up_error(browser, email, password, expected_message):
    login_page = LoginPage(browser)

    login_page.go_to_site()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_sing_in()
    login_page.check_login_page_is_downloaded()
    actual_messages = login_page.get_sing_up_error()
    assert actual_messages == expected_message