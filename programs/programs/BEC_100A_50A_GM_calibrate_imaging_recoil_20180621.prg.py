prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(12600000, "Synchronize.sub", enable=False)
    prg.add(17600000, "All Shutter Close 2017.sub")
    prg.add(17601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(17601500, "Config Field OFF.sub")
    prg.add(17604400, "Pulse TTL2-12", polarity=1, pulse_t=0.67800)
    prg.add(17604500, "MOT lights Off close.sub")
    prg.add(17605000, "Mirrors Imaging")
    prg.add(17606735, "Gray Molasses 2017")
    prg.add(17666735, "empty.sub")
    prg.add(17666735, "Loading_GM_Q50_MTC200A")
    prg.add(19791645, "B comp x", 744.0)
    prg.add(20000000, "Bcomp y Sign Minus", enable=False)
    prg.add(22600000, "All AOM On.sub")
    prg.add(37600000, "Evaporation Ramp.sub")
    prg.add(474603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(474610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(482620000, "empty.sub")
    prg.add(487620000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(487625000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=744, stop_t=1200)
    prg.add(527625000, "Picture SetImaging", enable=False)
    prg.add(527625000, "Picture MOT beams SetImaging")
    prg.add(527626000, "Picture SetRepumper")
    prg.add(527635000, "Mirrors Imaging Bragg")
    prg.add(538656610, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(539645000, "Config Field OFF.sub", enable=False)
    prg.add(539655000, "TTL Repumper MOT ON")
    prg.add(539656500, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(539656600, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(539656700, "Picture NaK Ready no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(539656700, "Picture NaK Ready MOT beams no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(539756700, "Config Field OFF.sub")
    prg.add(547569840, "TTL2-12 OFF")
    prg.add(547669840, "Pulse uw OFF")
    prg.add(547671100, "Set MOT NaK.sub")
    prg.add(548169840, "Dark Spot MOT load.sub")
    prg.add(548269840, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.125, 5, 0.25)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
