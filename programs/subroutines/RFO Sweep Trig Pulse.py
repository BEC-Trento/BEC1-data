prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO Sweep Trig ON")
    prg.add(50000, "RFO Sweep Trig OFF")
    return prg
