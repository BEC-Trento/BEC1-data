prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(125000000, "Synchronize.sub", enable=False)
    prg.add(130000000, "All Shutter Close 2017.sub")
    prg.add(130001490, "TTL2-12 ON")
    prg.add(130001500, "Config Field OFF.sub")
    prg.add(130004500, "MOT lights Off close.sub")
    prg.add(130005000, "Mirrors Imaging")
    prg.add(130006735, "Gray Molasses 2017")
    prg.add(130066735, "empty.sub")
    prg.add(130066735, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('curr'), funct_enable=False))
    prg.add(130066955, "Config MOT.sub")
    prg.add(130091645, "Delta 1 Voltage", 15.0000)
    prg.add(132091645, "Config MOT to MT compr.sub")
    prg.add(132191645, "B comp x", 965.0)
    prg.add(137901645, "Delta 1 Voltage", 30.0000)
    prg.add(138001645, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=1800, start_x=50.000, stop_t=900.0000)
    prg.add(138004145, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=450, start_x=0.000, stop_t=900.0000)
    prg.add(150000000, "Evaporation Ramp.sub", enable=False)
    prg.add(153000000, "empty.sub")
    prg.add(153003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=600, start_x=200.000, stop_t=600.0000)
    prg.add(153010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(173010000, "Config Field OFF.sub")
    prg.add(173019700, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(173020000, "Picture NaK.sub")
    prg.add(173023000, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(173023000, "Picture Levit 2017 - 15ms", enable=False)
    prg.add(173023000, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(173023000, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(173023000, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(173023000, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(173033000, "Picture NaK.sub", enable=False)
    prg.add(173033000, "empty.sub", enable=False)
    prg.add(181033000, "Set MOT NaK.sub")
    prg.add(181533000, "Dark Spot MOT load.sub")
    prg.add(181633000, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(202, 302, 2)
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
