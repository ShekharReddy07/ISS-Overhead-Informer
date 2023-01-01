import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 22.260424
MY_LONG = 84.853584


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_sunset():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now.hour >= sunset:
        return True


time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark

while True:
    time.sleep(60)
    if is_overhead():
        if is_sunset():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="shekharreddy1888@gmial.com", password="bftdkdkqpwbmfdpm")
                connection.sendmail(from_addr="shekharreddy1888@gmial.com",
                                    to_addrs="2105452@kiit.ac.in",
                                    msg="Subject:ISS aane wala hai\n\nYeh ISS upar hi hai dekh le")

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



