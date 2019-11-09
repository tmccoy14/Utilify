import requests
import smtplib
import credentials
from bs4 import BeautifulSoup
from lxml import html


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

login_data = {
    "smauthreason": "0",
    "target": "https://mydom.dominionenergy.com",
    "user": credentials.dominion_user,
    "password": credentials.password,
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

    sender = credentials.sender
    recipient = credentials.recipient
    password = credentials.password
    subject = "{} Utility Update".format(totalAmountDue[0])
    text = message

    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(sender, password)
    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_server.sendmail(sender, recipient, message)
    smtp_server.close()
