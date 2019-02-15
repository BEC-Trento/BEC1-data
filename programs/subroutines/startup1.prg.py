prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(12580, "B comp x", 0.0)
    prg.add(50000, "Optical Levit (-) Amp", 1000, enable=False)
    prg.add(100000, "B comp y", 0.0000)
    prg.add(110000, "IGBT B comp y ON")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    rep1 = np.arange(0,6,1)
    uw1 = [0.7, 1.8, 2.5]
    rep_arr, uw_tau_arr = np.meshgrid(rep1, uw1)
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
        cmd.run(wait_end=True, add_time=35000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
