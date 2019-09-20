prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(99943111, "MOT lights Off TTL.sub")
    prg.add(99956301, "Config Field OFF.sub")
    prg.add(99958001, "Gray Molasses 2017")
    prg.add(99994000, "Scope 2 Trigger ON")
    prg.add(99994100, "Scope 2 Trigger OFF")
    prg.add(100054100, "Setup_imaging_GM")
    prg.add(100054100, "BEC_imaging_ready", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(110003200, "DarkSpotMOT_19.sub", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 11, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
