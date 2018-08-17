prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(195000000, "Synchronize.sub", enable=False)
    prg.add(199900000, "[MAIN] Loading MOT - GM - MTC200A")
    prg.add(202900000, "B comp x", 665.0)
    prg.add(217900000, "Evaporation Ramp.sub")
    prg.add(654903000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(654910000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=100, start_x=30.000, stop_t=600.0000)
    prg.add(784120000, "empty.sub")
    prg.add(789120000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(789130000, "B comp x ramp", start_t=0, stop_x=750, n_points=200, start_x=665, stop_t=1200)
    prg.add(809130000, "empty.sub")
    prg.add(809131630, "TTL2-12 ON", enable=False)
    prg.add(809131630, "Picture Levit 2017 - variables", functions=dict(time=lambda x: x + 0))
    prg.add(809131630, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(809131630, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(809131630, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(809231630, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(809231630, "Picture NaK no Rep.sub", enable=False)
    prg.add(809231630, "empty.sub", enable=False)
    prg.add(817231630, "Set MOT NaK.sub")
    prg.add(817731630, "Dark Spot MOT load.sub")
    prg.add(817831630, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    tof_arr = np.asarray([10,20,30,40,50,70,100])
    tof_arr = np.repeat(tof_arr, 1)
    I0, a, b = 11.4, 29.7, -82
    Itof_arr = I0 + a*1e-3*tof_arr + b*1e-6*tof_arr**2
    iters = list(zip(tof_arr, Itof_arr))
    j = 0
    while(cmd.running):
        tof1, Itof1 = iters[j]
        cmd.set_var('tof', tof1)
        cmd.set_var('Itof', Itof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\nItof = %g\n'%(j+1, len(iters), tof1, Itof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
