import random


def genereation_verification_code():
    return random.randint(100000, 999999)


from eskiz_sms import EskizSMS

eskiz = EskizSMS(email='example@gmail.com', password='9201iwsjd823e88e9wq902')


# eskiz.send_sms(mobile_phone='998908632230', message=genereation_verification_code, from_whom='4546', callback_url=None)
def send_sms(message, recipient):
    eskiz.send_sms(mobile_phone=recipient, message=message, from_whom='4546', callback_url=None)
