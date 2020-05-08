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
    prg.add(230000000, "Evaporation_quad_rampdown_2ramps")
    prg.add(240000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2') - 0.0348))
    prg.add(240000000, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('marconi1_pulsetime')*1e-3, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')))
    prg.add(240000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')+ cmd.get_var('t1')-50))
    prg.add(240000000, "Single_frame_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')+ cmd.get_var('t1')))
    prg.add(240000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')), enable=False)
    prg.add(240000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(240000000, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(240000000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')+ cmd.get_var('t1')+3.1415))
    prg.add(240000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')+cmd.get_var('t1')+cmd.get_var('tof')-1))
    prg.add(240000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')+cmd.get_var('t1')+cmd.get_var('tof')))
    prg.add(240000000, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('tof')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')), enable=False)
    prg.add(250000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('t_wait')+cmd.get_var('t_wait2')+cmd.get_var('t1')), enable=False)
    prg.add(260000000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(260300000, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.12, 13.37, 1.01)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        marconi1_pulsetime = iters[j]
        cmd.set_var('marconi1_pulsetime', marconi1_pulsetime)
        print('\n')
        print('Run #%d/%d, with variables:\nmarconi1_pulsetime = %g\n'%(j+1, len(iters), marconi1_pulsetime))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
