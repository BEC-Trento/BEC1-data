prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(62100000, "Synchronize.sub", enable=False)
    prg.add(67000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(70000000, "B comp x", 775.0)
    prg.add(85000000, "Evaporation Ramp.sub")
    prg.add(462003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(462010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(492010000, "empty.sub", enable=False)
    prg.add(497010000, "Config Field OFF.sub")
    prg.add(497110000, "Picture FastStingray")
    prg.add(497110020, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(497112380, "Picture Levit 2017 - setup", enable=False)
    prg.add(497114480, "Delta 1 Current", 14.000, enable=False)
    prg.add(498304480, "Config Field OFF.sub", enable=False)
    prg.add(498314480, "Picture NaK.sub", enable=False)
    prg.add(498314480, "Picture FastStingray", enable=False)
    prg.add(514054905, "Set MOT NaK.sub")
    prg.add(514554905, "Dark Spot MOT load.sub")
    prg.add(514654905, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-3, 4, 2)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_det1 = iters[j]
        cmd.set_var('probe_det', probe_det1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_det = %g\n'%(j+1, len(iters), probe_det1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
