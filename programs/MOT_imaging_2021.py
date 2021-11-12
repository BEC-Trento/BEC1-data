prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(200000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(200000000, "Synchronize.sub", enable=False)
    prg.add(200930000, "MOT lights Off TTL.sub", enable=False)
    prg.add(200930000, "MOT lights Off TTL pre-imaging.sub")
    prg.add(200930190, "Config Field OFF.sub")
    prg.add(200930289, "Scope 2 Trigger Pulse", polarity=1, pulse_t=2.00000)
    prg.add(200931308, "Setup_imaging_MOT")
    prg.add(200932190, "Gray Molasses 2017")
    prg.add(200935309, "BEC_imaging", enable=False)
    prg.add(201088889, "Setup_imaging_MOT")
    prg.add(201091889, "BEC_imaging")
    prg.add(201291889, "open_probe", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 10, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        repeat = iters[j]
        cmd.set_var('repeat', repeat)
        print('\n')
        print('Run #%d/%d, with variables:\nrepeat = %g\n'%(j+1, len(iters), repeat))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
