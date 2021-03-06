import os
import re
from util.Notify import Notify
from subprocess import call
import time

class System:
    notify = Notify()

    @staticmethod
    def launchapp(appname):
        
        appname = appname.replace(" ","")

        if appname in "chrome":
            os.system("/usr/bin/google-chrome")
        
        elif appname in "firefox":
            os.system("/usr/bin/firefox")

        else:
            path = os.popen('whereis ' + appname ).read()
            print(appname)
            path = re.split(' ', path)

            print(path)
            if len(path) == 1:
                print('Did not find any app named {}'.format(appname))
            else:
                os.system(path[1])
    @staticmethod
    def change_brightness(value):
        if value>0 and value<=100:
            os.system('xbacklight -set ' + str(value))
            System.notify.notify('Brightness set to '+ str(value))
        else:
            System.notify.notify('Brightness cannot be set to '+ str(value))

    @staticmethod
    def set_sound(value):
        if (value <= 100) and (value >= 0):
            call(["amixer", "-D", "pulse", "sset", "Master", str(value)+"%"])
            System.notify.notify('Volume set to '+ str(value))
        else:
            System.notify.notify('Volume cannot be set to '+ str(value))
    
    @staticmethod
    def shutdown():
        System.notify.notify('Shutting down in 6 seconds')
        time.sleep(6)
        os.system("shutdown -h")
    
    @staticmethod
    def restart():
        System.notify.notify('Restarting in 6 seconds')
        time.sleep(6)
        os.system("reboot")
