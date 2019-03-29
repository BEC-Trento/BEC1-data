prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1500, "RFO FM amp", 1.0000)
    prg.add(0, "RFO Sweep Trig ON")
    prg.add(0, "Bottom Evaporation ON", enable=False)
    prg.add(19000, "Bottom Evaporation OFF", enable=False)
    prg.add(20000, "RFO Sweep Trig OFF")
    prg.add(21000, "RFO FM amp", 0.0000)
    prg.add(118500, "RFO FM amp", 1.0000)
    prg.add(120000, "RFO Sweep Trig 2 ON")
    prg.add(120000, "Bottom Evaporation ON", enable=False)
    prg.add(139000, "Bottom Evaporation OFF", enable=False)
    prg.add(140000, "RFO Sweep Trig 2 OFF")
    prg.add(141000, "RFO FM amp", 0.0000)
    return prg
