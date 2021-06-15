import smtplib
from email.message import EmailMessage

with open("textfile.txt") as fp:
    msg=EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = f'The contents of {"textfile.txt"}'
msg['From']='anthony.mota5@yahoo.com'
msg['To']='anthony.mota5@yahoo.com'
print(msg)
s=smtplib.SMTP('smtp.mail.yahoo.com',587)
s.starttls()
s.login('anthony.mota5','avhelxpbtdsfkfem')
s.sendmail('anthony.mota5@yahoo.com',"anthony.mota5@yahoo.com",str(msg))
s.quit()