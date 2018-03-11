import smtplib

import config

class Mail:
    @staticmethod
    def send_email(subject, msg):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
            server.quit()
            print("Success: Email sent!")
        except Exception as e:
            print(e)
            print("Email failed to send.")