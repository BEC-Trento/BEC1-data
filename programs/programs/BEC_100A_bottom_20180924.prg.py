prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(242100000, "Synchronize.sub")
    prg.add(247000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(250000000, "B comp x", 675.0)
    prg.add(265000000, "Evaporation Ramp.sub")
    prg.add(702003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(702010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(831220000, "empty.sub")
    prg.add(831220000, "Config Field OFF.sub")
    prg.add(831230000, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(831230000, "Picture NaK 20ms delay.sub")
    prg.add(831260000, "Config Field OFF.sub", enable=False)
    prg.add(847000425, "Set MOT NaK.sub")
    prg.add(847500425, "Dark Spot MOT load.sub")
    prg.add(847600425, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-3, 4, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_det1 = iters[j]
        cmd.set_var('probe_det', probe_det1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_det = %g\n'%(j+1, len(iters), probe_det1))
        cmd.run(wait_end=True, add_time=20000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
