prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(192600000, "Synchronize.sub", enable=False)
    prg.add(197600000, "All Shutter Close 2017.sub")
    prg.add(197601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(197601500, "Config Field OFF.sub")
    prg.add(197604500, "MOT lights Off close.sub")
    prg.add(197605000, "Mirrors Imaging")
    prg.add(197606735, "Gray Molasses 2017")
    prg.add(197666735, "empty.sub")
    prg.add(197666735, "Loading_GM_Q50_MTC200A")
    prg.add(199791645, "B comp x", 720.0)
    prg.add(200000000, "Bcomp y Sign Minus", enable=False)
    prg.add(202600000, "All AOM On.sub")
    prg.add(217600000, "Evaporation Ramp.sub")
    prg.add(654603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(654610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(766180000, "empty.sub")
    prg.add(771180000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=150, start_x=100.000, stop_t=600.0000)
    prg.add(771185000, "B comp x ramp", start_t=0, stop_x=860, n_points=150, start_x=720, stop_t=600)
    prg.add(781185000, "Picture SetImaging")
    prg.add(781195484, "Picture SetRepumper")
    prg.add(786195100, "Picture NaK Ready.sub", enable=False)
    prg.add(786195200, "Picture Levit 2017 - setup")
    prg.add(786196200, "Delta 1 Current", 14.100)
    prg.add(786586200, "IGBT 4 Open")
    prg.add(786595190, "TTL2-12 ON")
    prg.add(786596200, "Picture NaK Ready.sub")
    prg.add(794518340, "TTL2-12 OFF")
    prg.add(795518340, "Config Field OFF.sub")
    prg.add(795618340, "Pulse uw OFF")
    prg.add(795619600, "Set MOT NaK.sub")
    prg.add(796118340, "Dark Spot MOT load.sub")
    prg.add(796218340, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(120, 200, 7)
    j = 0
    while(cmd.running):
        tau1 = iters[j]
        cmd.set_var('tau', tau1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntau = %g\n'%(j+1, len(iters), tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
