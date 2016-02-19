prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(5000, "Initialize 0 TTL3")
    prg.add(10000, "Initialize 0 TTL0")
    prg.add(100000, "Set MOT K.sub")
    prg.add(1000000, "Config MOT.sub")
    prg.add(5000000, "Synchronize.sub")
    prg.add(14000000, "Config Field OFF.sub")
    prg.add(18000000, "Config MOT.sub")
    prg.add(20000000, "MOT lights Off K.sub")
    prg.add(20002500, "Config Field OFF.sub")
    prg.add(21000000, "Picture close K.sub")
    prg.add(26000000, "Set MOT K.sub")
    prg.add(27000000, "Config MOT.sub")
    prg.add(28000000, "K Cooler 2p (+) freq", 98.000000)
    prg.add(29000000, "K probe Cooler (-) freq", 96.000000)
    prg.add(30000000, "K probe Cooler (-) Amp", 1000.000000)
    prg.add(31000000, "K probe Repumper (+) Amp", 1.000000)
    prg.add(32000000, "K Repumper 1p (+) Amp", 1.000000)
    return prg
