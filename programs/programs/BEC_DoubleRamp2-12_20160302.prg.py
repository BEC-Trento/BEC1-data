prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(10000000, "Optical Levit ON")
    prg.add(119950000, "Melassa Na.sub")
    prg.add(119951000, "Melassa Na amp.sub")
    prg.add(119951500, "Config Field OFF.sub")
    prg.add(119999500, "MOT lights Off.sub")
    prg.add(120003500, "Delta 1 Current", 200.000)
    prg.add(120003510, "Delta 2 Voltage", 30.0000)
    prg.add(120003520, "Config MT compr.sub")
    prg.add(122007540, "All Shutter Close.sub")
    prg.add(125009540, "Mirrors Imaging")
    prg.add(125509540, "IGBT B comp x ON")
    prg.add(126009540, "All AOM On.sub")
    prg.add(129009540, "B comp x", 402.0)
    prg.add(129999500, "Evaporation Ramp.sub")
    prg.add(565002500, "Decompress Current MT.sub")
    prg.add(565009500, "Decompress Voltage MT.sub")
    prg.add(665589000, "B comp x ramp", start_t=0, stop_x=309, n_points=25, start_x=402, stop_t=500)
    prg.add(665590000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=300, start_x=100.000, stop_t=500.0000)
    prg.add(670430000, "Picture NaK RFO doubleCam2-12.sub")
    prg.add(671100000, "RFO FM amp", 1.0000, enable=False)
    prg.add(671100000, "RFO FM amp", 4.0000, enable=False)
    prg.add(671181000, "RFO DoubleSweepTrig Ramp", start_t=0.0000, stop_x=0.000, n_points=26, start_x=1.000, stop_t=600.0000)
    prg.add(671190000, "Pulse uw ON")
    prg.add(680594000, "Pulse uw OFF")
    prg.add(680690000, "RFO FM amp", 0.0000)
    prg.add(680993000, "Picture - Levit Film.sub")
    prg.add(694104500, "Set MOT NaK.sub")
    prg.add(694604500, "Dark Spot MOT load.sub")
    prg.add(694704500, "Config MOT.sub")
    return prg
