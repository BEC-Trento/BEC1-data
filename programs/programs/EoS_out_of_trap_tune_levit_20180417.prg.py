prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub", enable=False)
    prg.add(2000000, "Dark Spot MOT load.sub", enable=False)
    prg.add(2100000, "Config MOT.sub")
    prg.add(12600000, "Synchronize.sub", enable=False)
    prg.add(17600000, "All Shutter Close 2017.sub")
    prg.add(17601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(17601500, "Config Field OFF.sub")
    prg.add(17602000, "Mirrors Imaging", enable=False)
    prg.add(19601000, "B comp x", 925.0)
    prg.add(19602000, "Config MT compr.sub")
    prg.add(19603000, "Delta 1 Voltage", 30.0000)
    prg.add(19604000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=300, start_x=0.000, stop_t=600.0000)
    prg.add(26894000, "empty.sub")
    prg.add(31894000, "B comp y ramp", start_t=0, stop_x=1, n_points=100, start_x=0, stop_t=1000, enable=False)
    prg.add(46894000, "TTL2-12 ON")
    prg.add(46895000, "Picture Levit CFO 2018 - 10ms")
    prg.add(46995056, "Picture NaK.sub", enable=False)
    prg.add(55013696, "TTL2-12 OFF")
    prg.add(55113696, "Pulse uw OFF")
    prg.add(55114956, "Set MOT NaK.sub", enable=False)
    prg.add(55613696, "Dark Spot MOT load.sub", enable=False)
    prg.add(55713696, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(100, 300, 6)
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
