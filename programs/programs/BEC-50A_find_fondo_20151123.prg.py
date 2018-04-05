prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(10, "Initialize 0 TTL and Synchronize.sub")
    prg.add(500, "Config Field OFF.sub", enable=False)
    prg.add(11000, "TTL3-11 ON")
    prg.add(41000, "Optical Levit (-) Amp", 1000)
    prg.add(61000, "RFO1 Amp", 0)
    prg.add(91000, "B comp y", 0.0000)
    prg.add(101000, "IGBT B comp y ON")
    prg.add(491000, "Bcomp y Sign Plus", enable=False)
    prg.add(1491000, "Set MOT NaK.sub")
    prg.add(1991000, "Dark Spot MOT load.sub")
    prg.add(2091000, "Config MOT.sub")
    prg.add(9000000, "Optical Levit ON")
    prg.add(10000000, "Synchronize.sub", enable=False)
    prg.add(200000000, "Melassa Na.sub")
    prg.add(200001000, "Melassa Na amp.sub")
    prg.add(200001550, "Config Field OFF.sub")
    prg.add(200049550, "MOT lights Off.sub")
    prg.add(200053550, "Delta 1 Current", 200.000)
    prg.add(200053560, "Delta 2 Voltage", 30.0000)
    prg.add(200053570, "Config MT compr.sub")
    prg.add(202057590, "All Shutter Close.sub")
    prg.add(205059590, "Mirrors Imaging")
    prg.add(205559590, "IGBT B comp x ON")
    prg.add(206059590, "All AOM On.sub")
    prg.add(209059589, "B comp x", 945.0)
    prg.add(210001629, "Evaporation Ramp.sub")
    prg.add(647004629, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=150, start_x=200.000, stop_t=600.0000)
    prg.add(647011629, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=30.000, stop_t=600.0000)
    prg.add(754301629, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(754301764, "TTL2-12 ON")
    prg.add(754311629, "Picture NaK.sub", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(754311629, "Picture Levit 2017 - 50ms", enable=False)
    prg.add(754311629, "Picture Levit 2017 - 100ms", enable=False)
    prg.add(754311629, "Picture Levit 2017 - 150ms")
    prg.add(754311629, "Picture Levit 20170908.sub", enable=False)
    prg.add(754311629, "Config Field OFF.sub", enable=False)
    prg.add(754311764, "TTL2-12 OFF")
    prg.add(754321629, "Picture NaK.sub", enable=False)
    prg.add(762111669, "Bx Grad OFF")
    prg.add(762211669, "Set MOT NaK.sub")
    prg.add(762711669, "Dark Spot MOT load.sub")
    prg.add(762811669, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(3000, 5001, 500)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
