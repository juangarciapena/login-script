import sys
import time
from datetime import date

import datetime
import schedule
from selenium import webdriver

b = 1
tcp = 1
tcpf = 1

def action():
    global b
    global tcp
    global tcpf
   
    print("loggin in...")
    #write user and pass
    username = "xxxxxxxx" 
    password = "yyyyyyyy"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='D:\\Nuevacarpeta\\chromedriver.exe', options=options)
    driver.get("website") #write site

    username_textbox = driver.find_element_by_id("usuario")
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id("clave")
    password_textbox.send_keys(password)

    inputElement = driver.find_element_by_link_text("INGRESAR")
    inputElement.submit()
    print("logged in.")


    today = date.today()
    weekDayVec = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado TCP", "Domingo"]
    # 0 lunes - 6 domingo /// 0 lun,3 jue, 5 sab

    numDay = today.weekday()
    currentT = datetime.datetime.now()
    
    f = open('confirmacion.txt','a')
    f.write('\n{}/{} {}: Login a las {}'.format(today.day,today.month,weekDayVec[numDay],currentT.strftime("%H:%M")))
    f.close()   

    time.sleep(1500) # stay logged in 1500sec

    driver.quit()

    '''    
    #multiple login with exception
    if tcp == 0:
        if tcpf == 0:
            b = 0
        else:
            tcpf = 0

    if numDay != 5:   #5 si no es sabado 
        b = 0 
    else:
        tcp = 0
    '''
    
    #Login 3 times
    if tcp == 0:
        if tcpf == 0:
            b = 0
        else:
            tcpf = 0
    

    tcp = 0
    
    

# lunes
schedule.every().monday.at("07:52").do(action)
schedule.every().monday.at("10:25").do(action)
schedule.every().monday.at("11:45").do(action)

# jueves
schedule.every().thursday.at("07:51").do(action)
schedule.every().thursday.at("10:21").do(action)
schedule.every().thursday.at("11:45").do(action)

# sabado - 
schedule.every().saturday.at("07:50").do(action)
schedule.every().saturday.at("09:57").do(action)
schedule.every().saturday.at("13:18").do(action)


while b == 1:
    schedule.run_pending()
    time.sleep(1)

sys.exit
