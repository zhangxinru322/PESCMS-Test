from selenium.webdriver.common.by import By
"""以下为登陆页面的元素配置信息"""
#用户名
login_username = (By.XPATH, "//input[@placeholder='账号']")
#密码
login_password = (By.XPATH, "//input[@placeholder='密码']")
#验证码
login_code = (By.XPATH, "//input[@placeholder='验证码']")
#点击登录按钮
login_button = (By.CLASS_NAME,"el-button.login-btn.el-button--primary.el-button--medium")
#获取登录异常信息
login_error_info = (By.CLASS_NAME,"el-message--error")
#点击关闭异常提示框按钮
# login_error_button = (By.CLASS_NAME,"ui-dialog-close")