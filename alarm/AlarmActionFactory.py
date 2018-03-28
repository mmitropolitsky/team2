from alarm.SoundAlarmAction import SoundAlarmAction


class AlarmActionFactory(object):

    def get_alarm_aciton(self, level):
        alarm_aciton = None
        if level == 1:
            alarm_aciton = SoundAlarmAction()

        # else
        return alarm_aciton
