prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(41000, "Optical Levit (-) Amp", 1000)
    prg.add(46000, "TTL Pinning OFF")
    prg.add(96000, "B comp y", 0.0000)
    prg.add(106000, "IGBT B comp y ON")
    prg.add(496000, "Bcomp y Sign Plus", enable=False)
    prg.add(755000, "Bx Grad OFF")
    prg.add(1496000, "Set MOT NaK.sub")
    prg.add(1996000, "Dark Spot MOT load.sub")
    prg.add(2096000, "Config MOT.sub")
    prg.add(9005000, "Optical Levit ON")
    prg.add(10005000, "Synchronize.sub", enable=False)
    prg.add(190005000, "Melassa Na.sub")
    prg.add(190006000, "Melassa Na amp.sub")
    prg.add(190006500, "Config Field OFF.sub")
    prg.add(190054500, "MOT lights Off.sub")
    prg.add(190058500, "Delta 1 Current", 200.000)
    prg.add(190058510, "Delta 2 Voltage", 30.0000)
    prg.add(190058520, "Config MT compr.sub")
    prg.add(192062540, "All Shutter Close.sub")
    prg.add(195064540, "Mirrors Imaging")
    prg.add(195564540, "IGBT B comp x ON")
    prg.add(196064540, "All AOM On.sub")
    prg.add(199064539, "B comp x", 930.0)
    prg.add(200006579, "Evaporation Ramp.sub")
    prg.add(300005100, "Pinning Lock", 0.2000, enable=False)
    prg.add(300015000, "TTL Pinning ON")
    prg.add(637009579, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(637016579, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(710235000, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(710244000, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(710244000, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(710244000, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(711544000, "Pinning Lock ramp", start_t=0, stop_x=0, n_points=200, start_x=4, stop_t=100, enable=False)
    prg.add(712801538, "Bx Grad ON", enable=False)
    prg.add(712803579, "Decompress Current 200-50", start_t=0.0000, stop_x=20.000, n_points=150, start_x=50.000, stop_t=500.0000, enable=False)
    prg.add(712853999, "Pinning Lock ramp", start_t=0, stop_x=0, n_points=100, start_x=0.2, stop_t=20, enable=False)
    prg.add(744305000, "Config Field OFF.sub", enable=False)
    prg.add(746035000, "Pinning Lock ramp", start_t=0, stop_x=0, n_points=50, start_x=0.2, stop_t=20)
    prg.add(746235500, "TTL Pinning OFF")
    prg.add(746236000, "Picture - Field off at 0ms - Levit 180ms.sub")
    prg.add(746236000, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(746244500, "Picture NaK.sub", enable=False)
    prg.add(748423499, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(748423499, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(756034027, "Set MOT NaK.sub")
    prg.add(756534027, "Dark Spot MOT load.sub")
    prg.add(756634027, "Config MOT.sub")
    prg.add(7474932999, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
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