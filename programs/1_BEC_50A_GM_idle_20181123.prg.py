prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(7100000, "Synchronize.sub")
    prg.add(12000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(12000490, "Pulse TTL2-12", polarity=1, pulse_t=0.56900, enable=False)
    prg.add(15000000, "B comp x", 775.0)
    prg.add(30000000, "Evaporation Ramp.sub")
    prg.add(467003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(467010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(607010000, "empty.sub", enable=False)
    prg.add(612010000, "Config Field OFF.sub", enable=False)
    prg.add(612010000, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(612010030, "Picture FastStingray", enable=False)
    prg.add(612010030, "Picture FastStingray uw rep")
    prg.add(613010030, "Config Field OFF.sub")
    prg.add(613012410, "Picture Levit 2017 - setup", enable=False)
    prg.add(613014510, "Delta 1 Current", 13.200, enable=False)
    prg.add(613504510, "Config Field OFF.sub", enable=False)
    prg.add(613514510, "Pulse TTL2-12", polarity=1, pulse_t=0.95600, enable=False)
    prg.add(613514540, "Picture FastStingray", enable=False)
    prg.add(629254965, "Set MOT NaK.sub")
    prg.add(629754965, "Dark Spot MOT load.sub")
    prg.add(629854965, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    rep_arr, uw_tau_arr = np.mgrid[0:3:1, 0.4:3:0.3, ]
    iters = list(zip(rep_arr.ravel(), uw_tau_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rep1, uw_tau1 = iters[j]
        cmd.set_var('rep', rep1)
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nrep = %g\nuw_tau = %g\n'%(j+1, len(iters), rep1, uw_tau1))
        cmd.run(wait_end=True, add_time=15000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
