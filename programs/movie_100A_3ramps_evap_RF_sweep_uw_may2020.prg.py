prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(259000000, "Synchronize.sub", enable=False)
    prg.add(259943111, "MOT lights Off TTL.sub")
    prg.add(259947301, "Config Field OFF.sub")
    prg.add(259949001, "Gray Molasses 2017")
    prg.add(259949001, "Optical pumping", enable=False)
    prg.add(259949011, "Scope 2 Trigger ON")
    prg.add(259986000, "Scope 2 Trigger OFF")
    prg.add(260000000, "Load_Quad")
    prg.add(260010000, "Quad_RampUP")
    prg.add(260060000, "Mirrors Imaging")
    prg.add(265000000, "Ramp_bias_down.sub")
    prg.add(266000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(270000000, "Number_lock", enable=False)
    prg.add(280000000, "Evaporation_quad_rampdown_2ramps")
    prg.add(280000000, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.25e6, freq2=1.15e6, duration=10", n_points=80, func="freq1+ (freq2-freq1)/duration *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, freq2={}, duration={}'.format(cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap3_fend')*1e6,cmd.get_var('evap3_time')*1e-3), stop_t=lambda x: cmd.get_var('evap3_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.001))
    prg.add(280000000, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+0.032))
    prg.add(280100000, "Pulse uw ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')-10.12))
    prg.add(280100120, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') - 0.0348))
    prg.add(280100120, "rf_sweep", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(280100120, "rf_pulse", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(280100120, "Rf Sweep Siglent", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(280100120, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')-100.124))
    prg.add(280100120, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+ cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof')), enable=False)
    prg.add(280100120, "multiple_RF_sweep_movie", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(280100120, "RF sweep DAC V", 0.0000, functions=dict(value=lambda x: cmd.get_var('DAC_V'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')-4.0123))
    prg.add(280105120, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('evap3_time')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))), enable=False)
    prg.add(280105120, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('evap3_time')+cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))+cmd.get_var('tof2') -1))
    prg.add(280105120, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('evap3_time') +cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))+cmd.get_var('tof2')), enable=False)
    prg.add(282605120, "RF sweep DAC V", 0.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))+cmd.get_var('tof2')))
    prg.add(283105120, "Pulse uw OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))+cmd.get_var('tof2')))
    prg.add(290105120, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')), enable=False)
    prg.add(300105120, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(300405120, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.1, 1.14, 0.01)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        evap2_fend = iters[j]
        cmd.set_var('evap2_fend', evap2_fend)
        print('\n')
        print('Run #%d/%d, with variables:\nevap2_fend = %g\n'%(j+1, len(iters), evap2_fend))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
