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
    prg.add(202191645, "B comp x", 923.0)
    prg.add(205000000, "All AOM On.sub")
    prg.add(220000000, "Evaporation Ramp.sub")
    prg.add(394003000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(394010000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(478310000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(479310000, "empty.sub")
    prg.add(479310000, "Pulse uw ON")
    prg.add(479310080, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False))
    prg.add(479311280, "Picture Levit 2017 - 10ms")
    prg.add(479382280, "Picture NaK no Rep Trig2.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(479382280, "Picture NaK Trig 2.sub", enable=False)
    prg.add(484382280, "Config Field OFF.sub", enable=False)
    prg.add(484382280, "Picture Levit 2017 - 120ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(484392280, "Picture NaK Trig12.sub", enable=False)
    prg.add(484392280, "Picture NaK.sub", enable=False)
    prg.add(492392280, "Set MOT NaK.sub")
    prg.add(492892280, "Dark Spot MOT load.sub")
    prg.add(492992280, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(150, 200, 3)
    j = 0
    while(cmd.running):
        t1 = iters[j]
        cmd.set_var('t', t1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nt = %g\n'%(j+1, len(iters), t1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
