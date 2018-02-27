import notify2

notify2.init('Animus')

class Notify:
    def __init__(self):
        pass

    def notify(self, msg):
        print('test')
        notification = notify2.Notification('Animus', message=msg, icon='')
        notification.show()