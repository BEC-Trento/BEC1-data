prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(55000000, "Synchronize.sub")
    prg.add(60000000, "All Shutter Close 2017.sub")
    prg.add(60001490, "TTL2-12 ON")
    prg.add(60001500, "Config Field OFF.sub")
    prg.add(60004500, "MOT lights Off close.sub")
    prg.add(60005000, "Mirrors Imaging")
    prg.add(60006735, "Gray Molasses 2017")
    prg.add(60066735, "empty.sub")
    prg.add(60066735, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('curr'), funct_enable=False))
    prg.add(60066955, "Config MOT.sub")
    prg.add(60091645, "Delta 1 Voltage", 15.0000)
    prg.add(62091645, "Config MOT to MT compr.sub")
    prg.add(62191645, "B comp x", 965.0)
    prg.add(67901645, "Delta 1 Voltage", 30.0000)
    prg.add(68001645, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=1800, start_x=50.000, stop_t=900.0000)
    prg.add(68004145, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=450, start_x=0.000, stop_t=900.0000)
    prg.add(80000000, "Evaporation Ramp.sub", enable=False)
    prg.add(83000000, "empty.sub")
    prg.add(83003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=600, start_x=200.000, stop_t=600.0000)
    prg.add(83010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(103010000, "Config Field OFF.sub")
    prg.add(103019700, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(103020000, "Picture NaK.sub")
    prg.add(103023000, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(103023000, "Picture Levit 2017 - 15ms", enable=False)
    prg.add(103023000, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(103023000, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(103023000, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(103023000, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(103033000, "Picture NaK.sub", enable=False)
    prg.add(103033000, "empty.sub", enable=False)
    prg.add(111033000, "Set MOT NaK.sub")
    prg.add(111533000, "Dark Spot MOT load.sub")
    prg.add(111633000, "Config MOT.sub")
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
