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
    prg.add(230000000, "Evaporation_2ramps_keep_on")
    prg.add(230031000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(230040000, "Pulse uw ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('sync_time')-5.012), enable=False)
    prg.add(230052000, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.25e6, freq2=1.15e6, duration=10", n_points=100, func="freq1+ (freq2-freq1)/duration *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, freq2={}, duration={}'.format(cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap3_fend')*1e6,cmd.get_var('evap3_time')*1e-3), stop_t=lambda x: cmd.get_var('evap3_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')))
    prg.add(230052320, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('sync_time')+ cmd.get_var('t_movie_start')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))))
    prg.add(230052440, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start') - 0.0348))
    prg.add(230052440, "Rf Sweep Siglent", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')))
    prg.add(230052440, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('tof_frame'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start') + cmd.get_var('siglent1_sweep_time')+0.1), enable=False)
    prg.add(230052440, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')-41.124))
    prg.add(230052440, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+ cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof')), enable=False)
    prg.add(230052440, "multiple_RF_sweep_movie", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')), enable=False)
    prg.add(230052440, "RF sweep DAC V", 0.0000, functions=dict(value=lambda x: cmd.get_var('DAC_V'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')-50.0123), enable=False)
    prg.add(230052440, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start') + cmd.get_var('siglent1_sweep_time')+0.456 ))
    prg.add(230052440, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start') + cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame')-1.023))
    prg.add(230052449, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start') + cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame')))
    prg.add(232557440, "RF sweep DAC V", 0.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('sync_time')+cmd.get_var('evap3_time') + cmd.get_var('t_movie_start')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))), enable=False)
    prg.add(233557440, "Pulse uw OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))), enable=False)
    prg.add(234057440, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))), enable=False)
    prg.add(250057440, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(250357440, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('tof')), enable=False)
    prg.add(250457440, "open_probe_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.03, 1.09, 0.01)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        siglent1_freq = iters[j]
        cmd.set_var('siglent1_freq', siglent1_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nsiglent1_freq = %g\n'%(j+1, len(iters), siglent1_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
