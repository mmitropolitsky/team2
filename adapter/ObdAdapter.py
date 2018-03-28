import obd
import time

class ObdAdapter:

    ODB_PARAMS = ['SPEED', 'RPM', 'THROTTLE_POS', 'MAF']

    def __init__(self):
        self.__reader = obd.OBD('/dev/ttys024')
        #self.__reader = obd.Async('/dev/ttys010')
        #for param in self.ODB_PARAMS:
        #    self.__reader.watch(obd.commands[param])
        #self.__reader.start()



    def get_log_entry_and_slopes(self, last_entry=None):
        log_entry = {
            'timestamp': time.time()
        }
        slope = dict()
        for param in self.ODB_PARAMS:
            param_qty = self.__reader.query(obd.commands[param]).value
            value = param_qty.to_tuple()[0]
            param_key = param.lower()
            log_entry[param_key] = value
            if not last_entry or last_entry[param_key] <= value:
                suffix = "_increasing"
            else:
                suffix = "_decreasing"

            slope[param_key+suffix] = {
                'timestamp': log_entry['timestamp'],
                'value': value
            }
        return log_entry, slope

    def __getattr__(self, name):
        name_fixed = name.upper()
        if name_fixed in self.ODB_PARAMS:
            param_qty = self.__reader.query(obd.commands[name_fixed]).value
            return param_qty.to_tuple()[0]


