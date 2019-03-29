prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "RFO", 201)
    prg.add(20000, "RFO1 Amp", 1000)
    return prg
