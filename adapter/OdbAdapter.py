import obd

class OdbAdapter:

    ODB_PARAMS = ['SPEED', 'RPM', 'THROTTLE_POS', 'MAF']

    def __init__(self):
        self.__reader = obd.OBD('/dev/ttys010')

    def __getattr__(self, name):
        name_fixed = name.upper()
        if name_fixed in self.ODB_PARAMS:
            param_qty = self.__reader.query(obd.commands[name_fixed]).value
            return param_qty.to_tuple()[0]


