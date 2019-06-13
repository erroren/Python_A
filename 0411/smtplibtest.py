from smtplib import SMTP
from email.mime.text import MIMEText
smtp = SMTP(host='smtp.163.com', port=25)
# smtp.connect(port=465, source_address=)
useremail = "18137128152@163.com"
smtp.login(useremail, "qikuedu")
html = "<h1>标题1<h3>标题3</h3></h1>"
# sendtext = MIMEText("胡晨洋", "plain", "utf-8")
sendtext = MIMEText(html, "html", 'utf-8')
sendtext["from"] = useremail
sendtext["to"] = "982882262@qq.com"
sendtext["subject"] = "吴晨带附件的"


smtp.sendmail(useremail, "982882262@qq.com", sendtext.as_string())
smtp.quit()
