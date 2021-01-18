
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
Password = '....'

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

sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[1]/div/div[1]/aside/ul/li[7]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div[3]/div/a[1]').click()

sleep(2)
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

    
def month_int(argument):
    switcher = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    # print (switcher.get(argument, "Invalid month"))
    return switcher.get(argument, "Invalid month")


month = month_text(month)


from_box_month = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/span[1]').text

if from_box_month != month:
    f_month = month_int(from_box_month)
    target_month = month_int(month)
    while f_month != target_month:
        if f_month > target_month:
            next_ = driver.find_element_by_xpath('/html/body/div[3]/div[1]/a[2]').click()
        else:
            pre = driver.find_element_by_xpath('/html/body/div[3]/div[1]/a[1]').click()



sleep(1)

day = False
i = 1
while not day:
    # print(i)
    try:
        driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[1]/td['+str(i)+']/a').click()
        day = True
    except:
        i += 1
        # sleep(1)
        

search = driver.find_element_by_xpath('//*[@id="searchMyButton"]').click()

parti = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[7]/div/div/div[2]/div[3]/div[4]/div/div[1]/table/tbody/tr/td[12]/a').click()


students = []
end = False
i = 1

while not end:
    try:
        name = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div[2]/div[2]/table/tbody/tr['+str(i)+']/td[1]/div').text
        students = students + [name]
        i += 1
    except:
        end = True
  
        
  
for i in range(len(students)):
    print("student # "+str(i+1)+" name: " + students[i] )

        
        











