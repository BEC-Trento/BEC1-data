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
    prg.add(129009540, "B comp x", 411.0)
    prg.add(129999500, "Evaporation Ramp.sub")
    prg.add(565002500, "Decompress Current MT.sub")
    prg.add(565009500, "Decompress Voltage MT.sub")
    prg.add(664119000, "B comp x ramp", start_t=0, stop_x=316, n_points=25, start_x=411, stop_t=500)
    prg.add(664120000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=300, start_x=100.000, stop_t=500.0000)
    prg.add(668530000, "RFO FM amp", 0.4000)
    prg.add(668740000, "Picture NaK 12 doubleCam.sub")
    prg.add(669490000, "RFO Sweep Trig ON")
    prg.add(669500000, "Bottom Evaporation ON")
    prg.add(669510000, "RFO Sweep Trig OFF")
    prg.add(669609000, "Pulse uw ON")
    prg.add(670389000, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(671159000, "Bottom Evaporation OFF")
    prg.add(673059000, "Pulse uw OFF")
    prg.add(673099000, "Picture - Levit Film.sub")
    prg.add(676569000, "RFO FM amp", 0.0000)
    prg.add(686569500, "Set MOT NaK.sub")
    prg.add(687069500, "Dark Spot MOT load.sub")
    prg.add(687169500, "Config MOT.sub")
    return prg