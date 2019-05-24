prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON")
    prg.add(99937101, "MOT lights Off TTL.sub")
    prg.add(99937301, "Config Field OFF.sub")
    prg.add(99939001, "Gray Molasses 2017")
    prg.add(99990000, "Load_Quad")
    prg.add(100000000, "Quad_RampUP")
    prg.add(105000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(109843101, "Scope 1 Trigger OFF")
    prg.add(110000101, "Evaporation ramp", start_t=0.0000, func_args="fstart=40e6, fend=20e6, tau=0.4", n_points=500, func="(fstart - fend)*exp(-t/tau) + fend", stop_t=5000.0000, functions=dict(stop_t=lambda x: cmd.get_var('evap1_time'), time=lambda x: 10000+cmd.get_var('QuadRampTime')))
    prg.add(110000101, "Evaporation ramp", start_t=0.0000, func_args="fstart=20e6, fend=5e6, tau=2", n_points=500, func="(fstart - fend)*exp(-t/tau) + fend", stop_t=5000.0000, functions=dict(stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: 10000.02 + cmd.get_var('QuadRampTime') + cmd.get_var('evap1_time')), enable=False)
    prg.add(125000000, "Quad_RampDOWN", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime') +cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap_wait_time')))
    prg.add(126000101, "ConfigMOT_to_Ioffe.sub", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime') +cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap_wait_time')+cmd.get_var('Quad_rampdown_time')), enable=False)
    prg.add(127001000, "Config Field OFF.sub", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime')+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap_wait_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('ioffe_wait_time')))
    prg.add(127051000, "BEC_imaging", functions=dict(time=lambda x: 10000+cmd.get_var('QuadRampTime')+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap_wait_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('ioffe_wait_time')+cmd.get_var('tof')))
    prg.add(153575000, "DarkSpotMOT_19.sub")
    prg.add(159980000, "Scope 2 Trigger ON")
    prg.add(170010000, "Scope 2 Trigger OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 12, 1)
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
