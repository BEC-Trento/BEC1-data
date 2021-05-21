prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(10000000, "Dipole trap xy STANDBY")
    prg.add(110000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(129000000, "Synchronize.sub", enable=False)
    prg.add(129943111, "MOT lights Off TTL.sub")
    prg.add(129947301, "Config Field OFF.sub")
    prg.add(129949001, "Gray Molasses 2017")
    prg.add(129949011, "Scope 2 Trigger ON")
    prg.add(129986000, "Scope 2 Trigger OFF")
    prg.add(130000000, "Load_Quad")
    prg.add(130010000, "Quad_RampUP")
    prg.add(130060000, "Mirrors Imaging")
    prg.add(135000000, "Ramp_bias_down.sub")
    prg.add(136000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(140000000, "Number_lock", enable=False)
    prg.add(150001000, "Evaporation_2ramps_keep_on")
    prg.add(150001400, "Dipole trap xy ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('dipole_delay_time')))
    prg.add(150031000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(150052419, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+0.23))
    prg.add(150052419, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-12.135))
    prg.add(150052419, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')-cmd.get_var('t_cfo')))
    prg.add(150053420, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')), enable=False)
    prg.add(150053420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-cmd.get_var('t_cfo')), enable=False)
    prg.add(150053420, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(150053421, "BEC_imaging_x", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(150053421, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(150053421, "BEC_imaging_xy", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    prg.add(150153420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(163999999, "Dipole trap xy STANDBY", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    prg.add(170153420, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(170453420, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.1, 1.6, 0.1)
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
