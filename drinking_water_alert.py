import time
from plyer import notification

if __name__ == '__main__':
    while(True):
        notification.notify(
            title = "Hey Bro Drink Water",
            message = "It is really very Good for Health",
            app_icon = "D:\glassofwater.ico",
            timeout=5
        )
        time.sleep(60*60)