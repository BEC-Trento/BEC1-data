prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1000000, "Shutter Gray molasses Close")
    prg.add(0, "Na Gray molasses (+) Amp", 1.000000)
    prg.add(4500000, "Na Gray molasses (+) Amp", 1000.000000)
    return prg
