prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(30000000, "RFO FM amp", 5.0000)
    prg.add(30100000, "Pulse RFO Sweep Trig", polarity=1, pulse_t=0.10000)
    prg.add(30100500, "Pulse RFO Bottom Evap", polarity=1, pulse_t=1000.00000)
    return prg
