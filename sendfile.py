import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

server = smtplib.SMTP('smtp.gmail.com', 587) # SMTP server
server.ehlo()
server.starttls()
server.login('YOUR USERNAME', 'YOUR PASSWORD')

msg = MIMEMultipart('alternative')
toEmail = ""
fromEmail = ""
body = "Sending file from *nix terminal"
filename = sys.argv[1]
f = file(filename)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)

content = MIMEText(body, 'plain')
msg.attach(content)
msg.attach(attachment)

server.sendmail(fromEmail, toEmail, msg.as_string())

