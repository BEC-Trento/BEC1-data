prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub")
    prg.add(10, "Initialize 0 TTL and Synchronize.sub", enable=False)
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
    prg.add(10998420, "Synchronize.sub")
    prg.add(11998420, "Melassa Na.sub")
    prg.add(11999420, "Melassa Na amp.sub")
    prg.add(11999920, "Config Field OFF.sub")
    prg.add(12047920, "MOT lights Off.sub")
    prg.add(12051920, "Delta 1 Current", 200.000)
    prg.add(12051930, "Delta 2 Voltage", 30.0000)
    prg.add(12051940, "Config MT compr.sub")
    prg.add(14055960, "All Shutter Close.sub")
    prg.add(17057960, "Mirrors Imaging")
    prg.add(17557960, "IGBT B comp x ON")
    prg.add(18057960, "All AOM On.sub")
    prg.add(21057959, "B comp x", 900.0)
    prg.add(21999999, "Evaporation Ramp.sub")
    prg.add(459002999, "Decompress Current 200-50", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(459009999, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(535439999, "Config Field OFF.sub", enable=False)
    prg.add(535449999, "Picture NaK.sub", enable=False)
    prg.add(535449999, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(545290499, "Config Field OFF.sub", enable=False)
    prg.add(545300499, "Picture NaK.sub", enable=False)
    prg.add(551000000, "Picture NaK.sub", enable=False)
    prg.add(564291419, "Picture - Field off at 0ms - Levit 5ms.sub", enable=False)
    prg.add(566297959, "Picture - Field off at 0ms - Levit 50ms.sub", enable=False)
    prg.add(566297959, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(566297959, "Picture NaK Hamamatsu.sub", enable=False)
    prg.add(566297959, "Picture NaK Repump Off.sub", enable=False)
    prg.add(566308959, "Bx Grad ON", enable=False)
    prg.add(566310000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=100.000, stop_t=100.0000)
    prg.add(566311000, "B comp x ramp", start_t=0, stop_x=938, n_points=50, start_x=900, stop_t=100)
    prg.add(567411000, "Config Field OFF.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 150ms.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 100ms.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 80ms.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 180ms.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 10ms.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 20ms.sub", enable=False)
    prg.add(567411190, "Picture - Field off at 0ms - Levit 50ms.sub")
    prg.add(567411190, "Picture - Field off at 0ms - Levit 30ms.sub", enable=False)
    prg.add(567411290, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(567421290, "Bx Grad OFF", enable=False)
    prg.add(572422249, "Set MOT NaK.sub")
    prg.add(572922249, "Dark Spot MOT load.sub")
    prg.add(573022249, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(4, 22, 4)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
