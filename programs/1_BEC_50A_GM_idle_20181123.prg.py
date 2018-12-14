prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(202100000, "Synchronize.sub", enable=False)
    prg.add(207000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(210000000, "B comp x", 775.0)
    prg.add(225000000, "Evaporation Ramp.sub")
    prg.add(662003000, "Decompress Current 200-100", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(662010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(802010000, "empty.sub", enable=False)
    prg.add(807010000, "Config Field OFF.sub", enable=False)
    prg.add(807020000, "Pulse TTL2-12", polarity=1, pulse_t=0.95600, enable=False)
    prg.add(807020030, "Picture FastStingray", enable=False)
    prg.add(807022410, "Picture Levit 2017 - setup")
    prg.add(807024510, "Delta 1 Current", 14.000)
    prg.add(808214510, "Config Field OFF.sub")
    prg.add(808224510, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(808224540, "Picture FastStingray")
    prg.add(823964965, "Set MOT NaK.sub")
    prg.add(824464965, "Dark Spot MOT load.sub")
    prg.add(824564965, "Config MOT.sub")
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
