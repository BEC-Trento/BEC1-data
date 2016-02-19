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
    prg.add(-100, "TTL3-12 ON")
    prg.add(0, "TTL3-11 ON")
    prg.add(40, "TTL3-11 OFF")
    prg.add(190, "TTL3-12 OFF")
    prg.add(220, "Na Gray molasses (+) Amp", 1)
    prg.add(1020, "Na Gray molasses (-) Amp", 1)
    prg.add(8420, "Shutter Phase Imprint Close")
    prg.add(4878220, "Na Gray molasses (-) Amp", 1000)
    prg.add(4888220, "Na Gray molasses (+) Amp", 1000)
    prg.add(4898420, "Na Gray molasses (-) freq", 90.00)
    prg.add(4908220, "Na Gray molasses (+) freq", 110.00)
    prg.add(4999230, "TTL3-11 ON")
    return prg
