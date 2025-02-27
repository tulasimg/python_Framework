from base.selenium_driver import SeleniumDriver
import time

class LoginPage(SeleniumDriver):
 
    # Constructor will accept driver
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _title_xpath ="(//i[starts-with(@class,'a-icon')])[1]"
    _search_id = "twotabsearchtextbox"
    _sign_in_xpath = "//span[text()='Hello, Sign in']"
    _email_field_id = "ap_email"
    _pwd_field_id = "ap_password"
    _continue_button_id = "continue"
    _login_button_id ="signInSubmit"

    # Actions

    def assertLoginPgTitle(self):
        self.assertTitle("Amazon",self._title_xpath,locatorType="xpath")


    def search(self,data):
        self.sendKeysWithEnter(data,self._search_id,locatorType="id")


    def clickSigninLink(self):
        self.elementClick(self._sign_in_xpath,locatorType="xpath")


    def enterEmail(self,email):
        self.sendKeys(email,self._email_field_id,locatorType="id")

      
    def clickContinueBtn(self):
        self.elementClick(self._continue_button_id)


    def enterPassword(self, pwd):
        self.sendKeys(pwd, self._pwd_field_id)


    def clickLoginBtn(self):
        self.elementClick(self._login_button_id)

    # Business logic


    def login(self,data,email,password):
        time.sleep(2)
        self.clickSigninLink()

        self.enterEmail(email)
        self.clickContinueBtn()
        self.take_Screenshot(driver=self.driver)
        self.enterPassword(password)
        self.clickLoginBtn()
        time.sleep(2)
        self.search(data)
        time.sleep(5)


