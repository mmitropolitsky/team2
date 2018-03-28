from alarm.AlarmActionFactory import AlarmActionFactory


class Alarm(object):

    __alarm_counter = 0
    __alarm_action_factory = AlarmActionFactory()

    def ring(self):
        self.__alarm_counter += 1
        alarm_action = self.__alarm_action_factory.get_alarm_aciton(self.__alarm_counter)
        if alarm_action:
            alarm_action.do_action()

    def reset_alarm(self):
        self.__alarm_counter = 0
