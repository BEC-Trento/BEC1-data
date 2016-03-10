prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO", 0)
    prg.add(1000, "RFO1 Amp", 1000)
    prg.add(2000, "TTL RF ON")
    prg.add(252000, "TTL RF OFF")
    prg.add(253000, "RFO1 Amp", 1)
    prg.add(254000, "RFO2 Amp", 1)
    return prg
