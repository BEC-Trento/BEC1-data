prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(500, "K probe Repumper (+) Amp", 1.000000)
    prg.add(1000, "K Cooler 2p (+) freq", 100.000000)
    prg.add(2000, "K Cooler 1p (-) Amp", 1000.000000)
    prg.add(2500, "K Repumper 1p (+) Amp", 150.000000)
    prg.add(3000, "K Repumper 2p (+) freq", 98.000000)
    return prg
