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
    prg.add(756220000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=400, start_x=100.000, stop_t=4500.0000)
    prg.add(756230000, "B comp x ramp", start_t=0, stop_x=6000, n_points=400, start_x=665, stop_t=4500)
    prg.add(811230000, "empty.sub")
    prg.add(811231560, "Pulse TTL2-12", polarity=1, pulse_t=0.10000)
    prg.add(811232260, "TTL0-13 broken OFF", enable=False)
    prg.add(811232260, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(811232260, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(811232260, "Picture Levit 2017 - 80ms")
    prg.add(811232260, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(811232260, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(811232260, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(811232260, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(811237260, "B comp x", 750.0)
    prg.add(811237260, "Picture NaK short delay.sub", enable=False)
    prg.add(811267260, "Config Field OFF.sub", enable=False)
    prg.add(811272260, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(811302260, "Config Field OFF.sub", enable=False)
    prg.add(827042685, "Set MOT NaK.sub")
    prg.add(827542685, "Dark Spot MOT load.sub")
    prg.add(827642685, "Config MOT.sub")
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
