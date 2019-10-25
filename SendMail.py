#coding=utf-8

import os
import smtplib
from JiraReport.ReadConfig import readconfig
from JiraReport.GetVersion import get_version
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from JiraReport.LogAndExcept import logger

class SendMali(object):

    def __init__(self):
        self.msg_from = readconfig("MAIL", "MSG_FROM")
        self.passwd = readconfig("MAIL", "PASSWD")
        self.msg_to = readconfig("MAIL", "MSG_TO")

    #img_name type:tuple
    def get_img_path(self,img_names):
        nowpath = os.path.dirname(os.path.abspath(__file__))
        try:
            path = os.path.join(nowpath, "picture/%s.png"%img_names)
            with open(path, "rb") as of:
                img_data = of.read()
            return img_data
        except:
            logger().error("文件不存在！")

    #编辑邮件内容添加图片
    def mail_content(self,mail_title="测试报告",total="0", mail_img_name1="Bug类型",mail_img_name2="经办人",mail_img_name3="模块类型"):
        subject = mail_title
        msg = MIMEMultipart('related')
        iso_version,android_version = get_version()


        jv = "APP_" + readconfig().split("_")[0]
        content = MIMEText('<html lang="utf-8">'
                           '<head>'
                           '<meta http-equiv="Content-Type" content="text/html; charset=gb2312">'
                           '<title>%s</title>'
                           '</head>'
                           '<body><b>Dear all:</b><br>'
                           '<br>&emsp;&emsp;%s版本测试结束，如下情况<br>'
                           '<br>测试结果:<font  color="green">&emsp;测试通过</font><br>'
                           '<br>bug情况 合计提交 <font  color="red">%s个bug</font>,分布情况请查看饼图（包含模块分类、bug类型、经办人）<br>'
                           '<br>IOS:%s&emsp;Android:%s<br>'
                           '<img src="cid:mail_img_name1" alt="imageid">'
                           '<img src="cid:mail_img_name2" alt="imageid">'
                           '<img src="cid:mail_img_name3" alt="imageid">'
                           '</body></html>'%(mail_title,jv,total,iso_version,android_version), 'html', 'utf-8')  #



        msg.attach(content)

        msg['Subject'] = subject
        msg['From'] = self.msg_from
        msg['To'] = self.msg_to


        img_data1 = self.get_img_path(mail_img_name1)
        img_data2 = self.get_img_path(mail_img_name2)
        img_data3 = self.get_img_path(mail_img_name3)

        img1 = MIMEImage(img_data1)
        img1.add_header('Content-ID', 'mail_img_name1')
        msg.attach(img1)

        img2 = MIMEImage(img_data2)
        img2.add_header('Content-ID', 'mail_img_name2')
        msg.attach(img2)

        img3 = MIMEImage(img_data3)
        img3.add_header('Content-ID', 'mail_img_name3')
        msg.attach(img3)

        return msg


    def main(self,total):
        s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 邮件服务器及端口号
        s.login(self.msg_from, self.passwd)
        s.sendmail(self.msg_from, self.msg_to, self.mail_content(total=total).as_string())





