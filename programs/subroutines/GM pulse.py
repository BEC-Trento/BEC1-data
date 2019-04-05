prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-6000000, "AOM GM Detuning", 40.000)
    prg.add(-5990000, "Shutter Gray molasses Open")
    prg.add(-5989000, "AOM GM Amp ch2 (-)", 1)
    prg.add(-5988000, "AOM GM Amp ch1 (+)", 1)
    prg.add(-20000, "TTL Repumper GM ON")
    prg.add(-500, "AOM GM Amp ch2 (-)", 1000)
    prg.add(0, "AOM GM Amp ch1 (+)", 1000)
    prg.add(20000, "AOM GM Amp ch1 (+)", 1)
    prg.add(20500, "AOM GM Amp ch2 (-)", 1)
    prg.add(22000, "TTL Repumper GM OFF")
    prg.add(25000, "Shutter Gray molasses Close")
    prg.add(6015000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(6016000, "AOM GM Amp ch2 (-)", 1000)
    return prg
