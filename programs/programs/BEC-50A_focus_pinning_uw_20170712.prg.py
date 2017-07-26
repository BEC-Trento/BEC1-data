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
    prg.add(200000, "TTL Pinning ON")
    prg.add(200000, "TTL Pinning OFF", enable=False)
    prg.add(210000, "Pinning Lock", 1.0000)
    prg.add(501000, "Bcomp y Sign Plus", enable=False)
    prg.add(1501000, "Set MOT NaK.sub")
    prg.add(2001000, "Dark Spot MOT load.sub")
    prg.add(2101000, "Config MOT.sub")
    prg.add(9010000, "Optical Levit ON")
    prg.add(10010000, "Synchronize.sub", enable=False)
    prg.add(190010000, "Melassa Na.sub")
    prg.add(190011000, "Melassa Na amp.sub")
    prg.add(190011500, "Config Field OFF.sub")
    prg.add(190059500, "MOT lights Off.sub")
    prg.add(190063500, "Delta 1 Current", 200.000)
    prg.add(190063510, "Delta 2 Voltage", 30.0000)
    prg.add(190063520, "Config MT compr.sub")
    prg.add(192067540, "All Shutter Close.sub")
    prg.add(195060000, "Mirrors Imaging")
    prg.add(195560000, "IGBT B comp x ON")
    prg.add(196060000, "All AOM On.sub")
    prg.add(199060000, "B comp x", 980.0)
    prg.add(200000000, "Evaporation Ramp.sub")
    prg.add(637003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=500.0000)
    prg.add(637010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=500.0000)
    prg.add(744300000, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(744300000, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(744300000, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(746297000, "Pinning Lock ramp", start_t=0, stop_x=0, n_points=100, start_x=8, stop_t=10, enable=False)
    prg.add(746300000, "Pinning Lock", 0.0000)
    prg.add(746300050, "TTL Pinning OFF")
    prg.add(746300100, "Pulse uw ON")
    prg.add(746300160, "Pulse uw OFF")
    prg.add(746300210, "Config Field OFF.sub")
    prg.add(746301210, "Picture NaK.sub", enable=False)
    prg.add(746301210, "Picture NaK no Rep.sub")
    prg.add(746301210, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(746301210, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(746301210, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(746301210, "Picture - Field off at 0ms - Levit 120ms.sub", enable=False)
    prg.add(746301210, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(747478771, "Bx Grad OFF")
    prg.add(752478771, "Set MOT NaK.sub")
    prg.add(752978771, "Dark Spot MOT load.sub")
    prg.add(753078771, "Config MOT.sub")
    prg.add(755078771, "TTL Pinning ON")
    prg.add(755178771, "Pinning Lock", 3.0000)
    prg.add(757178771, "Optical Levit (+) Amp", 1000)
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
