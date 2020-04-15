# Prime-Now-Notifier
Text notifier for Amazon Prime Now delivery windows

Very small script utilizing Selenium to send notification via text/sms when Prime Now delivery windows open. 

Uses Twilio API to send text messages 

Usage: 

(1) Download Chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH. 

    ```export PATH=$PATH:/path/to/driver/chrome-driver```

(2) Clone this repository. 

(3) Enter the directory. 

    `cd Prime-Now-Notifier`

(4) Install this script using 

    `pip install .` 

(5) Create a .env file similar to `example.env`, add your Twilio keys and phone numbers. 

(6) 
