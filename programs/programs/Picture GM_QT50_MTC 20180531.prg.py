prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(122100000, "Synchronize.sub", enable=False)
    prg.add(127970000, "Shutter Probe Na Open")
    prg.add(129470000, "All Shutter Close.sub", enable=False)
    prg.add(129971490, "Pulse TTL2-12", polarity=1, pulse_t=0.05000)
    prg.add(129971500, "Config Field OFF.sub")
    prg.add(129974500, "MOT lights Off close.sub")
    prg.add(129976735, "Gray Molasses 2017")
    prg.add(130036735, "empty.sub")
    prg.add(130036735, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('curr'), funct_enable=False))
    prg.add(130036955, "Config MOT.sub")
    prg.add(130061645, "Delta 1 Voltage", 15.0000)
    prg.add(131061645, "Config MOT to MT compr.sub")
    prg.add(134061645, "empty.sub")
    prg.add(134061645, "Config Field OFF.sub")
    prg.add(134161645, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(139871645, "Delta 1 Voltage", 30.0000, enable=False)
    prg.add(139971645, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=1800, start_x=50.000, stop_t=900.0000, enable=False)
    prg.add(139974145, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=450, start_x=0.000, stop_t=900.0000, enable=False)
    prg.add(148893510, "Set MOT NaK.sub")
    prg.add(149393510, "Dark Spot MOT load.sub")
    prg.add(149493510, "Config MOT.sub")
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
