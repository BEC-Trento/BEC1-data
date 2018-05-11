prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(192600000, "Synchronize.sub", enable=False)
    prg.add(197600000, "All Shutter Close 2017.sub")
    prg.add(197601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(197601500, "Config Field OFF.sub")
    prg.add(197604500, "MOT lights Off close.sub")
    prg.add(197605000, "Mirrors Imaging")
    prg.add(197606735, "Gray Molasses 2017")
    prg.add(197666735, "empty.sub")
    prg.add(197666735, "Loading_GM_Q50_MTC200A")
    prg.add(199791645, "B comp x", 685.0)
    prg.add(200000000, "Bcomp y Sign Minus", enable=False)
    prg.add(202600000, "All AOM On.sub")
    prg.add(217600000, "Evaporation Ramp.sub")
    prg.add(654603000, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(654609000, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(654610000, "Delta 1 Voltage ramp", start_t=0.0000, stop_x=15.000, n_points=300, start_x=30.000, stop_t=600.0000, enable=False)
    prg.add(761900000, "empty.sub")
    prg.add(766900000, "B comp x ramp", start_t=0, stop_x=790, n_points=100, start_x=925, stop_t=1000, enable=False)
    prg.add(766905000, "B comp y ramp", start_t=0, stop_x=2.5, n_points=100, start_x=0, stop_t=1000, functions=dict(stop_x=lambda x: cmd.get_var('by'), funct_enable=False), enable=False)
    prg.add(766910000, "B comp z ramp", start_t=0.0000, stop_x=2.500, n_points=100, start_x=0.940, stop_t=1000.0000, enable=False)
    prg.add(776910000, "Picture SetImaging")
    prg.add(776920000, "Picture SetRepumper")
    prg.add(781920000, "TTL2-12 ON")
    prg.add(781930000, "Pulse uw", polarity=1, pulse_t=0.04000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('tau'), funct_enable=False))
    prg.add(782000000, "Picture NaK Ready no Rep Trig2.sub")
    prg.add(782000000, "Picture NaK Ready Trig 2.sub", enable=False)
    prg.add(782002500, "Picture Levit 2017 - setup")
    prg.add(782004500, "Delta 1 Current", 13.500)
    prg.add(782994500, "IGBT 4 Open")
    prg.add(783004500, "Picture NaK Ready.sub")
    prg.add(790926640, "TTL2-12 OFF")
    prg.add(791026640, "Pulse uw OFF")
    prg.add(791027900, "Set MOT NaK.sub")
    prg.add(791526640, "Dark Spot MOT load.sub")
    prg.add(791626640, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(4, 60, 4)
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
