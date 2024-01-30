import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("my_email", "my_pwd")
msg = "please subscribe to my channel"
reciever_mail = "kvinaykumarreddy1995@gmail.com"
s.send_mail("my_email", reciever_mail, msg)
s.quit()
print("successsfully sent")
