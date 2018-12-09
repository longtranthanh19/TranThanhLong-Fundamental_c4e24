from gmail import GMail,Message
from datetime import datetime

#1,Set Time 
now = datetime.now()
print(now.strftime('%Y/%m/%d %H:%M:%S %p'))        # At The Moment : 2018/12/09 22:12:43
deadline = '2018/12/10 07:00 AM'
format = '%Y/%m/%d %H:%M %p'
my_date = datetime.strptime(deadline, format)
print (my_date.strftime(format))

# 2,Send Mail
html_contents = ''' <p>Hi Sếp.</p>
<p>H&ocirc;m nay em nghỉ v&igrave; đơn giản em mệt.</p>
<p>Ch&agrave;o sếp</p> '''

gmail = GMail('longdzaivcl@gmail.com','longpro13')
msg = Message('Đơn xin nghỉ ốm', to = 'longtranthanh6@gmail.com' ,html = html_contents)

if now == my_date.strftime(format):
    gmail.send(msg)
else:
    print("It's too soon to send")