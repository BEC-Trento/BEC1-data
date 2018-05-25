prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(2200000, "Bx Grad OFF")
    prg.add(195000000, "Synchronize.sub", enable=False)
    prg.add(200000000, "All Shutter Close 2017.sub")
    prg.add(200001490, "TTL2-12 ON")
    prg.add(200001500, "Config Field OFF.sub")
    prg.add(200004500, "MOT lights Off close.sub")
    prg.add(200005000, "Mirrors Imaging")
    prg.add(200006735, "Gray Molasses 2017")
    prg.add(200066735, "empty.sub")
    prg.add(200066735, "Loading_GM_Q50_MTC200A")
    prg.add(202191645, "B comp x", 840.0)
    prg.add(205000000, "All AOM On.sub")
    prg.add(220000000, "Evaporation Ramp.sub", enable=False)
    prg.add(260001450, "Picture NaK.sub")
    prg.add(261006770, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(261013770, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(261014770, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(261014770, "Delta 1 Current ramp", start_t=0.0000, stop_x=30.000, n_points=300, start_x=50.000, stop_t=1000.0000, enable=False)
    prg.add(261024770, "empty.sub")
    prg.add(261024780, "TTL2-12 ON", enable=False)
    prg.add(261024780, "Bx Grad ON", enable=False)
    prg.add(261024780, "Bx Grad OFF", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 20ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(261024780, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(271024780, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(271524780, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(271524780, "Picture Stingray + Hamamatsu.sub", enable=False)
    prg.add(271524780, "Picture NaK no Rep.sub", enable=False)
    prg.add(271524780, "empty.sub", enable=False)
    prg.add(271724780, "Bx Grad OFF")
    prg.add(279724780, "Set MOT NaK.sub")
    prg.add(280224780, "Dark Spot MOT load.sub")
    prg.add(280324780, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.7, 1.15, 0.05)
    j = 0
    while(cmd.running):
        b1 = iters[j]
        cmd.set_var('b', b1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nb = %g\n'%(j+1, len(iters), b1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
