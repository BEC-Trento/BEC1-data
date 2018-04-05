prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(45000000, "Synchronize.sub")
    prg.add(50000000, "All Shutter Close 2017.sub")
    prg.add(50001490, "TTL2-12 ON")
    prg.add(50001500, "Config Field OFF.sub")
    prg.add(50004500, "MOT lights Off close.sub")
    prg.add(50005000, "Mirrors Imaging")
    prg.add(50006735, "Gray Molasses 2017")
    prg.add(50066735, "empty.sub")
    prg.add(50066735, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('curr'), funct_enable=False))
    prg.add(50066955, "Config MOT.sub")
    prg.add(50091645, "Delta 1 Voltage", 15.0000)
    prg.add(52091645, "Config MOT to MT compr.sub")
    prg.add(52191645, "B comp x", 975.0)
    prg.add(57901645, "Delta 1 Voltage", 30.0000)
    prg.add(58001645, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=1800, start_x=50.000, stop_t=900.0000)
    prg.add(58004145, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=450, start_x=0.000, stop_t=900.0000)
    prg.add(70000000, "Evaporation Ramp.sub")
    prg.add(507003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(507010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(633030000, "Config Field OFF.sub", enable=False)
    prg.add(633040000, "Picture NaK.sub", enable=False)
    prg.add(636698000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(636700000, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(636700000, "Picture Levit 2017 - 15ms", enable=False)
    prg.add(636700000, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(636700000, "Picture Levit 2017 - 150ms")
    prg.add(636700000, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(636700000, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(636710000, "Picture NaK.sub", enable=False)
    prg.add(636710000, "empty.sub", enable=False)
    prg.add(644710000, "Set MOT NaK.sub")
    prg.add(645210000, "Dark Spot MOT load.sub")
    prg.add(645310000, "Config MOT.sub")
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
