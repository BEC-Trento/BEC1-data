prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(510, "Mirrors Imaging")
    prg.add(1000, "Config Field OFF.sub", enable=False)
    prg.add(11500, "TTL3-11 ON")
    prg.add(48920, "Optical Levit (-) Amp", 1000, enable=False)
    prg.add(98920, "B comp y", 0.0000)
    prg.add(108920, "IGBT B comp y ON")
    prg.add(498920, "Bcomp y Sign Plus", enable=False)
    prg.add(1498920, "Set MOT NaK.sub", enable=False)
    prg.add(1998920, "Dark Spot MOT load.sub", enable=False)
    prg.add(2098920, "Config MOT.sub", enable=False)
    prg.add(9998920, "Melassa Na.sub", enable=False)
    prg.add(9999920, "Melassa Na amp.sub", enable=False)
    prg.add(10000420, "Config Field OFF.sub")
    prg.add(10048420, "MOT lights Off.sub")
    prg.add(15054440, "Mirrors Imaging")
    prg.add(16054440, "All AOM On.sub")
    prg.add(21054440, "Picture NaK.sub", enable=False)
    prg.add(21054440, "Picture NaK Repump Off.sub", enable=False)
    prg.add(21054440, "Picture NaK Hamamatsu.sub", enable=False)
    prg.add(21054440, "Picture EoS 6 frame - Hamamatsu.sub", enable=False)
    prg.add(21054440, "Picture NaK RFO doubleCam2-12.sub", enable=False)
    prg.add(21054440, "RFO SetImaging+Ref-solo-Hamamatsu")
    prg.add(21054440, "Picture NaK Init.sub", enable=False)
    prg.add(21954440, "RFO ImagingQuantum-solo-Hamamatsu Ramp", start_t=0.0000, stop_x=0.000, n_points=10, start_x=1.000, stop_t=36.0000)
    prg.add(21957860, "Picture - Field off at 0ms - Levit 50ms - Hamamatsu.sub", enable=False)
    prg.add(29726280, "Set MOT NaK.sub", enable=False)
    prg.add(30226280, "Dark Spot MOT load.sub", enable=False)
    prg.add(30326280, "Config MOT.sub", enable=False)
    prg.add(30900000, "All AOM On.sub")
    return prg