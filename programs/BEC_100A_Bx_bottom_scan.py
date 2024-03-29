prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(100000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(249000000, "Synchronize.sub", enable=False)
    prg.add(249943111, "MOT lights Off TTL.sub")
    prg.add(249947301, "Config Field OFF.sub")
    prg.add(249949001, "Gray Molasses 2017")
    prg.add(249949001, "Optical pumping", enable=False)
    prg.add(249949011, "Scope 2 Trigger ON")
    prg.add(249986000, "Scope 2 Trigger OFF")
    prg.add(250000000, "Load_Quad")
    prg.add(250010000, "Quad_RampUP")
    prg.add(250060000, "Mirrors Imaging")
    prg.add(255000000, "Ramp_bias_down.sub")
    prg.add(256000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(260000000, "Number_lock", enable=False)
    prg.add(270001000, "Evaporation_2ramps_keep_on")
    prg.add(270031000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(270052419, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+0.23))
    prg.add(270052419, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-12.135))
    prg.add(270052419, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-0.034))
    prg.add(270052420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')), enable=False)
    prg.add(270053420, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')))
    prg.add(270053420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-cmd.get_var('t_cfo')))
    prg.add(270053420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')-cmd.get_var('t_cfo')), enable=False)
    prg.add(270053420, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    prg.add(270053420, "BEC_imaging_x", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(270053420, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(270053420, "BEC_imaging_xy", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(270153419, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(280153420, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    prg.add(280453420, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-0.055, -0.0451, 0.002)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Bx_bottom = iters[j]
        cmd.set_var('Bx_bottom', Bx_bottom)
        print('\n')
        print('Run #%d/%d, with variables:\nBx_bottom = %g\n'%(j+1, len(iters), Bx_bottom))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
