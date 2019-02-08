from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome('./chromedriver.exe', options = options)

driver.get('https://www.facebook.com/')
print ("Opend facebook...")
a = driver.find_element_by_id('email')
a.send_keys('stevenjang31@gmail.com')
print ("Email Id entered...")
b = driver.find_element_by_id('pass')
b.send_keys('fm134816')
print ("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()
post_box=driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
post_box.send_keys("Test.")
sleep(5)
post_it=driver.find_elements_by_class_name("_6c0o")
post_it[0].click()
print ("Posted!!!!")