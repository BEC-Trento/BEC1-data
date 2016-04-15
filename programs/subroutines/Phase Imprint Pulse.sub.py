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
    prg.add(10000510, "TTL3-11 OFF")
    prg.add(10000530, "Bragg burst OFF")
    prg.add(10000660, "Na Gray molasses (+) Amp", 1)
    prg.add(10001460, "Na Gray molasses (-) Amp", 1)
    prg.add(10008860, "Shutter Phase Imprint Close")
    prg.add(14878660, "Na Gray molasses (-) Amp", 1000)
    prg.add(14888660, "Na Gray molasses (+) Amp", 1000)
    prg.add(14898860, "Na Gray molasses (-) freq", 90.00)
    prg.add(14908660, "Na Gray molasses (+) freq", 110.00)
    prg.add(14999670, "TTL3-11 ON")
    return prg
