prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(48420, "Optical Levit (-) Amp", 1000)
    prg.add(98420, "B comp y", 0.0000)
    prg.add(108420, "IGBT B comp y ON")
    prg.add(498420, "Bcomp y Sign Plus", enable=False)
    prg.add(1498420, "Set MOT NaK.sub")
    prg.add(1998420, "Dark Spot MOT load.sub")
    prg.add(2098420, "Config MOT.sub")
    prg.add(9998420, "Optical Levit ON")
    prg.add(10998420, "Synchronize.sub", enable=False)
    prg.add(190998420, "Melassa Na.sub")
    prg.add(190999420, "Melassa Na amp.sub")
    prg.add(190999920, "Config Field OFF.sub")
    prg.add(191047920, "MOT lights Off.sub")
    prg.add(191051920, "Delta 1 Current", 200.000)
    prg.add(191051930, "Delta 2 Voltage", 30.0000)
    prg.add(191051940, "Config MT compr.sub")
    prg.add(193055960, "All Shutter Close.sub")
    prg.add(196057960, "Mirrors Imaging")
    prg.add(196557960, "IGBT B comp x ON")
    prg.add(197057960, "All AOM On.sub")
    prg.add(200057960, "B comp x", 995.0)
    prg.add(200999500, "Evaporation Ramp.sub")
    prg.add(638002500, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(638009500, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(714439500, "Config Field OFF.sub", enable=False)
    prg.add(714449500, "Picture NaK.sub", enable=False)
    prg.add(714449500, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(724290000, "Config Field OFF.sub", enable=False)
    prg.add(724300000, "Picture NaK.sub", enable=False)
    prg.add(743290920, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    prg.add(745297460, "Config Field OFF.sub", enable=False)
    prg.add(745297460, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(745297460, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(745297460, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(745297460, "Picture NaK Hamamatsu.sub", enable=False)
    prg.add(745297460, "Picture NaK Repump Off.sub", enable=False)
    prg.add(745297460, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(745297460, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(745297460, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(745300000, "Picture - Field off at 0ms - Levit 180ms.sub")
    prg.add(745300000, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(745300000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(745307460, "Picture NaK.sub", enable=False)
    prg.add(749080000, "Set MOT NaK.sub")
    prg.add(749580000, "Dark Spot MOT load.sub")
    prg.add(749680000, "Config MOT.sub")
    return prg
