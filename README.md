
# Email Spam Bot

We made a python script that is run on the selenium framework. It allows you to choose how many emails you would like to send to a recepient, futhermore, you are able to change the speed, text body, and subject of the email. We currently have 2 versions, one where you are able to input the information in the code personally(spamV1.py) and another version which manages to ask your input in the terminal(spamV2.py). If you would like to get the first version working just follow the steps below.

# How to set it up?
 
1) First thing your going to do is change "EMAIL OF SENDER" on line 13 to include your actual email for example "marioJudah@gmail.com" so that line 13 is driver.find_element_by_xpath('//input[@type="email"]').send_keys("marioJudah@gmail.com").
2) Second thing your going to do is change "SENDER EMAIL PASSWORD" on line 16 to your password for that email that your using to send the email, in my case with email "marioJudah@gmail.com" the password is "pass1", knowing this line 16 would hypothetically look like driver.find_element_by_xpath('//input[@type="password"]').send_keys("pass1")
3) Third thing your going to do is change "EMAIL OF RECIEVER" on line 25 to the email that you are sending it to, so for example in this case I want to send it to "drake1@gmail.com", knowing this line 25 would look like   driver.find_element_by_xpath("//textarea[@name='to']").send_keys("drake1@gmail.com")
4) Fourthly your going to have to change "EMAIL SUBJECT " on line 26 to what you want the email subject to be, for example I want to talk about github in this email so the subject will be "Github", knowing this line 26 would look like driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Github " + str(j)) 
5) Last but not least your going to have to change "EMAIL BODY " on line 26 to what you want the email text body to say, for example I just want to say "hi" in this email , knowing this line 27 would look like  driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys("hi " + str(j))



# How to run the file?

To run the file you are going to have to download two modules that being selenium, and web driver manager. 
To install both of these modules you just have to type:
```
pip install selenium
pip install webdriver-manager
```
In your local terminal. After doing so to run the file (assuming your in the directory folder of your file) you just have to type:
```
python spam.py
```
In your local terminal and that should do it. 

# NOTE
If you ever run into any issues please feel free to contact mohammed.satar.alrasheed@gmail.com or open an issue.
