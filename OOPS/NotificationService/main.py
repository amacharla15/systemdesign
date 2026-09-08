class EmailNotification:
# state:
    sender_email_address : str 
    receiver_email_address : str

    def __init__(self, sender_email_address, receiver_email_address):
        self.sender_email_address=sender_email_address
        self.receiver_email_address=receiver_email_address
# methods:
    def send(self, message):
        print("successfully sent email to: "+ self.receiver_email_address +"with this " + message)

class SMSNotification:
#state:
    receiver_mobile_number : str
    sender_mobile_number : str
    def __init__(self,sender_mobile_number,receiver_mobile_number):
        self.sender_mobile_number=sender_mobile_number
        self.receiver_mobile_number=receiver_mobile_number
#methods:
    def send(self, message):
        print("successfully sent SMS to: "+ self.receiver_mobile_number +"with this " + message)

class PushNotification:
# state:
    receiver_device_id : str
    sender_device_id : str
    def __init__(self,sender_device_id,receiver_device_id):
        self.sender_device_id=sender_device_id
        self.receiver_device_id=receiver_device_id
# methods:
    def send(self, message):
        print("successfully sent PUSH notification to: "+ self.receiver_device_id +"with this " + message)

class NotificationService:
#state:
    def __init__(self,obj):
        self.obj=obj
#methods:
    def send(self,message):
        return self.obj.send(message)


if __name__ == "__main__":
    obj1=EmailNotification("aks@gmail.com","tinku@gmail.com")
    obj2=SMSNotification("8247679048","5309657864")
    obj3=PushNotification("1234","5678")

    notify1=NotificationService(obj1)
    notify2=NotificationService(obj2)
    notify3=NotificationService(obj3)

    notify1.send("ur email service is good")
    notify2.send("ur SMS service is good")
    notify3.send("ur PUSH service is good")
        
