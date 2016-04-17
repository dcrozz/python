#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image,ImageDraw,ImageFont
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
def createPic(sentence,color):
	x,y = 240,240
	word = len(sentence)/3
	img = Image.new('RGBA',(x,y),color='white')
	height = x//word
	myfont = ImageFont.truetype('华文黑体.ttf',height)
	ImageDraw.Draw(img).text((0,(x-height)//2),unicode(sentence,'UTF-8'),font=myfont,fill=color)
	img.save('testout.jpg','jpeg')
#line = raw_input('how many lines is this sentence?\n')
sentence = raw_input('the sentence:\n')
color = raw_input('the color:\n')
createPic(sentence,color)

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

host = 'smtp.126.com'
port = 25
mail_user = 'ukeyim@126.com'
mail_pw = raw_input('input the password:\n')


from_addr = 'ukeyim@126.com'
to_addrs = 'ukeyim@126.com'
msg = 'python mail test'

message = MIMEMultipart()
message['From'] = Header('Alex ukeyim','utf-8')
message['To'] = Header('Test','utf-8')
subject = 'Wechat Custom Sticks'
message['Subject'] = Header(subject,'utf-8')
fp = open('testout.jpg','rb')
img = MIMEImage(fp.read())
fp.close()
message.attach(img)
try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(host,port)
	smtpObj.login(mail_user,mail_pw)
	smtpObj.sendmail(from_addr,to_addrs,message.as_string())
	print 'Send Success'
except:
	print "Error"
