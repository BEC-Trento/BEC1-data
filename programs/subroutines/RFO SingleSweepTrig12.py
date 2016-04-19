prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1500, "RFO FM amp", 1.0000, enable=False)
    prg.add(0, "RFO Sweep Trig ON")
    prg.add(1000, "Bottom Evaporation ON")
    prg.add(20000, "RFO Sweep Trig OFF")
    prg.add(21000, "RFO FM amp", 0.0000, enable=False)
    prg.add(39000, "Bottom Evaporation OFF")
    return prg
