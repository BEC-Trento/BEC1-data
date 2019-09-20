prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(159943111, "MOT lights Off TTL.sub")
    prg.add(159947301, "Config Field OFF.sub")
    prg.add(159949001, "Gray Molasses 2017")
    prg.add(159949001, "Optical pumping", enable=False)
    prg.add(159985000, "Scope 2 Trigger ON")
    prg.add(159986000, "Scope 2 Trigger OFF")
    prg.add(160000000, "Load_Quad")
    prg.add(160000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')))
    prg.add(160000000, "Pulse uw Ramp", start_t=0.0000, stop_x=0.0000, n_points=1, start_x=1.0000, stop_t=400.0000, functions=dict(stop_x=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime'), start_x=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')))
    prg.add(160000000, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(160030000, "Quad_RampUP")
    prg.add(160050000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(160060000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_time')*1e-3, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: x +cmd.get_var('evap1_time')))
    prg.add(160064000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')+cmd.get_var('evap2_time')*0))
    prg.add(160070000, "Mirrors Imaging")
    prg.add(161000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(161010000, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(162000000, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.10000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(165020000, "Ramp_bias_down.sub")
    prg.add(170020000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(170020000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.7687e+09, 1.7688e+09, 15000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        marconi1_freq1 = iters[j]
        cmd.set_var('marconi1_freq', marconi1_freq1)
        print('\n')
        print('Run #%d/%d, with variables:\nmarconi1_freq = %g\n'%(j+1, len(iters), marconi1_freq1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
