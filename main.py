import undetected_chromedriver as uc
uc.install()
import pickle
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
import time
from datetime import date, datetime
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pause
import re
import sys


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#? MAKE SURE TO GET THE COOKIES FIRST

#? MAKE SURE TO GET THE COOKIES FIRST

#? MAKE SURE TO GET THE COOKIES FIRST

#? MAKE SURE TO GET THE COOKIES FIRST

#? MAKE SURE TO GET THE COOKIES FIRST

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




#!####### TIME #########################
now = datetime.now()
current_hour = int(now.strftime("%H"))


if current_hour >= 12 and current_hour < 24:
    time_sleep = 28 - current_hour
    print(f"Sleeping for {time_sleep} hours.")
    sleep(time_sleep*3600)


# ! Change  to your meeting start time format must be same.
now = datetime.now()
startTime = f'{now.year} {now.month} {now.day} 09 11 00'

#! Chnage it to meeting end time format must be same.
endTime = f'{now.year} {now.month} {now.day} 10 00 00'

#! Dont change it
day_name = now.strftime("%A")


#! If your saturday timing is different or same  then change it here format must be same.
saturday_startTime = f'{now.year} {now.month} {now.day} 07 31 00'

#! Dont change it is just a precaution for heroku deployment.
extended_pause = f'{now.year} {now.month} {now.day} 23 59 59'

#!#######################################


#! USER DETAILS ##########################

#! class CODE
meetingcode = 'abc-defg-hij'  # ! Replace with your meeting code
#? How to get meeting code ?
#? https://meet.google.com/abc-defg-hij
#? abc-defg-hij will be your meeting code

#! Chat message
full_name_with_roll = "CSE/18/27" #! Repalce With Your name and roll or anything you want
#? This message will be sent to chat.


#! Checking meet code is valid or not
if re.match("(^[a-z]{3}-)([a-z]{4}-)([a-z]{3}$)",meetingcode):
    pass
else:
    print("Meet Code Not Valid")
    sys.exit()
#! #######################################




def browser():
    #! Dont change anything
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--mute-audio")
    chromeOptions.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                    "profile.default_content_setting_values.media_stream_camera": 2,
                                                    "profile.default_content_setting_values.geolocation": 2,
                                                    "profile.default_content_setting_values.notifications": 2
                                                    })

    driver = webdriver.Chrome(chrome_options=chromeOptions)
    return driver


