prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(6000000, "Picture FastStingray")
    prg.add(6000000, "Picture NaK.sub", enable=False)
    prg.add(6000020, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    return prg
