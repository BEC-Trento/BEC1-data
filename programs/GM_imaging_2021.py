prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(100000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(100001000, "MOT lights Off TTL pre-imaging.sub")
    prg.add(100001190, "Config Field OFF.sub")
    prg.add(100002890, "Gray Molasses 2017")
    prg.add(100055890, "Scope 2 Trigger Pulse", polarity=1, pulse_t=2.00000)
    prg.add(100146909, "Setup_imaging_MOT")
    prg.add(100150028, "BEC_imaging")
    prg.add(101150028, "EMPTY")
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
