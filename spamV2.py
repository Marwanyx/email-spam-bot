from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome(executable_path = "Users/MAIN/Downloads/chromedriver")
print("Please input the email your are sending from")
SenderEmail = input()
print("Please input the password of the email your are sending from(password will be hidden)")
SenderPass =  getpass()
print("Please input the the email your are sending to")
EmailSend = input()
print("Please input the subject of the email you are sending")
Subject =input()
print("Please input the text body of the email you are sending")
Text =input()
print("Please input the amount of times you would like this email to be sent")
Sent =int(input())

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
sleep(2)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(SenderEmail)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(2)
driver.find_element_by_xpath('//input[@type="password"]').send_keys(str(SenderPass))
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(2)
driver.get("https://mail.google.com")
sleep(2)

def speed(j):
  driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
  sleep(3)
  driver.find_element_by_xpath("//textarea[@name='to']").send_keys(EmailSend)
  driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys(Subject + str(j))
  driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys(Text + str(j))
  driver.find_element_by_xpath("//div[text()='Send']").click()
  sleep(2)

for i in range(Sent):
  j = i + 1
  speed(j)