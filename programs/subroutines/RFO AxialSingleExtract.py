prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-6000, "RFO FM amp", 0.5000)
    prg.add(-5000, "RFO Sweep Trig ON")
    prg.add(0, "Bottom Evaporation ON")
    prg.add(10000, "RFO Sweep Trig OFF")
    prg.add(14000, "Bottom Evaporation OFF")
    prg.add(15000, "RFO FM amp", 0.0000)
    return prg
