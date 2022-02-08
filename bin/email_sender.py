import smtplib
import json
import keyring
from datetime import date
from email.message import EmailMessage

def send_emails(posts):

    # get login and service from cfg
    # then get pass from keyring
    with open('config.json', 'r') as f:
        config = json.load(f)

    service = config["MAIL"]["service"]
    login = config["MAIL"]["login"]
    password = keyring.get_password(service, login)

    # format mail body
    mail_body = ""
    curr_date = date.today()
    for i in posts:
        mail_body += i['date'] + "\n" + i['thread'] + "\n" + i['link'] + "\n\n"

    # init EmailMessage
    msg = EmailMessage()

    msg.set_content(
        f"There are {len(posts)} threads with new posts! \n They are as follows:\n {mail_body}"
    )
    
    msg['From'] = login
    msg['To'] = config['MAIL']['recipients']
    msg['Subject'] = f'Scraper\'s new mail - {curr_date}'

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(login, password)
        smtp_server.send_message(msg)
        smtp_server.close()
    except Exception as e:
        print(e)
