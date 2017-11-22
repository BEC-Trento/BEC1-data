prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4000000, "AOM GM Detuning", 40.000)
    prg.add(-3002000, "Shutter Gray molasses Open")
    prg.add(-3001000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-3000000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-2900000, "TTL Repumper GM ON")
    prg.add(-10000, "AOM GM Amp ch2 (-)", 1000)
    prg.add(0, "AOM GM Amp ch1 (+)", 1000)
    return prg
