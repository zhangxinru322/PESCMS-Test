from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base:
    #初始化
    def __init__(self,driver):
        self.driver=driver
    #查找元素方法
    def base_find_element(self,loc,timeout=50):
        return WebDriverWait(self.driver,timeout).until(
            EC.visibility_of_element_located(loc)
        )
    def base_wait_element_text(self, loc, msg, timeout=20):
        """等待元素文本包含预期内容，专门处理动态错误提示"""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(loc, msg)
        )
    #点击方法
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #输入方法
    def base_input(self,loc,value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
    #获取文本方法
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    #截图方法
    def base_screenshot(self):
        self.driver.get_screenshot_as_file(r"D:\zhangxinru\VS\3\PESCMS\screenshot.png")
