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
    prg.add(169950500, "Melassa Na.sub")
    prg.add(169951500, "Melassa Na amp.sub")
    prg.add(169952000, "Config Field OFF.sub")
    prg.add(170000000, "MOT lights Off.sub")
    prg.add(170004000, "Delta 1 Current", 200.000)
    prg.add(170004010, "Delta 2 Voltage", 30.0000)
    prg.add(170004020, "Config MT compr.sub")
    prg.add(172008040, "All Shutter Close.sub")
    prg.add(175010040, "Mirrors Imaging")
    prg.add(175510040, "IGBT B comp x ON")
    prg.add(176010040, "All AOM On.sub")
    prg.add(179010040, "B comp x", 1089.0)
    prg.add(180000000, "Evaporation Ramp.sub")
    prg.add(617003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(617010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(685760000, "Bottom Evaporation ON", enable=False)
    prg.add(685780000, "Config Field OFF.sub")
    prg.add(685785000, "Picture NaK.sub")
    prg.add(685795000, "RFO FM amp", 0.5000, enable=False)
    prg.add(686295000, "RFO FM amp", 0.0000, enable=False)
    prg.add(686305000, "Picture - Field off at 0ms - Levit 120ms.sub", enable=False)
    prg.add(686306000, "Bottom Evaporation OFF")
    prg.add(699776000, "Set MOT NaK.sub")
    prg.add(700276000, "Dark Spot MOT load.sub")
    prg.add(700376000, "Config MOT.sub")
    return prg