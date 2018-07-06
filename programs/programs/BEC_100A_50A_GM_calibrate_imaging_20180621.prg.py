prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(32600000, "Synchronize.sub", enable=False)
    prg.add(37600000, "All Shutter Close 2017.sub")
    prg.add(37601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(37601500, "Config Field OFF.sub")
    prg.add(37604500, "MOT lights Off close.sub")
    prg.add(37605000, "Mirrors Imaging")
    prg.add(37606735, "Gray Molasses 2017")
    prg.add(37666735, "empty.sub")
    prg.add(37666735, "Loading_GM_Q50_MTC200A")
    prg.add(39791645, "B comp x", 733.0)
    prg.add(40000000, "Bcomp y Sign Minus", enable=False)
    prg.add(42600000, "All AOM On.sub")
    prg.add(57600000, "Evaporation Ramp.sub")
    prg.add(494603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(494610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(550610000, "empty.sub")
    prg.add(555610000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(555615000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=730, stop_t=1200, enable=False)
    prg.add(595615000, "Picture SetImaging")
    prg.add(595625000, "Picture SetRepumper")
    prg.add(595625000, "Picture SetRepumper2", enable=False)
    prg.add(602636810, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(603635000, "Pulse TTL2-12", polarity=1, pulse_t=0.01540)
    prg.add(603635200, "Picture Repumper Ready Trig2.sub", enable=False)
    prg.add(603635200, "Pulse Repumper MOT", polarity=1, pulse_t=0.15000)
    prg.add(603636810, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(603925000, "Config Field OFF.sub")
    prg.add(612359984, "TTL2-12 OFF")
    prg.add(612459984, "Pulse uw OFF")
    prg.add(612461244, "Set MOT NaK.sub")
    prg.add(612959984, "Dark Spot MOT load.sub")
    prg.add(613059984, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    tof_arr, det_arr = np.mgrid[0.4:1.6:135, 5:20:564, ]
    iters = list(zip(tof_arr.ravel(), det_arr.ravel()))
    j = 0
    while(cmd.running):
        tof1, det1 = iters[j]
        cmd.set_var('tof', tof1)
        cmd.set_var('det', det1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\ndet = %g\n'%(j+1, len(iters), tof1, det1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
