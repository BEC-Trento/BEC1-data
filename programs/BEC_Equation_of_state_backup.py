prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(209000000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(209943111, "MOT lights Off TTL.sub")
    prg.add(209947301, "Config Field OFF.sub")
    prg.add(209949001, "Gray Molasses 2017")
    prg.add(209949001, "Optical pumping", enable=False)
    prg.add(209985000, "Scope 2 Trigger ON")
    prg.add(209986000, "Scope 2 Trigger OFF")
    prg.add(209990000, "Setup_microwave_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(209999990, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(209999990, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+0.156))
    prg.add(210000000, "Load_Quad")
    prg.add(210000000, "BEC_fast_imaging_uw_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(210010000, "Setup_tof_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(210010000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(210010000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-1))
    prg.add(210010000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(210210000, "Quad_RampUP")
    prg.add(210220000, "Evaporation_quad_rampdown_3ramps")
    prg.add(210260000, "Mirrors Imaging")
    prg.add(215200000, "Ramp_bias_down.sub")
    prg.add(220200000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(220200000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    i1 = np.random.uniform(0.8, 1.1, 20)
    i2 = np.random.uniform(1.4, 1.9, 150)
    i3 = np.random.uniform(2.2, 2.5, 50)
    iters = np.round(np.concatenate([i1, i2, i3]), 1)
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
