from framework.base_page import BasePage


class IndexPage(BasePage):
    Login = "xpath=>//*[@id='root']/div/div[2]/header/div/div[2]/button[3]"
    LI = "xpath=>/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[2]/span"
    Name = "name=>username"
    Password = "name=>password"
    Button = "xpath=>/html/body/div[4]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button"


    def login_page(self,name,password):
        self.click(self.Login)
        self.wait(1)
        self.click(self.LI)
        self.wait(3)
        self.type(self.Name,name)
        self.wait(1)
        self.type(self.Password,password)
        self.wait(1)
        self.click(self.Button)
        self.wait(3)

