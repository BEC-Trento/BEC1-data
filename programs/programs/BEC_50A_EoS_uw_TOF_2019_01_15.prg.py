prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(132100000, "Synchronize.sub", enable=False)
    prg.add(137000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(137000490, "Pulse TTL2-12", polarity=1, pulse_t=0.56900, enable=False)
    prg.add(140000000, "B comp x", 775.0)
    prg.add(155000000, "Evaporation Ramp.sub")
    prg.add(592003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(592010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(754010000, "empty.sub", enable=False)
    prg.add(759009060, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(759009990, "Picture FastStingray uw rep extra probe pic")
    prg.add(759329990, "Config Field OFF.sub", enable=False)
    prg.add(759332370, "Picture Levit 2017 - setup")
    prg.add(759334470, "Delta 1 Current", 13.200)
    prg.add(759824470, "Config Field OFF.sub")
    prg.add(759834470, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(759834500, "Picture FastStingray", enable=False)
    prg.add(759834500, "Picture FastStingray TOF Ready Trig2")
    prg.add(775574925, "Set MOT NaK.sub")
    prg.add(776074925, "Dark Spot MOT load.sub")
    prg.add(776174925, "Config MOT.sub")
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
