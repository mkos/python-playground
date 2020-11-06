import attr

@attr.s(auto_attribs=True)
class Resistor():
    volts: float = 0.0
    amps: float = 0.0
    ohms: float = 0.0


class VoltageResistor(Resistor):

    _volts = 0.0

    @property
    def volts(self):
        return self._volts

    @volts.setter
    def volts(self, volts):
        if volts < 0.0:
            raise ValueError(f'Voltage has to be greater than 0. Got {volts}')

        self._volts = volts
