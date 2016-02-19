prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1000, "RFO Sweep Trig ON")
    prg.add(0, "Bottom Evaporation ON")
    prg.add(10000, "RFO Sweep Trig OFF")
    prg.add(19000, "Bottom Evaporation OFF")
    return prg
