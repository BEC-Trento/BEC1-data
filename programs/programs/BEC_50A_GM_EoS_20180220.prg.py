prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(102600000, "Synchronize.sub", enable=False)
    prg.add(107600000, "All Shutter Close 2017.sub")
    prg.add(107601490, "TTL2-12 ON")
    prg.add(107601500, "Config Field OFF.sub")
    prg.add(107604500, "MOT lights Off close.sub")
    prg.add(107605000, "Mirrors Imaging")
    prg.add(107606735, "Gray Molasses 2017")
    prg.add(107666735, "empty.sub")
    prg.add(107666735, "Loading_GM_Q50_MTC200A")
    prg.add(109790000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(109791645, "B comp x", 915.0)
    prg.add(112600000, "All AOM On.sub")
    prg.add(127600000, "Evaporation Ramp.sub")
    prg.add(564603000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(564610000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(598860000, "empty.sub")
    prg.add(603850000, "TTL2-12 ON")
    prg.add(603860000, "Pulse uw ON", enable=False)
    prg.add(603860147, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(603861147, "Picture NaK no Rep Trig2.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(603861147, "Picture NaK Trig 2.sub")
    prg.add(604161147, "Config Field OFF.sub")
    prg.add(609161147, "Picture Levit 2017 - 50ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False))
    prg.add(609161147, "Picture Levit 2017 - 65ms", enable=False)
    prg.add(609161147, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(609161147, "Picture Levit 2017 - 120ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(609161147, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(610960147, "TTL2-12 ON", enable=False)
    prg.add(612161047, "Picture NaK Trig12.sub", enable=False)
    prg.add(612161047, "Picture NaK.sub", enable=False)
    prg.add(620179687, "TTL2-12 OFF")
    prg.add(620279687, "Pulse uw OFF")
    prg.add(620280947, "Set MOT NaK.sub")
    prg.add(620779687, "Dark Spot MOT load.sub")
    prg.add(620879687, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 20, 3)
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
