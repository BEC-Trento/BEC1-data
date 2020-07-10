prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(209943111, "MOT lights Off TTL.sub")
    prg.add(209947301, "Config Field OFF.sub")
    prg.add(209949001, "Gray Molasses 2017")
    prg.add(209949011, "Scope 2 Trigger ON")
    prg.add(209986000, "Scope 2 Trigger OFF")
    prg.add(210000000, "Load_Quad")
    prg.add(210010000, "Quad_RampUP")
    prg.add(210060000, "Mirrors Imaging")
    prg.add(215000000, "Ramp_bias_down.sub")
    prg.add(216000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(230000000, "Evaporation_2ramps_keep_on")
    prg.add(230001000, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.25e6, freq2=1.15e6, duration=10", n_points=300, func="freq1+ (freq2-freq1)/duration *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, freq2={}, duration={}'.format(cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap3_fend')*1e6,cmd.get_var('evap3_time')*1e-3), stop_t=lambda x: cmd.get_var('evap3_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(230001320, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')))
    prg.add(230001440, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start') - 0.0348))
    prg.add(230001440, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-1.124))
    prg.add(230001440, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(230001440, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time') +cmd.get_var('tof')-1))
    prg.add(230001449, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(230501449, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(246501449, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(246801449, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.3, 1.5, 0.1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        DAC_V = iters[j]
        cmd.set_var('DAC_V', DAC_V)
        print('\n')
        print('Run #%d/%d, with variables:\nDAC_V = %g\n'%(j+1, len(iters), DAC_V))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
