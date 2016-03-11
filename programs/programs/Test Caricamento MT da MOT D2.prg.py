prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(12580, "B comp x", 0.000000)
    prg.add(50000, "Optical Levit (-) Amp", 1000.000000)
    prg.add(100000, "B comp y", 0.000000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(77010000, "Shutter Probe Na Open")
    prg.add(79950500, "Melassa Na.sub")
    prg.add(79951500, "Melassa Na amp.sub")
    prg.add(79952000, "Config Field OFF.sub")
    prg.add(80000000, "MOT lights Off.sub")
    prg.add(80004000, "Delta 1 Current", 200.000000)
    prg.add(80004010, "Delta 2 Voltage", 30.000000)
    prg.add(80004020, "Config MT compr.sub")
    prg.add(80013000, "Picture close NaK.sub", enable=False)
    prg.add(82003000, "All Shutter Close.sub")
    prg.add(85000000, "Mirrors Imaging")
    prg.add(85500000, "IGBT B comp x ON")
    prg.add(86000000, "All AOM On.sub")
    prg.add(89000000, "B comp x", 169.000000)
    prg.add(90000200, "Evaporation Ramp.sub")
    prg.add(375000300, "Decompress Current MT.sub")
    prg.add(375010000, "Decompress Voltage MT.sub")
    prg.add(477810000, "Config Field OFF.sub", enable=False)
    prg.add(484380000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(484380000, "Picture - EoS 5 frame.sub")
    prg.add(488860000, "Picture - Field off at 0ms - Levit 120ms.sub", enable=False)
    prg.add(488870000, "Picture NaK.sub", enable=False)
    prg.add(503800000, "Set MOT NaK.sub")
    prg.add(505000000, "Dark Spot MOT load.sub")
    prg.add(525000000, "Config MOT.sub")
    prg.add(526000000, "Shutter Probe Na Open", enable=False)
    return prg