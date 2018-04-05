prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "RFO Sweep Trig ON")
    prg.add(5000, "RFO Sweep Trig OFF")
    return prg
