prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2000, "TTL Repumper GM OFF")
    prg.add(0, "AOM GM Amp ch1 (+)", 0)
    prg.add(400, "AOM GM Amp ch2 (-)", 0)
    prg.add(800, "Na Gray molasses (+) freq", 80.00)
    prg.add(1200, "Na Gray molasses (-) freq", 80.00)
    prg.add(1600, "Shutter Gray molasses Close")
    return prg
