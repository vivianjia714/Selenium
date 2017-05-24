#coding=utf-8
import smtplib
import os,datetime,time
from email.mime.text import MIMEText
from email.header import Header
import string

#邮件信息配置

def sentmail(result_dir):
    sender = 'luckystar1984@126.com'
    receiverlist = ['jiawenting@tuozhongedu.com','271626310@qq.com']
    receiver = ",".join(receiverlist)  
    subject = 'test report'
    smtpserver = 'smtp.126.com'
    username = 'luckystar1984@126.com'
    password = 'llzjlc521'
#定义正文
    f = open(result_dir, 'rb+')
    mail_body = f.read()
    f.close()

#HTML 形式的文件内容
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = 'luckystar1984@126.com'    
    msg['To'] = receiver 
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiverlist, msg.as_string())
    smtp.quit()
    print "mail sent!"
    
    
def report():
    result_dir = 'E:\\automation\\case_result\\case_report\\result.html'
    #lists=os.listdir(result_dir)
    sentmail(result_dir)

if __name__ == "__main__":
    report()
