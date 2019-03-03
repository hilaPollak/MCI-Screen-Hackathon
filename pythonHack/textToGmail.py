import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

##write the email of the user and the send
email_user='testSendingemail41@gmail.com'
email_send='rotemavg@gmail.com'


msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
##write the subject of the mail
msg['subject']='injured details'

body='injured details'
#plain defines the kind of the text-html,text etc
msg.attach(MIMEText(body,'plain'))



filename='Document.txt'
attachment=open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'TestOfHack6')

server.sendmail(email_user,email_send,text)
server.quit()
