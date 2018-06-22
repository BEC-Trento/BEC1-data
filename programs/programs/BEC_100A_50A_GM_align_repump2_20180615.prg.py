prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(82600000, "Synchronize.sub", enable=False)
    prg.add(87600000, "All Shutter Close 2017.sub")
    prg.add(87601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(87601500, "Config Field OFF.sub")
    prg.add(87604500, "MOT lights Off close.sub")
    prg.add(87605000, "Mirrors Imaging")
    prg.add(87606735, "Gray Molasses 2017")
    prg.add(87666735, "empty.sub")
    prg.add(87666735, "Loading_GM_Q50_MTC200A")
    prg.add(89791645, "B comp x", 745.0)
    prg.add(90000000, "Bcomp y Sign Minus", enable=False)
    prg.add(92600000, "All AOM On.sub")
    prg.add(107600000, "Evaporation Ramp.sub")
    prg.add(207600000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(207607000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(219607000, "empty.sub")
    prg.add(224607000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(224612000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=745, stop_t=1200)
    prg.add(264612000, "Picture SetImaging")
    prg.add(264622000, "Picture SetRepumper")
    prg.add(264622000, "Picture SetRepumper2", enable=False)
    prg.add(264722000, "Na Repumper2 (+) Amp", 1000)
    prg.add(269722000, "Config Field OFF.sub")
    prg.add(269730900, "Pulse TTL2-12", polarity=1, pulse_t=0.01540, enable=False)
    prg.add(269731000, "TTL Repumper MOT ON")
    prg.add(269732500, "TTL Repumper MOT OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(269732610, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(269732610, "Picture Levit 2017 - setup", enable=False)
    prg.add(269733610, "Delta 1 Current", 13.200, enable=False)
    prg.add(270523610, "IGBT 4 Open", enable=False)
    prg.add(270533510, "Pulse TTL2-12", polarity=1, pulse_t=0.01560, enable=False)
    prg.add(270533644, "Picture NaK Ready - high intensity.sub", enable=False)
    prg.add(278455784, "TTL2-12 OFF")
    prg.add(278555784, "Pulse uw OFF")
    prg.add(278557044, "Set MOT NaK.sub")
    prg.add(279055784, "Dark Spot MOT load.sub")
    prg.add(279155784, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-80, -35, 5)
    j = 0
    while(cmd.running):
        freq1 = iters[j]
        cmd.set_var('freq', freq1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nfreq = %g\n'%(j+1, len(iters), freq1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
