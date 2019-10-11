prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(109943111, "MOT lights Off TTL.sub")
    prg.add(109956301, "Config Field OFF.sub")
    prg.add(109958001, "Gray Molasses 2017")
    prg.add(109994000, "Scope 2 Trigger ON")
    prg.add(109994100, "Scope 2 Trigger OFF")
    prg.add(110054100, "Setup_imaging_GM")
    prg.add(110054100, "BEC_imaging_ready", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(120003200, "DarkSpotMOT_19.sub", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = [100, 200, 400, 600, 800, 1000]
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        push_amp1 = iters[j]
        cmd.set_var('push_amp', push_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\npush_amp = %g\n'%(j+1, len(iters), push_amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
