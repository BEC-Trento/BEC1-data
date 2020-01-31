prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "open_probe_z")
    prg.add(209000000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(209943111, "MOT lights Off TTL.sub")
    prg.add(209947301, "Config Field OFF.sub")
    prg.add(209949001, "Gray Molasses 2017")
    prg.add(209949001, "Optical pumping", enable=False)
    prg.add(209949011, "Scope 2 Trigger ON")
    prg.add(209986000, "Scope 2 Trigger OFF")
    prg.add(210000000, "Load_Quad")
    prg.add(210010000, "Quad_RampUP")
    prg.add(210060000, "Mirrors Imaging")
    prg.add(215000000, "Ramp_bias_down.sub")
    prg.add(216000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(220000000, "Number_lock", enable=False)
    prg.add(230000000, "Evaporation_quad_rampdown_3ramps")
    prg.add(230000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time') - 0.00123))
    prg.add(230000000, "B comp x func", start_t=0.0000, func_args="amp=5, freq=100, offset=1", n_points=100, func="amp*sin(2*pi*freq*t) + offset", stop_t=100.0000, functions=dict(func_args=lambda x: 'amp={}, freq={}, offset={}'.format(cmd.get_var('mod_amp'), cmd.get_var('mod_freq'),cmd.get_var('Bx_GM')+cmd.get_var('Bx_bottom')), stop_t=lambda x: cmd.get_var('mod_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time'), n_points=lambda x: 1e-3*cmd.get_var('mod_time') * cmd.get_var('mod_freq') * 10))
    prg.add(230000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('mod_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    prg.add(230000000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('mod_time')+cmd.get_var('hold_time_2')))
    prg.add(230000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('mod_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')-1))
    prg.add(230000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('mod_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    prg.add(240000000, "open_probe_z")
    prg.add(250000000, "open_probe_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('mod_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(80, 120, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        mod_freq = iters[j]
        cmd.set_var('mod_freq', mod_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nmod_freq = %g\n'%(j+1, len(iters), mod_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
