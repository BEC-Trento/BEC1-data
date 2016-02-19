prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(500000, "K Cooler 2p (+) freq", 97.000000)
    prg.add(510000, "K Repumper 2p (+) freq", 96.500000)
    prg.add(1000000, "Set MOT.sub")
    prg.add(1500000, "Config MOT.sub")
    prg.add(2000000, "Delta 1 Current", 6.000000)
    prg.add(2500000, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(2510000, "K probe Repumper (+) Amp", 1000.000000)
    prg.add(5000000, "K probe Cooler (-) freq", 98.000000)
    prg.add(5010000, "K probe Repumper (+) freq", 120.000000)
    prg.add(6000000, "Rele 5 Close", enable=False)
    prg.add(7000000, "Rele 5 Open")
    return prg
