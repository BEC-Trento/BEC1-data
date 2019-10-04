prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(30000000, "Na Probe x (+) freq", 120.00)
    prg.add(50000000, "Na Probe x (+) freq", 100.00)
    prg.add(70000000, "Na Probe x (+) freq", 120.00)
    prg.add(90000000, "Na Probe x (+) freq", 100.00)
    prg.add(110000000, "Na Probe x (+) freq", 110.00)
    return prg
