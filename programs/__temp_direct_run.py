prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(2500000, "All Shutter Open NaK.sub")
    prg.add(2600000, "Na Gray molasses (+) freq", 117.00)
    prg.add(2700000, "Na Gray molasses (-) freq", 83.00)
    prg.add(2800000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(2900000, "AOM GM Amp ch2 (-)", 1000)
    return prg
