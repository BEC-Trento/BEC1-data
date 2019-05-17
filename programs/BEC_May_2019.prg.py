prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON")
    prg.add(100104000, "MOT lights Off TTL.sub")
    prg.add(100104200, "Config Field OFF.sub")
    prg.add(100105300, "Scope 2 Trigger ON")
    prg.add(100105900, "Gray Molasses 2017")
    prg.add(100156899, "Load_Quad")
    prg.add(100166899, "Quad_RampUP")
    prg.add(105166899, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(110000000, "Scope 2 Trigger OFF")
    prg.add(110010000, "Scope 1 Trigger OFF")
    prg.add(110167000, "Evaporation ramp", start_t=0.0000, func_args="fstart=45e6, fend=25e6, tau=1", n_points=500, func="(fstart - fend)*exp(-t/tau) + fend", stop_t=5000.0000, functions=dict(func_args=lambda x: 'fstart={}, fend={}, tau={}'.format(cmd.get_var('f_evap_start'), cmd.get_var('f_evap_end'), cmd.get_var('evap_tau'))))
    prg.add(110167000, "Evaporation linear ramp", start_t=0.0000, stop_x=10000000.0000, n_points=500, start_x=36000000.0000, stop_t=5000.0000, functions=dict(stop_t=lambda x: cmd.get_var('linear_evap_time')), enable=False)
    prg.add(125166899, "Quad_RampDOWN", functions=dict(time=lambda x: 10515.6899+cmd.get_var('QuadRampTime') + +cmd.get_var('linear_evap_time')))
    prg.add(127167899, "Config Field OFF.sub", functions=dict(time=lambda x: 10716.6899+cmd.get_var('QuadRampTime')+cmd.get_var('linear_evap_time')))
    prg.add(127217899, "BEC_imaging", functions=dict(time=lambda x: 10715.6899+cmd.get_var('QuadRampTime')+cmd.get_var('tof')+cmd.get_var('linear_evap_time')))
    prg.add(133741899, "DarkSpotMOT_19.sub", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 15, 1)
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
