prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(209000000, "Synchronize.sub", enable=False)
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
    prg.add(230001000, "Evaporation_2ramps_keep_on")
    prg.add(230031000, "Synchronize.sub")
    prg.add(230051349, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.25e6, q=500e3", n_points=100, func="freq1- q *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, q={}'.format(cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap3_q')*1e3), stop_t=lambda x: cmd.get_var('evap3_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')))
    prg.add(230051699, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.25e6, q=100e3", n_points=100, func="freq1- q *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, q={}'.format((cmd.get_var('evap2_fend')-cmd.get_var('evap3_time')*1e-6*cmd.get_var('evap3_q'))*1e6, cmd.get_var('evap4_q')*1e3), stop_t=lambda x: cmd.get_var('evap4_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')))
    prg.add(230052100, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.25e6, q=50e3", n_points=100, func="freq1- q *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, q={}'.format((cmd.get_var('evap2_fend')-cmd.get_var('evap3_time')*1e-6*cmd.get_var('evap3_q')-cmd.get_var('evap4_time')*1e-6*cmd.get_var('evap4_q'))*1e6, cmd.get_var('evap5_q')*1e3), stop_t=lambda x: cmd.get_var('evap5_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')), enable=False)
    prg.add(230052100, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+0.23), enable=False)
    prg.add(230052100, "Evaporation freq", 0, functions=dict(frequency=lambda x: (cmd.get_var('evap2_fend')+cmd.get_var('rf_shield_offset'))*1e6, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('sync_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+0.033))
    prg.add(230052419, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+cmd.get_var('t_movie_start')+0.23))
    prg.add(230052460, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-0.034))
    prg.add(230052460, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-2.135))
    prg.add(230052460, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+cmd.get_var('t_movie_start')))
    prg.add(230052460, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-1))
    prg.add(230052460, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('evap4_time')+cmd.get_var('evap5_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(20, 476, 50)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        evap4_time = iters[j]
        cmd.set_var('evap4_time', evap4_time)
        print('\n')
        print('Run #%d/%d, with variables:\nevap4_time = %g\n'%(j+1, len(iters), evap4_time))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=101)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
