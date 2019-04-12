prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5990000, "Shutter Gray molasses Open")
    prg.add(-5989000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-5988000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-5510000, "Na Gray molasses (-) freq", 90.00)
    prg.add(-5500000, "Na Gray molasses (+) freq", 110.00)
    prg.add(-20000, "TTL Repumper GM ON", enable=False)
    prg.add(-500, "AOM GM Amp ch2 (-)", 1000)
    prg.add(0, "AOM GM Amp ch1 (+)", 1000)
    return prg
