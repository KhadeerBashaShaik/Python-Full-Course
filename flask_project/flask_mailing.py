from flask import Flask
from flask_mail import Mail, Message
import csv

app=Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='rohanthking@gmail.com'
app.config['MAIL_PASSWORD']='mmxgjywpgvmpmevf'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/')
def index():
    for _ in range(3):
        with open('mail.csv','r') as f:
            reader=csv.reader(f)
            next(reader)
            for name,addr in reader:
                msg=Message(f"Hi ..\n{name} ",sender='rohanthking@gmail.com',recipients=[addr])
                msg.body = "This was sent by Flask App"
                mail.send(msg)
                print(f"SENT SUCCESS")
    return 'sent success'

if __name__=='__main__':
    app.run(debug = True)