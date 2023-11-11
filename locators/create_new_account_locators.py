from selenium.webdriver.common.by import By


class CreateNewAccountPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//*[@id = 'firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//*[@id = 'lastname']")
    EMAIL_FIELD = (By.XPATH, "//*[@id = 'email_address']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id = 'password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//*[@id = 'password-confirmation']")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id='send2' and @class='action login primary']")

    TEXT_THX_FOR_REGISTRATION_MSG = "Thank you for registering with Main Website Store."
