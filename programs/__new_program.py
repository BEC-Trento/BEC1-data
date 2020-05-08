prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000)
    prg.add(100010, "Pulse uw ON")
    prg.add(100040, "Pulse uw OFF")
    return prg
