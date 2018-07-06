prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(52600000, "Synchronize.sub", enable=False)
    prg.add(57600000, "All Shutter Close 2017.sub")
    prg.add(57601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(57601500, "Config Field OFF.sub")
    prg.add(57604500, "MOT lights Off close.sub")
    prg.add(57605000, "Mirrors Imaging")
    prg.add(57606735, "Gray Molasses 2017")
    prg.add(57666735, "empty.sub")
    prg.add(57666735, "Loading_GM_Q50_MTC200A")
    prg.add(59791645, "B comp x", 733.0)
    prg.add(60000000, "Bcomp y Sign Minus", enable=False)
    prg.add(62600000, "All AOM On.sub")
    prg.add(77600000, "Evaporation Ramp.sub")
    prg.add(514603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(514610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(538610000, "empty.sub")
    prg.add(543610000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(543615000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=730, stop_t=1200, enable=False)
    prg.add(583615000, "Picture SetImaging")
    prg.add(583615000, "Picture MOT beams SetImaging", enable=False)
    prg.add(583625000, "Mirrors Imaging Bragg", enable=False)
    prg.add(583635000, "Picture SetRepumper")
    prg.add(587635000, "Pulse TTL2-12", polarity=1, pulse_t=0.67800)
    prg.add(595635000, "Config Field OFF.sub", enable=False)
    prg.add(595645000, "Picture Levit 2017 - setup", enable=False)
    prg.add(595646000, "Delta 1 Current", 13.200, enable=False)
    prg.add(595646000, "IGBT 4 Open", enable=False)
    prg.add(595656000, "Pulse TTL2-12", polarity=1, pulse_t=0.01540, enable=False)
    prg.add(595656100, "TTL Repumper MOT ON")
    prg.add(595657600, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(595657710, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(595657710, "Picture NaK Ready MOT beams no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(595677710, "Pulse Repumper MOT", polarity=1, pulse_t=0.15000, enable=False)
    prg.add(595677810, "Picture NaK Ready no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(595977810, "Config Field OFF.sub")
    prg.add(603790950, "TTL2-12 OFF")
    prg.add(603890950, "Pulse uw OFF")
    prg.add(603892210, "Set MOT NaK.sub")
    prg.add(604390950, "Dark Spot MOT load.sub")
    prg.add(604490950, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 10, 2)
    j = 0
    while(cmd.running):
        det1 = iters[j]
        cmd.set_var('det', det1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndet = %g\n'%(j+1, len(iters), det1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
