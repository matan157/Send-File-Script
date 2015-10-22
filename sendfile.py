import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('minionsrule2k15@gmail.com', 'abc123!.')

msg = MIMEMultipart('alternative')
toEmail = "matan.uchen@gmail.com"
fromEmail = "minionsrule2k15@gmail.com"
body = "Sending file from *nix terminal"
filename = sys.argv[1]
f = file(filename)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)

content = MIMEText(body, 'plain')
msg.attach(content)
msg.attach(attachment)

server.sendmail(fromEmail, toEmail, msg.as_string())

