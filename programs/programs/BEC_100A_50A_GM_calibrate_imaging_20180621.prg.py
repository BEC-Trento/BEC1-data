prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(82600000, "Synchronize.sub", enable=False)
    prg.add(87600000, "All Shutter Close 2017.sub")
    prg.add(87601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(87601500, "Config Field OFF.sub")
    prg.add(87604500, "MOT lights Off close.sub")
    prg.add(87605000, "Mirrors Imaging")
    prg.add(87606735, "Gray Molasses 2017")
    prg.add(87666735, "empty.sub")
    prg.add(87666735, "Loading_GM_Q50_MTC200A")
    prg.add(89791645, "B comp x", 720.0)
    prg.add(90000000, "Bcomp y Sign Minus", enable=False)
    prg.add(92600000, "All AOM On.sub")
    prg.add(107600000, "Evaporation Ramp.sub")
    prg.add(544603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(544610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(673820000, "empty.sub")
    prg.add(678820000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(678825000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=730, stop_t=1200, enable=False)
    prg.add(718825000, "Picture SetImaging", enable=False)
    prg.add(718825000, "Picture MOT beams SetImaging")
    prg.add(718835000, "Mirrors Imaging Bragg")
    prg.add(718845000, "Picture SetRepumper")
    prg.add(722845000, "Pulse TTL2-12", polarity=1, pulse_t=0.67800)
    prg.add(722846000, "MT trap Heating", start_t=0.0000, func_args="amp=1, freq=160, offs=50", n_points=1000, func="amp*sin(2*pi*freq*t) + offs", stop_t=625.0000)
    prg.add(730846000, "Config Field OFF.sub")
    prg.add(730856000, "Pulse TTL2-12", polarity=1, pulse_t=0.01540, enable=False)
    prg.add(730856100, "TTL Repumper MOT ON")
    prg.add(730857600, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(730857710, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(730867710, "Picture NaK Ready MOT beams no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(730867710, "Picture Levit 2017 - setup", enable=False)
    prg.add(730868710, "Delta 1 Current", 13.200, enable=False)
    prg.add(731658710, "IGBT 4 Open", enable=False)
    prg.add(731668610, "Pulse TTL2-12", polarity=1, pulse_t=0.01560, enable=False)
    prg.add(731668744, "Picture NaK Ready - high intensity.sub", enable=False)
    prg.add(739590884, "TTL2-12 OFF")
    prg.add(739690884, "Pulse uw OFF")
    prg.add(739692144, "Set MOT NaK.sub")
    prg.add(740190884, "Dark Spot MOT load.sub")
    prg.add(740290884, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    det_arr, tof_arr = np.mgrid[3:5:3, 0.5:1.6:1, ]
    iters = list(zip(det_arr.ravel(), tof_arr.ravel()))
    j = 0
    while(cmd.running):
        det1, tof1 = iters[j]
        cmd.set_var('det', det1)
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndet = %g\ntof = %g\n'%(j+1, len(iters), det1, tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
