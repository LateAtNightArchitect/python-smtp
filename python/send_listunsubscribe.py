#!/usr/bin/env python

import smtplib

from email.message import Message
from email.mime.text import MIMEText

# Set SMTP server
SMTPHOST = "localhost"
SMTPPORT = 25

# Create mail
SENDER = "Sender Name <sender@example.com>"
RECIPIENT = "recipient@example.org"

# The subject line for the email.
SUBJECT = "SMTP Test for Mailing List Unsubscribe Headers"

# List-Unsubscribe header(s)
UNSUBSCRIBE_URL= "<https://unsubscribe.example.com/?id=11111>"

# The email body
BODY_TEXT = "Hello"

msg = MIMEText(BODY_TEXT)
msg['Subject'] = SUBJECT 
msg['From'] = SENDER 
msg['To'] = RECIPIENT
msg['List-Unsubscribe'] = UNSUBSCRIBE_URL
msg['List-Unsubscribe-Post'] = "List-Unsubscribe=One-Click"

# Set SMTP connection 
session = smtplib.SMTP(
  host = SMTPHOST,
  port = SMTPPORT
)
session.set_debuglevel(1)

# Try to send the email.
session.sendmail(
    from_addr = SENDER,
    to_addrs = RECIPIENT,
    msg = msg.as_string()
    )

session.quit()
