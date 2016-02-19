prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4901000, "Na Gray molasses (+) Amp", 1)
    prg.add(-4900000, "Shutter Gray molasses Open")
    prg.add(-100000, "Repumper D1 ON")
    prg.add(0, "Na Gray molasses (+) Amp", 1000)
    return prg
