from selenium import webdriver
import pickle
import sys
import time

driver = webdriver.Chrome()
driver.get('https://accounts.google.com/') #! Enter Your Credentials Here and login

check_login = input("Have You Sucessfully Logged in ? (y/n): ") #! Enter 'y' for yes 'n' for no

if check_login.startswith("y") == True: # Incase the user enters 'yes' or 'no' instead of 'y'/'n'
    pickle.dump(driver.get_cookies(), open("lnme.pkl", "wb"))
    print("Logged in Sucessfully \n Exiting in a few seconds...")
    time.sleep(5) # Ten seconds is too long
    driver.quit()
elif check_login.startswith("n") == True: # Created a new outcome for the user saying no 
    print("You chose to not login. \n Quitting...")
    time.sleep(5)
    driver.quit()
else:
    print("Login Attempt Unsuccessful! \n
Please Try Again.")
    sys.exit()
