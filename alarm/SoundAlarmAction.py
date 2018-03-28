from alarm.AlarmAction import AlarmAction


class SoundAlarmAction(AlarmAction):
    def do_action(self):
        print 'ALARMA'