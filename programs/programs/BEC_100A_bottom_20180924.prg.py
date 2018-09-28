prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(202100000, "Synchronize.sub")
    prg.add(207000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(210000000, "B comp x", 695.0)
    prg.add(225000000, "Evaporation Ramp.sub")
    prg.add(662003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(662010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(791220000, "empty.sub")
    prg.add(791220000, "Config Field OFF.sub", enable=False)
    prg.add(791230000, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(791260000, "Config Field OFF.sub")
    prg.add(807000425, "Set MOT NaK.sub")
    prg.add(807500425, "Dark Spot MOT load.sub")
    prg.add(807600425, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    tof_arr, rep_arr = np.mgrid[80:200:1, 0:8:1, ]
    iters = list(zip(tof_arr.ravel(), rep_arr.ravel()))
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1, rep1 = iters[j]
        cmd.set_var('tof', tof1)
        cmd.set_var('rep', rep1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\nrep = %g\n'%(j+1, len(iters), tof1, rep1))
        cmd.run(wait_end=True, add_time=3000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
