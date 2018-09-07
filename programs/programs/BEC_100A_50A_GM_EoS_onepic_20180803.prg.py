prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub", enable=False)
    prg.add(0, "Initialize Experiment.sub")
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(162100000, "Synchronize.sub")
    prg.add(167000000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(170000000, "B comp x", 665.0)
    prg.add(185000000, "Evaporation Ramp.sub")
    prg.add(622003000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(622010000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(751220000, "empty.sub", enable=False)
    prg.add(756220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=4500.0000)
    prg.add(756230000, "B comp x ramp", start_t=0, stop_x=6000, n_points=200, start_x=665, stop_t=4500)
    prg.add(811230000, "empty.sub", enable=False)
    prg.add(811231560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(811231560, "TTL0-13 broken OFF", enable=False)
    prg.add(811231617, "Picture Levit 2017 - 10ms", enable=False)
    prg.add(811231617, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(811231617, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(811231617, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(811231617, "Pulse uw", polarity=1, pulse_t=0.00250, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('t_uw'), funct_enable=False), enable=False)
    prg.add(811231617, "Pulse uw ON")
    prg.add(811231617, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(811231651, "Picture NaK no Rep short delay.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(811231651, "Picture NaK short delay.sub", enable=False)
    prg.add(811231651, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(811261651, "Config Field OFF.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_uw')))
    prg.add(827002076, "Set MOT NaK.sub")
    prg.add(827502076, "Dark Spot MOT load.sub")
    prg.add(827602076, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    t_uw_arr, rep_arr = np.mgrid[5:6:0.5, 0:30:1, ]
    iters = list(zip(t_uw_arr.ravel(), rep_arr.ravel()))
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        t_uw1, rep1 = iters[j]
        cmd.set_var('t_uw', t_uw1)
        cmd.set_var('rep', rep1)
        print('\n')
        print('Run #%d/%d, with variables:\nt_uw = %g\nrep = %g\n'%(j+1, len(iters), t_uw1, rep1))
        cmd.run(wait_end=True, add_time=3000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
