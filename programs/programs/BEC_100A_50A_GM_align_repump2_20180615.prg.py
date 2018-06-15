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
    prg.add(199791645, "B comp x", 745.0)
    prg.add(200000000, "Bcomp y Sign Minus", enable=False)
    prg.add(202600000, "All AOM On.sub")
    prg.add(217600000, "Evaporation Ramp.sub")
    prg.add(654603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(654610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(751180000, "empty.sub")
    prg.add(756180000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(756185000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=745, stop_t=1200)
    prg.add(773685000, "Shutter Repump2 Open")
    prg.add(773695000, "Shutter 3DMOT cool Na Close")
    prg.add(775695000, "Picture SetImaging")
    prg.add(775705000, "Picture SetRepumper")
    prg.add(780705000, "TTL2-12 ON")
    prg.add(780705100, "Picture Levit 2017 - setup")
    prg.add(780706100, "Delta 1 Current", 13.000)
    prg.add(781196100, "IGBT 4 Open")
    prg.add(781201100, "Pulse Repumper MOT", polarity=1, pulse_t=0.40000)
    prg.add(781206100, "Picture NaK Ready.sub", enable=False)
    prg.add(781206100, "Picture NaK Ready no Rep.sub")
    prg.add(789128240, "TTL2-12 OFF")
    prg.add(789228240, "Pulse uw OFF")
    prg.add(789229500, "Set MOT NaK.sub")
    prg.add(789728240, "Dark Spot MOT load.sub")
    prg.add(789828240, "Config MOT.sub")
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
