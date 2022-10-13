from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
service = Service(executable_path=ChromeDriverManager().install())

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)
driver.get("http://192.168.1.1/")
time.sleep(5)

btn_user_name = driver.find_element(By.ID, "username").send_keys("admin")  
btn_password = driver.find_element(By.ID, "password").send_keys("admin")
btn_login = driver.find_element(By.XPATH, "//div[@class='login_user_g_right']").click()
time.sleep(20)
driver.switch_to.frame("menufrm")
btn_password = driver.find_element(By.ID, "network").click()

time.sleep(10)

driver.switch_to.default_content()

driver.switch_to.frame("basefrm")

btn_password = driver.find_element(By.NAME, "wlancfgText").click()

driver.switch_to.frame("showfrm")

campo_password = driver.find_element(By.ID, "wlWpaPsk")
campo_password.clear()
campo_password.send_keys("holamundo")

time.sleep(10)
#btn_save = driver.find_element(By.ID, "save").click()
print(driver.page_source)
time.sleep(2)
driver.quit()
exit()