prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(41000, "Optical Levit (+) Amp", 1000)
    prg.add(91000, "B comp y", 0.0000)
    prg.add(101000, "IGBT B comp y ON")
    prg.add(491000, "Bcomp y Sign Plus", enable=False)
    prg.add(1491000, "Set MOT NaK.sub")
    prg.add(1991000, "Dark Spot MOT load.sub")
    prg.add(2091000, "Config MOT.sub")
    prg.add(9000000, "Optical Levit ON")
    prg.add(10000000, "Synchronize.sub", enable=False)
    prg.add(190000000, "Melassa Na.sub")
    prg.add(190001000, "Melassa Na amp.sub")
    prg.add(190001500, "Config Field OFF.sub")
    prg.add(190049500, "MOT lights Off.sub")
    prg.add(190053500, "Delta 1 Current", 200.000)
    prg.add(190053510, "Delta 2 Voltage", 30.0000)
    prg.add(190053520, "Config MT compr.sub")
    prg.add(192057540, "All Shutter Close.sub")
    prg.add(195059540, "Mirrors Imaging")
    prg.add(195559540, "IGBT B comp x ON")
    prg.add(196059540, "All AOM On.sub")
    prg.add(199059539, "B comp x", 1000.0)
    prg.add(200001579, "Evaporation Ramp.sub")
    prg.add(637004579, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(637011579, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(719916070, "Optical Levit (+) Amp", 1, enable=False)
    prg.add(720416070, "Config Field OFF.sub", enable=False)
    prg.add(720416070, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    prg.add(720416070, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(720416070, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(720416070, "Picture - Field off at 0ms - Levit 100ms.sub")
    prg.add(720416070, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(720416070, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(720416070, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(720422070, "Picture NaK.sub", enable=False)
    prg.add(721589531, "Bx Grad OFF")
    prg.add(726589531, "Set MOT NaK.sub")
    prg.add(727089531, "Dark Spot MOT load.sub")
    prg.add(727189531, "Config MOT.sub")
    prg.add(731340971, "Optical Levit (+) Amp", 1000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(500, -600, -100)
    j = 0
    while(cmd.running):
        b1 = iters[j]
        cmd.set_var('b', b1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nb = %g\n'%(j+1, len(iters), b1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
