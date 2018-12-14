prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1510000, "Set MOT NaK.sub")
    prg.add(2010000, "Dark Spot MOT load.sub")
    prg.add(2110000, "Config MOT.sub")
    prg.add(2120000, "B comp x", 710.0, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False), enable=False)
    prg.add(2120100, "Bcomp y Sign Minus", enable=False)
    prg.add(2130000, "B comp y", 0.0700, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False), enable=False)
    prg.add(2140000, "B comp z", 1.0050, functions=dict(value=lambda x: cmd.get_var('b'), funct_enable=False), enable=False)
    prg.add(102140000, "Synchronize.sub", enable=False)
    prg.add(102709033, "Shutter Probe Na Open", enable=False)
    prg.add(102709133, "Na Probe/Push (+) OFF")
    prg.add(107141600, "Config Field OFF.sub")
    prg.add(107141655, "MOT lights Off close.sub", enable=False)
    prg.add(107141655, "Melassa Na.sub", enable=False)
    prg.add(107142205, "Melassa Na amp.sub", enable=False)
    prg.add(107142255, "MOT lights Off close.sub")
    prg.add(107147255, "Pulse TTL2-12", polarity=1, pulse_t=0.68490, functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(107147285, "Gray Molasses 2017")
    prg.add(107207285, "empty.sub", enable=False)
    prg.add(107209164, "Picture close.sub", functions=dict(time=lambda x: x + cmd.get_var('tof')), enable=False)
    prg.add(116122904, "Set MOT NaK.sub")
    prg.add(116622904, "Dark Spot MOT load.sub")
    prg.add(116722904, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    rep_arr, tof_arr = np.mgrid[0:2:1, 2:20:2, ]
    iters = list(zip(rep_arr.ravel(), tof_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1, tof1 = iters[j]
        cmd.set_var('rep', rep1)
        cmd.set_var('tof', tof1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\ntof = %g\n'%(j+1, len(iters), rep1, tof1))
        cmd.run(wait_end=True, add_time=500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
