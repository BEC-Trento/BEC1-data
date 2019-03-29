prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-6000000, "Na Gray molasses (+) Amp", 1)
    prg.add(-5850000, "Na Gray molasses (-) Amp", 1)
    prg.add(-5750000, "Na Gray molasses (-) freq", 90.00)
    prg.add(-5730000, "Na Gray molasses (+) freq", 110.00)
    prg.add(-5650000, "Shutter Phase Imprint Open")
    prg.add(-4000000, "TTL3-11 OFF")
    prg.add(-1200, "Na Gray molasses (+) Amp", 1000)
    prg.add(-600, "Na Gray molasses (-) Amp", 1000)
    prg.add(0, "TTL3-11 ON")
    prg.add(10, "Bragg burst ON")
    prg.add(57, "TTL3-11 OFF")
    prg.add(18077, "Bragg burst OFF")
    prg.add(18207, "Na Gray molasses (+) Amp", 1)
    prg.add(19007, "Na Gray molasses (-) Amp", 1)
    prg.add(26407, "Shutter Phase Imprint Close")
    prg.add(4896207, "Na Gray molasses (-) Amp", 1000)
    prg.add(4906207, "Na Gray molasses (+) Amp", 1000)
    prg.add(4916407, "Na Gray molasses (-) freq", 90.00)
    prg.add(4926207, "Na Gray molasses (+) freq", 110.00)
    prg.add(5017217, "TTL3-11 ON")
    return prg
