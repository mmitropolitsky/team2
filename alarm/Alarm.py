from alarm.AlarmAction import AlarmAction


class Alarm(object):

    alarm_level = 0
    __alarm_action = AlarmAction()


    def ring(self):
        self.alarm_level += 1
        if self.__alarm_action:
            self.__alarm_action.do_action(self)

    def reset_alarm(self):
        self.alarm_level = 0
