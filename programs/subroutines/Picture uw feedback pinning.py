prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-6000000, "Picture SetImaging")
    prg.add(-5100000, "Na Probe/Push (+) freq", 110.00)
    prg.add(-5000000, "Na Probe/Push (-) freq", 110.00)
    prg.add(-500, "Pulse uw ON")
    prg.add(-480, "Pulse uw OFF")
    prg.add(0, "Picture Quantum - 1 shot Trig1")
    prg.add(1000000, "Picture Quantum - 1 shot Trig1")
    return prg
