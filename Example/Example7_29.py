import string
import smtplib

Host = "smtp.163.com"

Subject = "This is a test email"
From = "heping_tsdwx@163.com"
To = "476702292@qq.com"
Body = "This is a simple email from heping!"

account = From
password = ""

body = string.join(["From: %s" %From, "To: %s" %To, "Subject: %s" %Subject, "", Body], "\r\n")
smtp_client =  smtplib.SMTP(Host)
smtp_client.starttls()
smtp_client.login(account,password)
smtp_client.sendmail(From,To,body)
smtp_client.quit()

