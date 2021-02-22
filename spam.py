from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome(executable_path = "Users/MAIN/Downloads/chromedriver")

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
sleep(2)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys("email")
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(2)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("password")
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(2)
driver.get("https://mail.google.com")
sleep(2)

def speed(j):
  driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
  sleep(3)
  driver.find_element_by_xpath("//textarea[@name='to']").send_keys("speedmero@gmail.com")
  driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("yo it worked btw " + str(j))
  driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys("yo it worked btw " + str(j))
  driver.find_element_by_xpath("//div[text()='Send']").click()
  sleep(3)

for i in range(10):
  j = i + 1
  speed(j)
  sleep(3)
