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
    prg.add(129009540, "B comp x", 885.0)
    prg.add(129999500, "Evaporation Ramp.sub")
    prg.add(565002500, "Decompress Current MT.sub")
    prg.add(565009500, "Decompress Voltage MT.sub")
    prg.add(665589000, "B comp x ramp", start_t=0, stop_x=998, n_points=25, start_x=885, stop_t=500)
    prg.add(665590000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=300, start_x=100.000, stop_t=500.0000)
    prg.add(670430000, "Picture NaK RFO doubleCam2-12.sub")
    prg.add(671100000, "RFO FM amp", 0.3500)
    prg.add(671169000, "RFO SingleSweepTrig12 Ramp", start_t=0.0000, stop_x=0.000, n_points=81, start_x=1.000, stop_t=960.0000)
    prg.add(671178000, "Pulse uw ON")
    prg.add(672160000, "RFO FM amp", 0.3600)
    prg.add(672860000, "RFO FM amp", 0.4100)
    prg.add(673860000, "RFO FM amp", 0.4600)
    prg.add(674860000, "RFO FM amp", 0.5200)
    prg.add(675860000, "RFO FM amp", 0.5700)
    prg.add(676860000, "RFO FM amp", 0.6600)
    prg.add(677860000, "RFO FM amp", 0.7800)
    prg.add(678860000, "RFO FM amp", 1.3000)
    prg.add(679860000, "RFO FM amp", 2.5000)
    prg.add(684182000, "Pulse uw OFF")
    prg.add(684278000, "RFO FM amp", 0.0000)
    prg.add(684581000, "Picture - Levit Film.sub")
    prg.add(697692500, "Set MOT NaK.sub")
    prg.add(698192500, "Dark Spot MOT load.sub")
    prg.add(698292500, "Config MOT.sub")
    return prg
