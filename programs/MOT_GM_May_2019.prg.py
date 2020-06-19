prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(152943111, "MOT lights Off TTL.sub", enable=False)
    prg.add(152943111, "MOT lights Off TTL_GM.sub")
    prg.add(152945000, "Config Field OFF.sub")
    prg.add(152958001, "Gray Molasses 2017")
    prg.add(152958012, "Scope 2 Trigger ON")
    prg.add(152958112, "Scope 2 Trigger OFF")
    prg.add(153010257, "Setup_imaging_GM")
    prg.add(153010257, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(153010267, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(153016947, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(162966047, "DarkSpotMOT_19.sub", enable=False)
    prg.add(163266047, "open_probe")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 10, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof = iters[j]
        cmd.set_var('tof', tof)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
