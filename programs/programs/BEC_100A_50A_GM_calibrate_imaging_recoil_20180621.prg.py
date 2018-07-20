prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(102600000, "Synchronize.sub", enable=False)
    prg.add(107600000, "All Shutter Close 2017.sub")
    prg.add(107601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(107601500, "Config Field OFF.sub")
    prg.add(107604400, "Pulse TTL2-12", polarity=1, pulse_t=0.67800)
    prg.add(107604500, "MOT lights Off close.sub")
    prg.add(107605000, "Mirrors Imaging")
    prg.add(107606735, "Gray Molasses 2017")
    prg.add(107666735, "empty.sub")
    prg.add(107666735, "Loading_GM_Q50_MTC200A")
    prg.add(109791645, "B comp x", 744.0)
    prg.add(110000000, "Bcomp y Sign Minus", enable=False)
    prg.add(112600000, "All AOM On.sub")
    prg.add(127600000, "Evaporation Ramp.sub")
    prg.add(564603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(564610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(590640000, "empty.sub")
    prg.add(595640000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(595645000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=744, stop_t=1200)
    prg.add(635645000, "Picture SetImaging", enable=False)
    prg.add(635645000, "Picture MOT beams SetImaging")
    prg.add(635646000, "Picture SetRepumper")
    prg.add(635655000, "Mirrors Imaging Bragg")
    prg.add(646676610, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(647665000, "Config Field OFF.sub", enable=False)
    prg.add(647675000, "TTL Repumper MOT ON")
    prg.add(647676500, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(647676600, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(647680000, "Picture NaK Ready no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(647680000, "Picture NaK Ready MOT beams no Rep Trig2.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(647780000, "Config Field OFF.sub")
    prg.add(655593140, "TTL2-12 OFF")
    prg.add(655693140, "Pulse uw OFF")
    prg.add(655694400, "Set MOT NaK.sub")
    prg.add(656193140, "Dark Spot MOT load.sub")
    prg.add(656293140, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 20, 1)
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
