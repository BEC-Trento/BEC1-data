prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(159000000, "Synchronize.sub", enable=False)
    prg.add(159943111, "MOT lights Off TTL.sub")
    prg.add(159947301, "Config Field OFF.sub")
    prg.add(159949001, "Gray Molasses 2017")
    prg.add(159949001, "Optical pumping", enable=False)
    prg.add(159949011, "Scope 2 Trigger ON")
    prg.add(159986000, "Scope 2 Trigger OFF")
    prg.add(160000000, "Load_Quad")
    prg.add(160010000, "Quad_RampUP")
    prg.add(160060000, "Mirrors Imaging")
    prg.add(165000000, "Ramp_bias_down.sub")
    prg.add(166000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(170000000, "Number_lock", enable=False)
    prg.add(180000000, "Evaporation_quad_rampdown_2ramps")
    prg.add(188990000, "Pulse uw ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(190000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')  - 0.0348))
    prg.add(190000000, "Evaporation_setfull", ch0_amp=1000, ch0_freq=1000000.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: cmd.get_var('rf_freq1')*1e6, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')-0.0013), enable=False)
    prg.add(190000000, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.082e6, freq2=1.084e6, duration=10", n_points=100, func="freq1+ (freq2-freq1)/duration *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, freq2={}, duration={}'.format(cmd.get_var('rf_freq1')*1e6, cmd.get_var('rf_freq2')*1e6, cmd.get_var('rf_pulse_time')*1e-3), stop_t=lambda x: cmd.get_var('rf_pulse_time'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(190000000, "Evaporation_setfull", ch0_amp=1, ch0_freq=1000000.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: cmd.get_var('rf_freq2')*1e6, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('rf_pulse_time')+0.0012), enable=False)
    prg.add(190000000, "rf_sweep", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(190000000, "rf_pulse", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(190000010, "B grad x kick", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+ cmd.get_var('rf_pulse_time')), enable=False)
    prg.add(190000010, "Evaporation_setfull", ch0_amp=1000, ch0_freq=0.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: cmd.get_var('rf_freq1')*1e6, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(190000010, "Evaporation_setfull", ch0_amp=1, ch0_freq=0.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: cmd.get_var('rf_freq1')*1e6, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('rf_pulse_time')), enable=False)
    prg.add(190000010, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')-50))
    prg.add(190000010, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+ cmd.get_var('t1')), enable=False)
    prg.add(190000010, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(190000010, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(190000010, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(190005010, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+1))
    prg.add(190005010, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('tof')-1))
    prg.add(190005010, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') +cmd.get_var('tof')))
    prg.add(195005010, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('tof')), enable=False)
    prg.add(198005010, "Pulse uw OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time') + cmd.get_var('rf_pulse_time') +cmd.get_var('tof')), enable=False)
    prg.add(205005010, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(215005010, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(215305010, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(20, 100, 10)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        rf_amp = iters[j]
        cmd.set_var('rf_amp', rf_amp)
        print('\n')
        print('Run #%d/%d, with variables:\nrf_amp = %g\n'%(j+1, len(iters), rf_amp))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
