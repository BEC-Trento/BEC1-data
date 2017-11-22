prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(52100000, "Synchronize.sub")
    prg.add(57970000, "Shutter Probe Na Open")
    prg.add(59470000, "All Shutter Close.sub", enable=False)
    prg.add(59971490, "TTL2-12 ON")
    prg.add(59971500, "Config Field OFF.sub")
    prg.add(59974500, "MOT lights Off close.sub")
    prg.add(59976735, "Gray Molasses 2017")
    prg.add(60036735, "empty.sub")
    prg.add(60036735, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('curr'), funct_enable=False))
    prg.add(60036955, "Config MOT.sub")
    prg.add(60061645, "Delta 1 Voltage", 15.0000)
    prg.add(60061645, "Config MOT to MT compr.sub", enable=False)
    prg.add(62061633, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(62061643, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(62092400, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(67177085, "B comp x", 975.0, enable=False)
    prg.add(68092399, "Delta 1 Current ramp", start_t=0.0000, stop_x=200.000, n_points=3000, start_x=50.000, stop_t=1000.0000, enable=False)
    prg.add(68097399, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=30.000, n_points=3000, start_x=0.000, stop_t=1000.0000, enable=False)
    prg.add(68097399, "Evaporation Ramp.sub", enable=False)
    prg.add(68097399, "empty.sub", enable=False)
    prg.add(68097409, "Config Field OFF.sub", enable=False)
    prg.add(68109264, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(68109264, "Picture NaK.sub", enable=False)
    prg.add(77016764, "Set MOT NaK.sub")
    prg.add(77516764, "Dark Spot MOT load.sub")
    prg.add(77616764, "Config MOT.sub")
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
