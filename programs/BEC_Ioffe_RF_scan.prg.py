prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(209943111, "MOT lights Off TTL.sub")
    prg.add(209947301, "Config Field OFF.sub")
    prg.add(209949001, "Gray Molasses 2017")
    prg.add(209949001, "Optical pumping", enable=False)
    prg.add(209975000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')))
    prg.add(209985000, "Scope 2 Trigger ON")
    prg.add(209986000, "Scope 2 Trigger OFF")
    prg.add(209999990, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')))
    prg.add(209999990, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+.15))
    prg.add(210000000, "Load_Quad")
    prg.add(210000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')))
    prg.add(210000000, "Pulse uw ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')))
    prg.add(210000000, "Pulse uw OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(210000000, "RF pulse ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')), enable=False)
    prg.add(210000000, "RF pulse OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+1e-3*cmd.get_var('RF_pulsetime')), enable=False)
    prg.add(210000000, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('hold_time_2')))
    prg.add(210000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('tof')), enable=False)
    prg.add(210010000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('tof')), enable=False)
    prg.add(210020000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('hold_time_2')))
    prg.add(210020000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    prg.add(210030000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    prg.add(210030000, "Quad_RampUP")
    prg.add(210045000, "Evaporation amp", 1000)
    prg.add(210050000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(210060000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_time')*1e-3, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: x +cmd.get_var('evap1_time')))
    prg.add(210064000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')))
    prg.add(210065000, "RF pulse amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')), enable=False)
    prg.add(210065000, "Evaporation amp", 1, functions=dict(time=lambda x: x + cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(210066000, "RF pulse freq", 0.0000, functions=dict(frequency=lambda x: cmd.get_var('RF_freq')), enable=False)
    prg.add(210070000, "Mirrors Imaging")
    prg.add(215020000, "Ramp_bias_down.sub")
    prg.add(220010000, "RF pulse amp", 0, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('tof')), enable=False)
    prg.add(220020000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(220020000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('tof')), enable=False)
    prg.add(220030000, "Na Push (+) freq", 60.00)
    prg.add(220035000, "Na Probe/Push (-) freq", 60.00)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.77e+09, 1.7707e+09, 30000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        marconi1_freq = iters[j]
        cmd.set_var('marconi1_freq', marconi1_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nmarconi1_freq = %g\n'%(j+1, len(iters), marconi1_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
