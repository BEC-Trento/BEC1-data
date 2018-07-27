prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1510000, "Set MOT NaK.sub")
    prg.add(2010000, "Dark Spot MOT load.sub")
    prg.add(2110000, "Config MOT.sub")
    prg.add(2120000, "B comp x", 710.0, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False))
    prg.add(2120100, "Bcomp y Sign Minus", enable=False)
    prg.add(2130000, "B comp y", 0.0700, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False))
    prg.add(2140000, "B comp z", 1.0050, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False))
    prg.add(102140000, "Synchronize.sub")
    prg.add(109500000, "Shutter Probe Na Open")
    prg.add(112291500, "Config Field OFF.sub")
    prg.add(112291555, "MOT lights Off close.sub", enable=False)
    prg.add(112291555, "Melassa Na.sub", enable=False)
    prg.add(112292105, "Melassa Na amp.sub", enable=False)
    prg.add(112292105, "TTL2-12 ON")
    prg.add(112292155, "MOT lights Off close.sub")
    prg.add(112299385, "Gray Molasses Pulse 2017", enable=False)
    prg.add(112299385, "Gray Molasses 2017")
    prg.add(112359385, "empty.sub", enable=False)
    prg.add(112561240, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(121367800, "TTL2-12 OFF")
    prg.add(121474980, "Set MOT NaK.sub")
    prg.add(121974980, "Dark Spot MOT load.sub")
    prg.add(122074980, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(710, 750, 10)
    j = 0
    while(cmd.running):
        b1 = iters[j]
        cmd.set_var('b', b1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nb = %g\n'%(j+1, len(iters), b1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
