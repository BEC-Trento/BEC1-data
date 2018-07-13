prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(92600000, "Synchronize.sub", enable=False)
    prg.add(97600000, "All Shutter Close 2017.sub")
    prg.add(97601490, "Pulse TTL2-12", polarity=1, pulse_t=1.00000, enable=False)
    prg.add(97601500, "Config Field OFF.sub")
    prg.add(97604500, "MOT lights Off close.sub")
    prg.add(97605000, "Mirrors Imaging")
    prg.add(97606735, "Gray Molasses 2017")
    prg.add(97666735, "empty.sub")
    prg.add(97666735, "Loading_GM_Q50_MTC200A")
    prg.add(99791645, "B comp x", 733.0)
    prg.add(100000000, "Bcomp y Sign Minus", enable=False)
    prg.add(102600000, "All AOM On.sub")
    prg.add(117600000, "Evaporation Ramp.sub")
    prg.add(554603000, "Decompress Current 200-100", start_t=0.0000, stop_x=100.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(554610000, "Decompress Voltage 200-100", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(683820000, "empty.sub")
    prg.add(688820000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=100.000, stop_t=1200.0000)
    prg.add(688825000, "B comp x ramp", start_t=0, stop_x=860, n_points=200, start_x=733, stop_t=1200)
    prg.add(715825000, "Picture SetImaging", enable=False)
    prg.add(715825000, "Picture MOT beams SetImaging")
    prg.add(715835000, "Picture SetRepumper")
    prg.add(715845000, "Mirrors Imaging Bragg")
    prg.add(715845000, "Picture SetRepumper2", enable=False)
    prg.add(722856395, "Pulse Trig Extra Hamamatsu", polarity=1, pulse_t=0.10000)
    prg.add(723855000, "Pulse TTL2-12", polarity=1, pulse_t=0.01540)
    prg.add(723856235, "Pulse uw", polarity=1, pulse_t=0.01200)
    prg.add(723856235, "Pulse Repumper MOT", polarity=1, pulse_t=0.15000, enable=False)
    prg.add(723856396, "Picture NaK Ready no Rep.sub", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('t_rep'), funct_enable=False))
    prg.add(723857596, "Picture Levit 2017 - setup")
    prg.add(723858596, "Delta 1 Current", 13.000)
    prg.add(723998596, "IGBT 4 Open")
    prg.add(724008596, "Pulse Repumper MOT", polarity=1, pulse_t=0.15000)
    prg.add(724010206, "Picture NaK Ready MOT beams no Rep Trig2.sub")
    prg.add(724298396, "Config Field OFF.sub")
    prg.add(732733380, "TTL2-12 OFF")
    prg.add(732833380, "Pulse uw OFF")
    prg.add(732834640, "Set MOT NaK.sub")
    prg.add(733333380, "Dark Spot MOT load.sub")
    prg.add(733433380, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.asarray([1.3, 2.8, 7.6, 22.7, 70.3, ])
    j = 0
    while(cmd.running):
        tprobe1 = iters[j]
        cmd.set_var('tprobe', tprobe1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntprobe = %g\n'%(j+1, len(iters), tprobe1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
