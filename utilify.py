import requests
import smtplib
import sys

from bs4 import BeautifulSoup
from lxml import html

# This function authenticates with the gmail server
# And then sends the email with the utility updates
def send_email(sender, recipient, password, subject, text):
    smtp_server = smtplib.SMTP_SSL("smtp-mail.outlook.com", 587)
    smtp_server.login(sender, password)
    body = "Subject: {}\n\n{}".format(subject, text)
    smtp_server.sendmail(sender, recipient, body)
    smtp_server.close()


# Scrapes the dominion energy website for the necessary utility information
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

login_data = {
    "smauthreason": "0",
    "target": "https://mydom.dominionenergy.com",
    "user": sys.argv[1],
    "password": sys.argv[2],
}

with requests.Session() as s:
    url = "https://mydom.dominionenergy.com/siteminderagent/forms/login.fcc"
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html5lib")

    r = s.post(url, data=login_data, headers=headers)

    tree = html.fromstring(r.content)
    totalAmountDue = tree.xpath('//span[@class="bodyTextGreen"]/text()')

    message = "Dominion Energy:\nAs of{}, the total amount due is {}".format(
        totalAmountDue[0], totalAmountDue[1]
    )

    sender = sys.argv[3]
    recipient = sys.argv[4]
    password = sys.argv[5]
    subject = "{} Utility Update".format(totalAmountDue[0])
    text = message

    send_email(sender, recipient, password, subject, text)
