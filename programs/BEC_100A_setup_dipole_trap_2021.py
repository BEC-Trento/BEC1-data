prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(10000000, "Dipole trap xy STANDBY")
    prg.add(100000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(119000000, "Synchronize.sub", enable=False)
    prg.add(119943111, "MOT lights Off TTL.sub")
    prg.add(119947301, "Config Field OFF.sub")
    prg.add(119949001, "Gray Molasses 2017")
    prg.add(119949011, "Scope 2 Trigger ON")
    prg.add(119986000, "Scope 2 Trigger OFF")
    prg.add(120000000, "Load_Quad")
    prg.add(120010000, "Quad_RampUP")
    prg.add(120060000, "Mirrors Imaging")
    prg.add(125000000, "Ramp_bias_down.sub")
    prg.add(126000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(130000000, "Number_lock", enable=False)
    prg.add(139900000, "Dipole trap xy ON", enable=False)
    prg.add(140001000, "Evaporation_2ramps_keep_on")
    prg.add(140031000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(140052419, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+0.23))
    prg.add(140052419, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-12.135))
    prg.add(140052419, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')-cmd.get_var('t_cfo')))
    prg.add(140053420, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')), enable=False)
    prg.add(140053420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')-cmd.get_var('t_cfo')), enable=False)
    prg.add(140053420, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(140053421, "BEC_imaging_x", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(140053421, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(140053421, "BEC_imaging_xy", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    prg.add(140153420, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')), enable=False)
    prg.add(144000000, "Dipole trap xy STANDBY", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('sync_time')+cmd.get_var('evap3_time')+cmd.get_var('t_movie_start')+cmd.get_var('tof')))
    prg.add(150153421, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(150453421, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 2.1, 0.5)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Levitation_current = iters[j]
        cmd.set_var('Levitation_current', Levitation_current)
        print('\n')
        print('Run #%d/%d, with variables:\nLevitation_current = %g\n'%(j+1, len(iters), Levitation_current))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
