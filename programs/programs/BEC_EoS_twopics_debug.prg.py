prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(12600000, "Synchronize.sub", enable=False)
    prg.add(17600000, "All Shutter Close 2017.sub")
    prg.add(17601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(17601500, "Config Field OFF.sub")
    prg.add(17604500, "MOT lights Off close.sub")
    prg.add(17605000, "Mirrors Imaging")
    prg.add(17606735, "Gray Molasses 2017")
    prg.add(17666735, "empty.sub")
    prg.add(17666735, "Loading_GM_Q50_MTC200A", enable=False)
    prg.add(19791645, "B comp x", 700.0)
    prg.add(20000000, "Bcomp y Sign Minus", enable=False)
    prg.add(22600000, "All AOM On.sub")
    prg.add(72600000, "Picture SetImaging")
    prg.add(72610000, "Picture SetRepumper")
    prg.add(77610000, "TTL2-12 ON")
    prg.add(77610010, "Pulse uw", polarity=1, pulse_t=0.00900, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('tau'), funct_enable=False))
    prg.add(77610110, "Picture NaK Ready no Rep Trig2.sub")
    prg.add(77611210, "Picture NaK Ready.sub")
    prg.add(85533350, "TTL2-12 OFF")
    prg.add(85633350, "Pulse uw OFF")
    prg.add(85634610, "Set MOT NaK.sub")
    prg.add(86133350, "Dark Spot MOT load.sub")
    prg.add(86233350, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(120, 200, 7)
    j = 0
    while(cmd.running):
        tau1 = iters[j]
        cmd.set_var('tau', tau1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntau = %g\n'%(j+1, len(iters), tau1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
