import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('http://www.jd.com')

driver.find_element_by_xpath('//*[@id="su"]').click()

time.sleep(10)
driver.find_element_by_xpath('//html/body/div[1]/div[3]/div[1]/div[3]/div[1]/h3/a[1]').click()
handles = driver.window_handles
# print(handles)
driver.switch_to.window(handles[0])
time.sleep(5)
driver.minimize_window()

time.sleep(3)

driver.quit()