prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(159000000, "Synchronize.sub", enable=False)
    prg.add(159249001, "Scope 2 Trigger ON")
    prg.add(159299001, "Scope 2 Trigger OFF")
    prg.add(159943111, "MOT lights Off TTL.sub")
    prg.add(159947301, "Config Field OFF.sub")
    prg.add(159949001, "Gray Molasses 2017")
    prg.add(160249001, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(160249001, "DarkSpotMOT_19.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(550, 701, 50)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        DS_amp = iters[j]
        cmd.set_var('DS_amp', DS_amp)
        print('\n')
        print('Run #%d/%d, with variables:\nDS_amp = %g\n'%(j+1, len(iters), DS_amp))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
