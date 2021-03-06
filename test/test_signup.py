import time

from model.credSignup import SignupCred
import pytest
from random import randrange

random = None


@pytest.allure.step("Signup with happy pass and with approve by email link")
def test_registration_with_approve(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Fill in form by valid data"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password="TestTest12", captcha="1111", promo_code=""))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.registration_event_message_ru
    with pytest.allure.step("Enter to admin and click to registration link"):
        app.admin.registration_with_approve()
    with pytest.allure.step("Assert that user is approved "):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.approve_registration_message_ru


@pytest.allure.step("Signup with nick name number only")
def test_sign_up_nick_number_only(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with nick name number only"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username=str(random),
                               password="TestTest12", captcha="1111", promo_code=""))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.registration_event_message_ru


@pytest.allure.step("Signup with password caps")
def test_sign_up_password_upper(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password caps"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password=("TestTest12").upper(), captcha="1111", promo_code=""))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.registration_event_message_ru


@pytest.allure.step("Signup with password only number")
def test_sign_up_password_number(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password only number"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password="123456789", captcha="1111", promo_code=""))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.registration_event_message_ru


@pytest.allure.step("Signup with password only special symbols")
def test_sign_up_password_special(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password only special symbols"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password='!@#$%^/\&*()~?|}"\'{:[]<>,.', captcha="1111", promo_code=""))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.registration_event_message_ru


@pytest.allure.step("See password button")
def test_sign_up_password_see_password(app):
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Open signup pop-up"):
                app.registration.open_signup_popup()
    with pytest.allure.step("Fill in password field"):
        app.driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("TestTest12")
    with pytest.allure.step("Click on the 'see password' button"):
        app.driver.find_element_by_xpath(app.selectors.see_password_button).click()
        time.sleep(0.5)
        assert app.warning.get_value(xpath=app.selectors.signup_password_field) == "TestTest12"


@pytest.allure.step("Close pop-up by outside click")
def test_sign_up_with_promo(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password only special symbols"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password="TestTest12", promo_code="testdd", captcha="1111"))
        with pytest.allure.step("Assert for text about email"):
            assert app.warning.get_outer_text(
                app.selectors.event_message) == app.text.registration_event_message_ru
        with pytest.allure.step("Enter to admin and click to registration link"):
            app.admin.registration_with_approve()
        with pytest.allure.step("Assert that user is approved "):
            assert app.warning.get_outer_text(
                app.selectors.event_message) == app.text.approve_registration_message_ru
        with pytest.allure.step("Assert that verify pop-up is opened"):
            assert app.warning.get_outer_text(app.selectors.h4_promo_pop_up) == app.text.h4_promo_title_ru
            assert app.warning.get_outer_text(app.selectors.text_promo_pop_up) == app.text.text_promo_pop_up


@pytest.allure.step("Close pop-up by outside click")
def test_close_outside(app):
    with pytest.allure.step("Open 'sign up' pop-up"):
        app.registration.open_signup_popup()
    with pytest.allure.step("Click out side pop-up"):
        app.session.click_out_side()
    with pytest.allure.step("Assert that pup-up is closed"):
        assert not app.session.element_is_display(app.selectors.signup_h4_title)


"""
@pytest.allure.step("Signup with happy pass")
def test_sign_up_happy_pass(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Fill in form by valid data"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password="TestTest12", captcha="1111", promo_code=""))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            app.selectors.event_message) == app.text.registration_event_message_ru


def test_sign_up(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))


@pytest.allure.step("Signup with space before email")
def test_sign_up_with_space_before(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with space before email"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email=" testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password="TestTest12", captcha="1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"


@pytest.allure.step("Signup with space after email")
def test_sign_up_with_space_after(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with space after email"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com ", username="triced" + str(random),
                               password="TestTest12", captcha="1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"


@pytest.allure.step("Signup with nick name caps")
def test_sign_up_nick_email_upper(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with email and nick upper"):
                app.registration.sign_up_happy_pass(SignupCred(email=("testpm8+" + str(random) + "@gmail.com ").upper(),
                                                               username=("triced" + str(random)).upper(),
                                                               password="TestTest12", captcha="1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"


@pytest.allure.step("Signup with password Low")
def test_sign_up_password_low(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password low"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                               password=("TestTest12").lower(), captcha="1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"



@pytest.allure.step("Signup with space after nickname")
def test_sign_up_nick_space_after(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with space after nickname"):
                app.registration.sign_up_happy_pass(
                    SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random) + " ",
                               password="TestTest12", captcha="1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.get_outer_text(
            "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

"""