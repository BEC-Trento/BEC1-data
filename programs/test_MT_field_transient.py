prg_comment = "che schifo"
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "All Shutter Close 2017.sub", enable=False)
    prg.add(6000000, "All AOM On.sub")
    prg.add(6101490, "Config Field OFF.sub")
    prg.add(6201490, "Mirrors Imaging", enable=False)
    prg.add(7201490, "Bcomp y Sign Minus", enable=False)
    prg.add(12201490, "empty.sub")
    prg.add(13201490, "B comp x", 930.0)
    prg.add(14201490, "B comp y", 0.5000)
    prg.add(14301490, "Delta 1 Current", 0.000)
    prg.add(14401490, "Config MT compr.sub")
    prg.add(14501490, "Delta 1 Voltage", 30.0000)
    prg.add(14601490, "Delta 2 Current", 200.000)
    prg.add(14701490, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=300, start_x=0.000, stop_t=1500.0000)
    prg.add(15701490, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=300, start_x=0.000, stop_t=1500.0000)
    prg.add(55701490, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=500.0000)
    prg.add(75701490, "empty.sub")
    prg.add(75701529, "TTL2-12 ON")
    prg.add(75702529, "Config Field OFF.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('dt'), funct_enable=False))
    prg.add(75704029, "TTL2-12 OFF")
    prg.add(77204029, "Set MOT NaK.sub")
    prg.add(77704029, "Dark Spot MOT load.sub")
    prg.add(77804029, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(130, 200, 10)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
