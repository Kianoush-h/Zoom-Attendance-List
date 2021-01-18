
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""

from selenium import webdriver 
from time import sleep 
from selenium.webdriver.firefox.options import Options



LogInUrl = 'https://us04web.zoom.us/web/sso/login?en=signin'

Company_Domain = 'concordia-ca'

UserName = 'concordia.ca\K_HARATI'
Password = 'KAmm@16973003'

Date = '01/10/2021' # mm/dd/yy



options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options, executable_path='./geckodriver.exe')


driver.get(LogInUrl) 

login_sso =  driver.find_element_by_xpath('//*[@id="domain"]')
login_sso.clear()
login_sso.send_keys(Company_Domain)
login_sso.submit()

send = False

while (not send):
    try:
        UserName_input = driver.find_element_by_xpath('//*[@id="userNameInput"]')
        UserName_input.send_keys(UserName)
        send = True
    except:
        pass


Password_input = driver.find_element_by_xpath('//*[@id="passwordInput"]')
Password_input.send_keys(Password)

Password_input.submit()



driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div[1]/aside/ul/li[7]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div[3]/div/a[1]').click()


from_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[7]/div/div/div[2]/div[3]/div[3]/form/div/button[1]').click()


month = int(Date.split('/')[0])


def month_text(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    # print (switcher.get(argument, "Invalid month"))
    return switcher.get(argument, "Invalid month")

month = month_text(month)






















