prg_comment = "che schifo"
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "All Shutter Close 2017.sub")
    prg.add(6000000, "All AOM On.sub")
    prg.add(6001490, "TTL2-12 ON")
    prg.add(6101490, "Config Field OFF.sub")
    prg.add(6201490, "Mirrors Imaging")
    prg.add(11201490, "empty.sub")
    prg.add(12201490, "B comp x", 930.0)
    prg.add(12301490, "Delta 1 Current", 0.000)
    prg.add(12401490, "Config MT compr.sub")
    prg.add(12501490, "Delta 1 Voltage", 30.0000)
    prg.add(12601490, "Delta 2 Current", 200.000)
    prg.add(12701490, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=300, start_x=0.000, stop_t=1500.0000)
    prg.add(13701490, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=300, start_x=0.000, stop_t=1500.0000)
    prg.add(1213701490, "empty.sub")
    prg.add(1213701490, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=300, start_x=200.000, stop_t=1500.0000)
    prg.add(1214701490, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=1500.0000)
    prg.add(1234701490, "Config Field OFF.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('dt'), funct_enable=False))
    prg.add(1234702990, "TTL2-12 OFF")
    prg.add(1236202990, "Set MOT NaK.sub")
    prg.add(1236702990, "Dark Spot MOT load.sub")
    prg.add(1236802990, "Config MOT.sub")
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
