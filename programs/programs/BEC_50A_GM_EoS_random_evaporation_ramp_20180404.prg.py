prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(192390000, "Synchronize.sub", enable=False)
    prg.add(197390000, "All Shutter Close 2017.sub")
    prg.add(197391490, "TTL2-12 ON")
    prg.add(197391500, "Config Field OFF.sub")
    prg.add(197394500, "MOT lights Off close.sub")
    prg.add(197395000, "Mirrors Imaging")
    prg.add(197396735, "Gray Molasses 2017")
    prg.add(197456735, "empty.sub")
    prg.add(197456735, "Loading_GM_Q50_MTC200A")
    prg.add(199580000, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(199581645, "B comp x", 915.0)
    prg.add(202390000, "All AOM On.sub")
    prg.add(217390000, "Evaporation Ramp.sub")
    prg.add(367393000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(367400000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(373400000, "empty.sub")
    prg.add(388400000, "TTL2-12 ON")
    prg.add(388410000, "Pulse uw ON", enable=False)
    prg.add(388410074, "Pulse uw OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(388411074, "Picture NaK no Rep Trig2.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(388411074, "Picture NaK Trig 2.sub", enable=False)
    prg.add(390411074, "Picture Levit 2017 - 50ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False))
    prg.add(390411074, "Picture Levit 2017 - 65ms", enable=False)
    prg.add(390411074, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(390411074, "Picture Levit 2017 - 120ms", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(390411074, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(392210074, "TTL2-12 ON", enable=False)
    prg.add(393410974, "Picture NaK Trig12.sub", enable=False)
    prg.add(393410974, "Picture NaK.sub", enable=False)
    prg.add(401429614, "TTL2-12 OFF")
    prg.add(401529614, "Pulse uw OFF")
    prg.add(401530874, "Set MOT NaK.sub")
    prg.add(402029614, "Dark Spot MOT load.sub")
    prg.add(402129614, "Config MOT.sub")
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
