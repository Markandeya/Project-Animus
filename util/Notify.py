import notify2

class Notify:
    def __init__(self):
        notify2.init('Animus')

    def notify(self, msg, ico="notification-message-im"):
        notification = notify2.Notification('Animus', message=msg, icon=ico)
        notification.show()