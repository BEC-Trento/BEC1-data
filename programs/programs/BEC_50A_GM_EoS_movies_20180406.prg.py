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
    prg.add(197601490, "TTL2-12 ON")
    prg.add(197601500, "Config Field OFF.sub")
    prg.add(197604500, "MOT lights Off close.sub")
    prg.add(197605000, "Mirrors Imaging")
    prg.add(197606735, "Gray Molasses 2017")
    prg.add(197666735, "empty.sub")
    prg.add(197666735, "Loading_GM_Q50_MTC200A")
    prg.add(199790000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(199791645, "B comp x", 915.0)
    prg.add(202600000, "All AOM On.sub")
    prg.add(217600000, "Evaporation Ramp.sub")
    prg.add(654603000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(654610000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(761900000, "empty.sub")
    prg.add(766400000, "Picture SetImaging")
    prg.add(766400000, "Picture Quantum - 1 shot Trig2")
    prg.add(766700135, "TTL2-12 ON")
    prg.add(766710135, "Pulse uw Ramp", start_t=0.0000, stop_x=0.000, n_points=24, start_x=1.000, stop_t=460.0000)
    prg.add(766711135, "Picture Ramp Trig2", start_t=0.0000, stop_x=0.000, n_points=24, start_x=1.000, stop_t=460.0000)
    prg.add(769711135, "Config Field OFF.sub", enable=False)
    prg.add(774711135, "Picture Levit 2017 - 50ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(774711135, "Picture Levit 2017 - 65ms", enable=False)
    prg.add(774711135, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(774711135, "Picture Levit 2017 - 120ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False))
    prg.add(774711135, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(776510135, "TTL2-12 ON", enable=False)
    prg.add(777711035, "Picture NaK Trig12.sub", enable=False)
    prg.add(785729675, "TTL2-12 OFF")
    prg.add(785829675, "Pulse uw OFF")
    prg.add(785830935, "Set MOT NaK.sub")
    prg.add(786329675, "Dark Spot MOT load.sub")
    prg.add(786429675, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(188, 1000, 10)
    j = 0
    while(cmd.running):
        t1 = iters[j]
        cmd.set_var('t', t1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt = %g\n'%(j+1, len(iters), t1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
