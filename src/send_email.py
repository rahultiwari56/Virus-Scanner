import os 
import sys
import smtplib
from email.message import EmailMessage

from config import config

# path = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(path,'../'))


class Scan_Report:

    '''
        This class contain two functions
        1. notify
            It generates content for the email

            Input:
                - file_key : It is the hash key generated for the scanned file
                - user_email : It is the user/recepient email 
            
            Output:
                - Once the email sent it will return success
        
        2. send_email
            This function will send the email to the given recepient's email

            Input:
                - msg : It takes email message as input
            
            Output:
                - Sends the email
    '''

    def __init__(self , email_address , password):
        self.email_address = email_address
        self.password = password

    def notify(self , file_key, user_email):
        msg = EmailMessage()
        msg['Subject'] = "File SCan Status"
        msg['From'] = self.email_address
        msg['to'] = user_email

        msg.set_content(config.content+file_key)
        self.send_email(msg)
        return 'success'


    def send_email(self ,msg):
        try:
            #this code is to send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  #smpt and port no. for gmail(465)
                smtp.login(self.email_address, self.password)         
                smtp.send_message(msg)                             
                print("Email Sent")

        except:
            print(f'{sys.exc_info()[0]} -- Error caused while sending email')
            


        
