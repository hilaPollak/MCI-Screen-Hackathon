# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:39:13 2018

@author: rotem
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message():
    msg = MIMEMultipart('alternative')
    s = smtplib.SMTP('smtp.sendgrid.net', 587)
    s.login(USERNAME, PASSWORD)

    toEmail, fromEmail = rotem@gmail.com, frrotemavgom@gmail.com
    msg['Subject'] = 'subject'
    msg['From'] = fromEmail
    body = 'This is the message'

    content = MIMEText(body, 'plain')
    msg.attach(content)
    s.sendmail(fromEmail, toEmail, msg.as_string())

