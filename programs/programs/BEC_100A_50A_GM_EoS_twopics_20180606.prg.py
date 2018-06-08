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
    prg.add(107601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(107601500, "Config Field OFF.sub")
    prg.add(107604500, "MOT lights Off close.sub")
    prg.add(107605000, "Mirrors Imaging")
    prg.add(107606735, "Gray Molasses 2017")
    prg.add(107666735, "empty.sub")
    prg.add(107666735, "Loading_GM_Q50_MTC200A")
    prg.add(109791645, "B comp x", 700.0)
    prg.add(110000000, "Bcomp y Sign Minus", enable=False)
    prg.add(112600000, "All AOM On.sub")
    prg.add(127600000, "Evaporation Ramp.sub")
    prg.add(564603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(564610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(693820000, "empty.sub")
    prg.add(698820000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=150, start_x=100.000, stop_t=600.0000)
    prg.add(698825000, "B comp x ramp", start_t=0, stop_x=860, n_points=150, start_x=700, stop_t=600)
    prg.add(708825000, "Picture SetImaging")
    prg.add(708835000, "Picture SetRepumper")
    prg.add(713835000, "TTL2-12 ON")
    prg.add(713835010, "Pulse uw", polarity=1, pulse_t=0.00900, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('tau'), funct_enable=False))
    prg.add(713835110, "Picture NaK Ready no Rep Trig2.sub")
    prg.add(713835110, "Picture NaK Ready Trig 2.sub", enable=False)
    prg.add(713836210, "Picture NaK Ready.sub")
    prg.add(721758350, "TTL2-12 OFF")
    prg.add(721858350, "Pulse uw OFF")
    prg.add(721859610, "Set MOT NaK.sub")
    prg.add(722358350, "Dark Spot MOT load.sub")
    prg.add(722458350, "Config MOT.sub")
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
