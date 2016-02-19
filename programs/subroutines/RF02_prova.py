prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "RFO", 0)
    prg.add(20000, "RFO2 Amp", 1000)
    prg.add(30000, "RF02 ON")
    return prg
