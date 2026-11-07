class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending email notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification")


obj1 = Notification()
obj2 = EmailNotification()
obj3 = SMSNotification()

obj1.send()
obj2.send()
obj3.send()