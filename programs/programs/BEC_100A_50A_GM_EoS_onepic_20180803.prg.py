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
    prg.add(210000000, "B comp x", 665.0)
    prg.add(225000000, "Evaporation Ramp.sub")
    prg.add(662003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(662010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(791220000, "empty.sub", enable=False)
    prg.add(796220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=2500.0000)
    prg.add(796230000, "B comp x ramp", start_t=0, stop_x=750, n_points=200, start_x=665, stop_t=2500)
    prg.add(831230000, "empty.sub", enable=False)
    prg.add(831231560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(831231560, "TTL0-13 broken OFF", enable=False)
    prg.add(831231617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(831231617, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(831231617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(831231617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(831231617, "Pulse uw", polarity=1, pulse_t=0.01500, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('t_uw'), funct_enable=False))
    prg.add(831271717, "Picture NaK no Rep short delay.sub", enable=False)
    prg.add(831271717, "Picture NaK short delay.sub", enable=False)
    prg.add(831271717, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False))
    prg.add(831301717, "Config Field OFF.sub")
    prg.add(831336717, "Config Field OFF.sub", enable=False)
    prg.add(847077142, "Set MOT NaK.sub")
    prg.add(847577142, "Dark Spot MOT load.sub")
    prg.add(847677142, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    t_uw_arr, run_arr = np.mgrid[1.5:3:0.5, 0:20:1, ]
    iters = list(zip(t_uw_arr.ravel(), run_arr.ravel()))
    j = 0
    while(cmd.running):
        t_uw1, run1 = iters[j]
        cmd.set_var('t_uw', t_uw1)
        cmd.set_var('run', run1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt_uw = %g\nrun = %g\n'%(j+1, len(iters), t_uw1, run1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
