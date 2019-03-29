prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5505000, "Na Gray molasses (-) freq", 90.000000)
    prg.add(-5500000, "Na Gray molasses (+) freq", 110.000000)
    prg.add(-5250000, "Na Gray molasses (+) Amp", 1.000000)
    prg.add(-5000000, "Na Gray molasses (-) Amp", 1.000000)
    prg.add(-4900000, "Shutter Gray molasses Open")
    prg.add(0, "Na Gray molasses (+) Amp", 1000.000000)
    prg.add(400, "Na Gray molasses (-) Amp", 1000.000000)
    prg.add(40000, "Na Gray molasses (+) Amp", 1.000000)
    prg.add(40400, "Na Gray molasses (-) Amp", 1.000000)
    prg.add(1000000, "Shutter Gray molasses Close")
    prg.add(5500000, "Na Gray molasses (+) Amp", 1000.000000)
    return prg