def login():
    driver.get('https://meet.google.com/')
    sleep(5)
    try:
        cookies = pickle.load(open("lnme.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        sleep(5)
    except:
        print("\nError !!!!\nFirst run get_cookies.py")
        driver.quit()
        sys.exit()


def meet_redirect():
    driver.get(f'https://meet.google.com/{meetingcode}')
    sleep(5)

    try:

        if(check_exists_by_xpath("//*[@id=\"yDmH0d\"]/div[3]/div/div[2]/div[3]/div/span/span")) == True:

            #! DISMISS BUTTON
            dismiss = wait.until(when.element_to_be_clickable(
                (by.XPATH, "//*[@id=\"yDmH0d\"]/div[3]/div/div[2]/div[3]/div/span/span")))
            dismiss.click()
            sleep(2)
    except:
        pass

    try:
        # ! mic option closed
        if(check_exists_by_css("[aria-label='Close']") == True):

            close_mic_option = wait.until(when.element_to_be_clickable(
                (by.CSS_SELECTOR, "[aria-label='Close']")))
            close_mic_option.click()
            sleep(2)
    except NoSuchElementException:
        pass

    # ! TURNED OFF VIDEO OPTION JUST TO BE SURE
    if(check_exists_by_css("[aria-label='Turn off camera (CTRL + E)']") == True):

        video_hide_btn = wait.until(when.element_to_be_clickable(
            (by.CSS_SELECTOR, "[aria-label='Turn off camera (CTRL + E)']")))
        video_hide_btn.click()
        sleep(1)
    else:
        pass

    try:
        driver.find_element_by_xpath(
            "//span[contains(text(),'Ask to join')]").click()
        sleep(180)  # !change it to 3-5 minutes e.g 300-360 sec
    except NoSuchElementException:
        if(check_exists_by_xpath("//span[contains(text(),'Join now')]") == True):
            driver.find_element_by_xpath(
                "//span[contains(text(),'Join now')]").click()
            sleep(180)  # !change it to 3-5 minutes e.g 300-360 sec
    try:
        if(check_exists_by_xpath("//span[contains(text(),'Join now')]") == True):
            # print("available")
            driver.find_elements_by_xpath(
                "/html/body/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/span/span")[0].click()
            sleep(5)

    except NoSuchElementException:
        pass


def end_meet():
    click_on_body = wait.until(
        when.element_to_be_clickable((by.CSS_SELECTOR, 'body')))  # ! It will click on a body tag i.e Home to make sure end call btn is available to be clicked

    click_on_body.click()
    sleep(1)
    end_call_btn = wait.until(when.element_to_be_clickable(
        (by.CSS_SELECTOR, "[aria-label='Leave call']")))  # ! It will End the call
    end_call_btn.click()


def send_roll():

    select_chat_btn = wait.until(when.element_to_be_clickable(
        (by.CSS_SELECTOR, "[aria-label='Chat with everyone']")))
    select_chat_btn.click()
    sleep(10)  # ! It will wait for 10 sec after clicking chat button


def send_roll_direct():

    try:
        driver.find_elements_by_css_selector(
            "[aria-label='Send a message to everyone']")[0].send_keys(full_name_with_roll, Keys.ENTER) #! It will send message to chat
    except:
        pass


def check_exists_by_css(css_Selector):
    try:
        driver.find_element_by_css_selector(css_Selector)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


if __name__ == "__main__":
    if(day_name != 'Saturday' and day_name != 'Sunday'):
        driver = browser()
        wait = webdriver.support.ui.WebDriverWait(driver, 5)
        driver.execute_script("document.body.style.zoom='50%'")
        startTime = list(map(int, startTime.split()))
        endTime = list(map(int, endTime.split()))
        extended_pause = list(map(int, extended_pause.split()))
        print(
            f"Waiting until Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...")
        pause.until(datetime(*startTime))
        login() #! it will login to google meet.
        try:
            meet_redirect() #! it will redirect to google meet site.
            while(check_exists_by_css("[aria-label='Chat with everyone']") != True):
                meet_redirect()
            send_roll() #! it will click on chat btn
            print("You Have Joined class at " + datetime.now().time().strftime("%H:%M:%S"))
            driver.execute_script("document.body.style.zoom='80%'")
            for i in range(1000):
                if(datetime.now().strftime("%H:%M:%S") < '09:55:00'): #! Dont change it if we are same (u know what i mean) otherwise you can change it accordingly
                    send_roll_direct() #! it will send message to chat.
                    sleep(180)
                else:
                    break
            print(
                f"Waiting until meet End time [{endTime[-3]:02}:{endTime[-2]:02}:{endTime[-1]:02}]...")
            driver.execute_script("document.body.style.zoom='0%'")
            sleep(5)
            # ! Dont change it if we are same (u know what i mean) otherwise you can change it accordingly
            if(datetime.now().strftime("%H:%M:%S") >= '10:01:00'):
                # print("Exiting")
                try:
                    end_meet() #! it will end meet
                    sleep(5)
                    driver.close()
                    driver.quit()
                except:
                    driver.quit()
                    #sys.exit()
            else:
                pause.until(datetime(*endTime))
            try:
                end_meet()
                driver.close()
                driver.quit()
            except:
                driver.close()
                driver.quit()
        except:
            end_meet()
            sleep(2)
            driver.close()
            driver.quit()
        print(
            f"Extended Till [{extended_pause[-3]:02}:{extended_pause[-2]:02}:{extended_pause[-1]:02}]...")
        pause.until(pause.until(datetime(*extended_pause))) #! Its just a precaution for heroku dont change it (only change if you know what are you doing)

    #! Saturday case
    #! Same as if block only thing is cahnged is startTime
    elif(day_name == 'Saturday'):
        driver = browser()
        wait = webdriver.support.ui.WebDriverWait(driver, 5)
        driver.execute_script("document.body.style.zoom='50%'")
        saturday_startTime = list(map(int, saturday_startTime.split()))
        endTime = list(map(int, endTime.split()))
        extended_pause = list(map(int, extended_pause.split()))
        print(
            f"Waiting until Meet start time [{saturday_startTime[-3]:02}:{saturday_startTime[-2]:02}:{saturday_startTime[-1]:02}]...")
        pause.until(datetime(*saturday_startTime))
        login()
        try:
            meet_redirect()
            while(check_exists_by_css("[aria-label='Chat with everyone']") != True):
                meet_redirect()
            send_roll()
            print("You Have Joined class at " + datetime.now().time().strftime("%H:%M:%S"))
            driver.execute_script("document.body.style.zoom='80%'")
            for _ in range(100):
                if(datetime.now().strftime("%H:%M:%S") < '09:55:00'):
                    send_roll_direct()
                    sleep(180)
                else:
                    break
            print(
                f"Waiting until meet End time [{endTime[-3]:02}:{endTime[-2]:02}:{endTime[-1]:02}]...")
            driver.execute_script("document.body.style.zoom='0%'")
            if(datetime.now().strftime("%H:%M:%S") >= '10:01:00'):
                # print("Exiting......")
                try:
                    end_meet()
                    sleep(5)
                    driver.close()
                    driver.quit()
                except:
                    driver.quit()
                    #sys.exit()
            else:
                pause.until(datetime(*endTime))
            try:
                end_meet()
                driver.close()
                driver.quit()
            except:
                driver.close()
                driver.quit()
        except:
            end_meet()
            sleep(2)
            driver.close()
            driver.quit()
        print(
            f"Extended Till [{extended_pause[-3]:02}:{extended_pause[-2]:02}:{extended_pause[-1]:02}]...")
        pause.until(pause.until(datetime(*extended_pause)))
    else:
        print('I wont Run Today :)')

        extended_pause = list(map(int, extended_pause.split()))
        print(
            f"Extended Till [{extended_pause[-3]:02}:{extended_pause[-2]:02}:{extended_pause[-1]:02}]...")
        pause.until(pause.until(datetime(*extended_pause)))
