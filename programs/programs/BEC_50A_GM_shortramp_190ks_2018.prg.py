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
    prg.add(200000000, "All Shutter Close 2017.sub")
    prg.add(200001490, "TTL2-12 ON")
    prg.add(200001500, "Config Field OFF.sub")
    prg.add(200004500, "MOT lights Off close.sub")
    prg.add(200005000, "Mirrors Imaging")
    prg.add(200006735, "Gray Molasses 2017")
    prg.add(200066735, "empty.sub")
    prg.add(200066735, "Loading_GM_Q50_MTC200A")
    prg.add(202191645, "B comp x", 860.0)
    prg.add(205000000, "All AOM On.sub")
    prg.add(220000000, "Evaporation Ramp.sub")
    prg.add(657003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(657010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(766310000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(767310000, "empty.sub")
    prg.add(767312000, "Pulse uw ON", enable=False)
    prg.add(767312020, "Pulse uw OFF", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 20ms")
    prg.add(767313020, "Picture Levit 2017 - 30ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 80ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 120ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(767313020, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(767313020, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(767323020, "Picture NaK.sub", functions=dict(time=lambda x: x + cmd.get_var('tof'), funct_enable=False), enable=False)
    prg.add(767323020, "Picture NaK no Rep.sub", enable=False)
    prg.add(767323020, "empty.sub", enable=False)
    prg.add(775323020, "Set MOT NaK.sub")
    prg.add(775823020, "Dark Spot MOT load.sub")
    prg.add(775923020, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(5, 20, 2)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
