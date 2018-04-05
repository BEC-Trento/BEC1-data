prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(1501000, "TTL Pinning OFF")
    prg.add(2001000, "Dark Spot MOT load.sub")
    prg.add(2101000, "Config MOT.sub")
    prg.add(115001000, "Synchronize.sub", enable=False)
    prg.add(120001000, "All Shutter Close 2017.sub")
    prg.add(120002490, "TTL2-12 ON")
    prg.add(120002500, "Config Field OFF.sub")
    prg.add(120005500, "MOT lights Off close.sub")
    prg.add(120006000, "Mirrors Imaging")
    prg.add(120007735, "Gray Molasses 2017")
    prg.add(120067735, "empty.sub")
    prg.add(120067735, "Loading_GM_Q50_MTC200A")
    prg.add(122192645, "B comp x", 955.0)
    prg.add(122193645, "TTL Pinning ON")
    prg.add(122193655, "Pinning Lock", 9.0000)
    prg.add(140002010, "Evaporation Ramp.sub")
    prg.add(577005010, "Decompress Current 200-50", start_t=0.0000, stop_x=50.000, n_points=300, start_x=200.000, stop_t=600.0000)
    prg.add(577012010, "Decompress Voltage 200-50", start_t=0.0000, stop_x=0.000, n_points=300, start_x=30.000, stop_t=600.0000)
    prg.add(684310010, "TTL2-12 OFF", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False))
    prg.add(684310020, "TTL Pinning OFF")
    prg.add(684310030, "Pinning Lock", 0.0000)
    prg.add(684312030, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('t'), funct_enable=False), enable=False)
    prg.add(684312030, "Picture Levit 2017 - 15ms", enable=False)
    prg.add(684312030, "Picture Levit 2017 - 50ms")
    prg.add(684312030, "Picture Levit 2017 - 150ms", enable=False)
    prg.add(684312030, "Picture Levit 2017 - 180ms", enable=False)
    prg.add(684312030, "Picture Levit 2017 - 200ms", enable=False)
    prg.add(684322030, "Picture NaK.sub", enable=False)
    prg.add(684322030, "empty.sub", enable=False)
    prg.add(692322030, "Set MOT NaK.sub")
    prg.add(692822030, "Dark Spot MOT load.sub")
    prg.add(692922030, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(202, 302, 2)
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
