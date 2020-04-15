# Prime-Now-Notifier
Text notifier for Amazon Prime Now delivery windows

Very small script utilizing Selenium to send notification via text/sms when Prime Now delivery windows open. 

Uses the [Twilio API](https://www.twilio.com/) to send text messages. 

Usage: 

(1) Download Chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH. 

    export PATH=$PATH:/path/to/driver/chrome-driver

(2) Clone this repository. 

    git clone https://github.com/bhavika/Prime-Now-Notifier.git

(3) Enter the directory. 

    cd Prime-Now-Notifier

(4) Create a virtual environment, using Python 3. 

    python -m venv venv

(5) Activate the virtual environment. 

    source venv/bin/activate

(6) Install this script using pip - 

    pip install .

(7) Create a .env file similar to `example.env`, add your Twilio keys and phone numbers. 

(8) Now, run the notify.py script. 

    python notify.py

This will open up a Chrome window and you will see the Amazon Prime Now storefront. Log in to your Amazon account there and leave the browser window open. 