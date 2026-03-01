import page
from base.base import Base
class Pagelogin(Base):
    #输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)
    #输入密码
    def page_input_password(self,password):
        self.base_input(page.login_password,password)
    #输入验证码
    def page_input_code(self,code):
        self.base_input(page.login_code, code)
    #点击登录按钮
    def page_click_login_button(self):
        self.base_click(page.login_button)
    #获取登录异常信息
    def page_get_error_info(self):
        # 先等错误提示文本加载完成
        self.base_wait_element_text(page.login_error_info, "用户不存在/密码错误")
        # 再获取文本
        return self.base_get_text(page.login_error_info)
    #点击关闭异常提示按钮
    # def page_error_close(self):
    #     self.base_click(page.login_error_button)
    #截图
    def page_screenshot(self):
        self.base_screenshot()

    #组合业务方法
    def page_login(self,username,password,code):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_code(code)
        self.page_click_login_button()