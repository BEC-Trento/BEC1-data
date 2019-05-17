prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4990000, "Shutter Gray molasses Open", enable=False)
    prg.add(-29500, "Na Gray molasses (+) freq", 110.00)
    prg.add(-21000, "Na Gray molasses (-) freq", 90.00)
    prg.add(-20000, "TTL Repumper GM ON")
    prg.add(-500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(0, "AOM GM Amp ch2 (-)", 1000, functions=dict(amplitude=lambda x: cmd.get_var('GM_amp')))
    return prg
