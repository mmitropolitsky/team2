from Tkinter import StringVar

import Tkinter


class AlarmAction(object):
    # top = None
    # level = None
    # label = None

    # def __init__(self):
        # self.top = Tkinter.Tk()
        # self.top.title = 'Title'
        # self.top.geometry = ('200x180')
        #
        # self.label = Tkinter.Button(master=self.top, text='0')
        # self.label.place(x=5, y=5, width=60, height=30)
        # self.label.pack()
        # self.top.mainloop()

    def do_action(self, alarm):
        # self.level.set('' + alarm.alarm_level)

        print 'ALARM LEVEL:' + str(alarm.alarm_level)
