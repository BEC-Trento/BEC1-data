prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(500, "Config Field OFF.sub")
    prg.add(1500000, "Set MOT NaK.sub")
    prg.add(2000000, "Dark Spot MOT load.sub")
    prg.add(2100000, "Config MOT.sub")
    prg.add(65000000, "Synchronize.sub", enable=False)
    prg.add(70000000, "All Shutter Close 2017.sub")
    prg.add(70000490, "TTL2-12 ON")
    prg.add(70000500, "Config Field OFF.sub")
    prg.add(70002500, "MOT lights Off close.sub")
    prg.add(70003500, "Mirrors Imaging", enable=False)
    prg.add(70004000, "Gray Molasses 2017")
    prg.add(70064000, "empty.sub")
    prg.add(70064000, "Loading_GM_Q50_MTC200A")
    prg.add(72188910, "B comp x", 735.0, enable=False)
    prg.add(74997265, "All AOM On.sub")
    prg.add(76997265, "empty.sub", enable=False)
    prg.add(77997265, "TTL2-12 OFF")
    prg.add(93897265, "Set MOT NaK.sub")
    prg.add(94397265, "Dark Spot MOT load.sub")
    prg.add(94497265, "Config MOT.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.2, 3, 0.2)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
