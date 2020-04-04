import requests
from time import sleep
from selenium import webdriver

_API_KEY_ = ""
_PHONE_NUM = ""

if __name__ == "__main__":
    browser_profile = webdriver.ChromeOptions()
    browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    browser = webdriver.Chrome(options=browser_profile)
    sleep(25)    

    try:
        while True: 
            browser.get(r"https://primenow.amazon.com/storefront?merchantId=A1BV2214E4H2PJ&ref_=pn_gw_nav_sbs_1_A1BV2214E4H2PJ")
            sleep(3)
            banner = browser.find_element_by_xpath(
                "/html/body/div[1]/div/header/div[1]/div[1]/div[3]/div/div[1]/div[2]")
            if "sold out" in banner.text:
                continue
            else:
                resp = requests.post('https://textbelt.com/text', {
                    'phone': _PHONE_NUM,
                    'message': 'Slots available!',
                    'key': _API_KEY_,
                    })
                print(resp.json())
                sleep(60)
                
    except:
        print("Exception raised! ")
        resp = requests.post('https://textbelt.com/text', {
            'phone': _PHONE_NUM,
            'message': 'Exception raised!',
            'key': _API_KEY_,
            })
        print(resp.json())