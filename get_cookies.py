from selenium import webdriver
import pickle
import sys
import time


driver = webdriver.Chrome()
driver.get('https://accounts.google.com/') #! Enter Your Credentials Here and login

check_login = input("Have You Sucessfully Logged in ? (y for yes n for no) : ") #! Enter 'y' for yes 'n' for no

if(check_login.lower() == 'y'):
    pickle.dump(driver.get_cookies(), open("lnme.pkl", "wb"))
    print("Logged in Sucessfully\nExiting in 10 seconds......")
    time.sleep(10)
    driver.quit()

else:
    print("Unsucessfull !!!!\n\
Please Login Again.")
    sys.exit()

