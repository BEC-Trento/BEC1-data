prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-6000, "TTL Repumper GM OFF")
    prg.add(0, "AOM GM Amp ch1 (+)", 1)
    prg.add(400, "AOM GM Amp ch2 (-)", 1)
    prg.add(960000, "Shutter Gray molasses Close")
    prg.add(5460000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(5461000, "AOM GM Amp ch2 (-)", 1000)
    return prg
