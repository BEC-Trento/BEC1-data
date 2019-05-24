prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON")
    prg.add(92938111, "MOT lights Off TTL.sub")
    prg.add(92942301, "Config Field OFF.sub")
    prg.add(92944001, "Gray Molasses 2017")
    prg.add(92995000, "Load_Quad")
    prg.add(93485000, "Scope 2 Trigger ON")
    prg.add(94995000, "ConfigMOT_to_Ioffe.sub", enable=False)
    prg.add(100000000, "Quad_RampUP", enable=False)
    prg.add(105000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(109843101, "Scope 1 Trigger OFF", enable=False)
    prg.add(125000000, "Quad_RampDOWN", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime') +cmd.get_var('evap_wait_time')))
    prg.add(127001000, "Config Field OFF.sub", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime')+cmd.get_var('evap_wait_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('ioffe_wait_time')))
    prg.add(127051000, "BEC_imaging", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime')+cmd.get_var('evap_wait_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('ioffe_wait_time')+cmd.get_var('tof')))
    prg.add(140010000, "Scope 2 Trigger OFF")
    prg.add(153575000, "DarkSpotMOT_19.sub")
    return prg
def commands(cmd):
    import numpy as np
    tof_arr = np.arange(1, 14, 1)
    probe_det_arr = np.arange(13, 0, -1)
    iters = list(zip(tof_arr, probe_det_arr))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1, probe_det1 = iters[j]
        cmd.set_var('tof', tof1)
        cmd.set_var('probe_det', probe_det1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\nprobe_det = %g\n'%(j+1, len(iters), tof1, probe_det1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
