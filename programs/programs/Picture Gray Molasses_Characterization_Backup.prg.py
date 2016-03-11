prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(4000000, "Shutter Optical Levit Close")
    prg.add(64000000, "Shutter Probe Na Open")
    prg.add(66949000, "Config Field OFF.sub")
    prg.add(66950000, "MOT lights Off.sub")
    prg.add(66952000, "GrayMolasses_ON.sub")
    prg.add(66957000, "Rampa_GrayMol.sub")
    prg.add(67120000, "GrayMolasses_OFF.sub")
    prg.add(67170000, "Picture close NaK.sub")
    prg.add(73232085, "Set MOT NaK.sub")
    prg.add(73732085, "Dark Spot MOT load.sub")
    prg.add(73832085, "Config MOT.sub")
    prg.add(73932085, "Shutter Gray molasses Open", enable=False)
    prg.add(74329045, "Rampa GM per test", start_t=0.0000, stop_x=200.000, n_points=25, start_x=1000.000, stop_t=2.0000, enable=False)
    prg.add(74339045, "Repumper D1 OFF", enable=False)
    return prg