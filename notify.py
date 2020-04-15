import requests
from time import sleep
from selenium import webdriver
import os 
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def text_alerts(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=os.getenv("MY_PHONE"), from_=os.getenv("TWILIO_PHONE"), body=message
    )
    return message.sid

if __name__ == "__main__":
    browser_profile = webdriver.ChromeOptions()
    browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    browser = webdriver.Chrome(options=browser_profile, executable_path=os.getenv('CHROMEDRIVER_PATH'))
    sleep(25)    

    try:
        while True: 
            browser.get(r"https://primenow.amazon.com/storefront?merchantId=A1BV2214E4H2PJ&ref_=pn_gw_nav_sbs_1_A1BV2214E4H2PJ")
            sleep(300)
            banner = browser.find_element_by_xpath(
                "/html/body/div[1]/div/header/div[1]/div[1]/div[3]/div/div[1]/div[2]")
            print(banner.text)
            if "sold out" in banner.text:
                continue
            else:
                text_alerts(message="Prime Now delivery slot available!")
                sleep(60)
    except Exception as e:
        print("Exception raised! ", e)
        text_alerts(message="An error occurred in the PrimeNow Notifier.")