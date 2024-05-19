#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

# Set SMTP server
SMTPHOST = "localhost"
SMTPPORT = 25

# Create mail
SENDER = "Sender Name <sender@example.com>"
RECIPIENT = "recipient@example.org"

# The subject line for the email.
SUBJECT = "SMTP Test for BCC Header"

# The email body
BODY_TEXT = "Hello"

msg = MIMEText(BODY_TEXT)
msg['Subject'] = SUBJECT 
msg['From'] = SENDER 
msg['Bcc'] = RECIPIENT

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
