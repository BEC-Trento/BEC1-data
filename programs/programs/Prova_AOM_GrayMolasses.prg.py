prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(1000, "Shutter Gray molasses Open")
    prg.add(10000000, "Na Gray molasses (+) freq", 100.000000)
    prg.add(10010000, "Na Gray molasses (-) freq", 100.000000)
    prg.add(10020000, "Na Gray molasses (+) Amp", 1.000000)
    prg.add(10020500, "Na Gray molasses (-) Amp", 1000.000000)
    prg.add(15000000, "Na Gray molasses (+) Amp", 1000.000000)
    prg.add(18000000, "Na Gray molasses (+) Amp", 1.000000)
    return prg
