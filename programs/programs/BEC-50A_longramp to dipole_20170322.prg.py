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
    prg.add(200057959, "B comp x", 935.0)
    prg.add(200999999, "Evaporation Ramp.sub")
    prg.add(638002999, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(638009999, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(745300500, "TTL2-10 ON")
    prg.add(745301000, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=200, start_x=0.000, stop_t=700.0000)
    prg.add(745311000, "Config Field OFF.sub", enable=False)
    prg.add(745311499, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(745321000, "Picture NaK.sub", enable=False)
    prg.add(752371000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=50.000, stop_t=600.0000)
    prg.add(758380000, "Picture NaK.sub", enable=False)
    prg.add(758381000, "Dipole Trap x DAC V", 0.0000)
    prg.add(758381100, "TTL2-10 OFF")
    prg.add(758391100, "Picture NaK.sub")
    prg.add(758411100, "Bx Grad OFF")
    prg.add(763401100, "Set MOT NaK.sub")
    prg.add(763901100, "Dark Spot MOT load.sub")
    prg.add(764001100, "Config MOT.sub")
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
