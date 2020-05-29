prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(5000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01556)
    prg.add(5100, "Evaporation amp", 1000)
    prg.add(15100, "Evaporation amp", 1)
    return prg
