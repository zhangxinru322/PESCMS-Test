from selenium.webdriver.common.by import By
"""以下为登陆页面的元素配置信息"""
#用户名
login_username = (By.NAME,"account")
#密码
login_password = (By.NAME,"passwd")
#点击登录按钮
login_button = (By.CLASS_NAME,"am-btn.am-radius.am-btn-primary.am-btn-block.am-margin-bottom")
#获取登录异常信息
login_error_info = (By.XPATH,"//div[contains(@class,'ui-dialog-content')]")
#点击关闭异常提示框按钮
login_error_button = (By.CLASS_NAME,"ui-dialog-close")