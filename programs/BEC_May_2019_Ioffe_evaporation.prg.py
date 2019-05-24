prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON")
    prg.add(199943111, "MOT lights Off TTL.sub")
    prg.add(199947301, "Config Field OFF.sub")
    prg.add(199949001, "Gray Molasses 2017")
    prg.add(199980000, "Scope 1 Trigger OFF")
    prg.add(199985000, "Scope 2 Trigger ON")
    prg.add(199986000, "Scope 2 Trigger OFF")
    prg.add(200000000, "Load_Quad")
    prg.add(200030000, "Evaporation ramp", start_t=0.0000, func_args="fstart=40e6, fend=4e6, tau=3", n_points=500, func="(fstart - fend)*exp(-t/tau) + fend", stop_t=5000.0000, functions=dict(func_args=lambda x: 'fstart={}, fend={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(200040000, "Evaporation ramp", start_t=0.0000, func_args="fstart=4e6, fend=2e6, tau=2", n_points=500, func="(fstart - fend)*exp(-t/tau) + fend", stop_t=5000.0000, functions=dict(func_args=lambda x: 'fstart={}, fend={}, tau={}'.format(cmd.get_var('evap2_fstart')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: 20000.1 + cmd.get_var('evap1_time')))
    prg.add(205000000, "Ramp_bias_down.sub")
    prg.add(210000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(230000000, "Quad_RampDOWN", functions=dict(time=lambda x: 20000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')*0))
    prg.add(232001000, "Config Field OFF.sub", functions=dict(time=lambda x: 20000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown_time')*0+cmd.get_var('hold_time')))
    prg.add(232051000, "BEC_imaging", functions=dict(time=lambda x: 20000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown_time')*0+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(258575000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: 20000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown_time')*0+cmd.get_var('hold_time')+cmd.get_var('tof')+1000))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(20, 30, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        evap1_fstart1 = iters[j]
        cmd.set_var('evap1_fstart', evap1_fstart1)
        print('\n')
        print('Run #%d/%d, with variables:\nevap1_fstart = %g\n'%(j+1, len(iters), evap1_fstart1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
