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
    prg.add(209949011, "Scope 2 Trigger ON")
    prg.add(209986000, "Scope 2 Trigger OFF")
    prg.add(210000000, "Load_Quad")
    prg.add(210010000, "Quad_RampUP")
    prg.add(210060000, "Mirrors Imaging")
    prg.add(215000000, "Ramp_bias_down.sub")
    prg.add(216000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(220000000, "Number_lock", enable=False)
    prg.add(230000000, "Evaporation_quad_rampdown_3ramps")
    prg.add(230000000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(232500000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(232500000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01356, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time') - 0.00123), enable=False)
    prg.add(232500000, "Evaporation_setfull", ch0_amp=1000, ch0_freq=457620.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: cmd.get_var('RF_freq'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time'), ch0_amp=lambda x: cmd.get_var('RF_amp')), enable=False)
    prg.add(232500000, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time') + 1e-3*cmd.get_var('RF_pulsetime')), enable=False)
    prg.add(232500000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')), enable=False)
    prg.add(232500000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')+10), enable=False)
    prg.add(232500000, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3 * cmd.get_var('marconi1_pulsetime'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(232500000, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')), enable=False)
    prg.add(232500000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')))
    prg.add(232500000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')-1))
    prg.add(232500000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')+min(2+1e-3*cmd.get_var('cam1_ExposureTime'), cmd.get_var('tof'))))
    prg.add(242500000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(3, 10, 2)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time_2 = iters[j]
        cmd.set_var('hold_time_2', hold_time_2)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time_2 = %g\n'%(j+1, len(iters), hold_time_2))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
