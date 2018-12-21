prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(12210080, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(12210110, "Picture FastStingray")
    prg.add(12210110, "Picture close.sub", enable=False)
    prg.add(12210110, "Picture NaK - new Stingray", enable=False)
    prg.add(30806630, "All AOM On.sub")
    return prg
