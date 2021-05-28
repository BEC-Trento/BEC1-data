prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(10000000, "Dipole trap xy STANDBY")
    prg.add(200000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(219000000, "Synchronize.sub", enable=False)
    prg.add(219943111, "MOT lights Off TTL.sub")
    prg.add(219947301, "Config Field OFF.sub")
    prg.add(219949001, "Gray Molasses 2017")
    prg.add(219949011, "Scope 2 Trigger ON")
    prg.add(219986000, "Scope 2 Trigger OFF")
    prg.add(220000000, "Load_Quad")
    prg.add(220010000, "Quad_RampUP")
    prg.add(220060000, "Mirrors Imaging")
    prg.add(225000000, "Ramp_bias_down.sub")
    prg.add(226000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(230000000, "Number_lock", enable=False)
    prg.add(240001000, "Evaporation_2ramps_keep_on")
    prg.add(240001400, "Dipole trap xy ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('dipole_delay_time')))
    prg.add(240031000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')-cmd.get_var('sync_time')))
    prg.add(240052419, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.13))
    prg.add(240052419, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=100, start_x=100.000, stop_t=2000.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.23, start_x=lambda x: cmd.get_var('Quad_current_rampdown'), stop_t=lambda x: cmd.get_var('Quad_rampdown2_time'), stop_x=lambda x: cmd.get_var('Quad_rampdown2_current')))
    prg.add(240052419, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.23+cmd.get_var('Quad_rampdown2_time')))
    prg.add(240052419, "Ramp_bias_field", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.33))
    prg.add(240052419, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=200.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('Quad_rampdown2_time'), start_x=lambda x: cmd.get_var('Dipole_x_DAC_V'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V_final')))
    prg.add(240052419, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=8.000, stop_t=200.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('Quad_rampdown2_time')-0.04, start_x=lambda x: cmd.get_var('Dipole_y_DAC_V'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V_final')), enable=False)
    prg.add(240052419, "Dipole trap xy STANDBY", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')))
    prg.add(240052419, "Pulse uw", polarity=1, pulse_t=0.01000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')-1))
    prg.add(240052419, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')-1.05))
    prg.add(240052620, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')-22.3))
    prg.add(240053420, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof')))
    prg.add(240053420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('tof2')-cmd.get_var('t_cfo')))
    prg.add(240053420, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('tof2')+cmd.get_var('Quad_rampdown2_time')))
    prg.add(240053420, "Dipole trap xy STANDBY", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof2')+500), enable=False)
    prg.add(240053421, "BEC_imaging_x", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof2')), enable=False)
    prg.add(240053421, "BEC_imaging_xy", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof2')), enable=False)
    prg.add(240153420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof2')), enable=False)
    prg.add(260153420, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof2')), enable=False)
    prg.add(260453420, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('tof')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('tof2')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.77096e+09, 1.77105e+09, 10000)
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
