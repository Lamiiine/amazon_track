import requests
from bs4 import BeautifulSoup
import smtplib

# change to url of your product
URL = 'https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/ref=lp_16225007011_1_2'

header = {'authority': 'scrapeme.live',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',}

def price_checker():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser') 

    price = soup.find(id="priceblock_ourprice").get_text()
    current_price = float(price[1:4]) # converting the price into a float

    if current_price <  50 :
        send_email()
    print(current_price)
    print(price)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yourEmail@example', 'password') # change to your email & password

    subject = "You can buy now"
    body = "Hello Customer, your most wanted product on Amazon has gone below the threshold, you can buy now"
    msg = f"Subject: {subject}\n\n{body}"

    # set your email address 
    server.sendmail(
        'sender@example.com',
        'receiver@example.com',
        msg
    )
    print("email sent")

    server.quit()


price_checker()