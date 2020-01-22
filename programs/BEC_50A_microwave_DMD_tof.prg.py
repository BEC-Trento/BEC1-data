prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF")
    prg.add(5010234, "Green Light AOM amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('green_amp')))
    prg.add(159943111, "MOT lights Off TTL.sub")
    prg.add(159947301, "Config Field OFF.sub")
    prg.add(159949001, "Gray Molasses 2017")
    prg.add(159949001, "Optical pumping", enable=False)
    prg.add(159975000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(159985000, "Scope 2 Trigger ON")
    prg.add(159986000, "Scope 2 Trigger OFF")
    prg.add(159999990, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+1+cmd.get_var('tof')-0.009))
    prg.add(159999990, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+1+cmd.get_var('tof')+.15))
    prg.add(160000000, "Load_Quad")
    prg.add(160000000, "Green Light AOM amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('green_amp'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(160000000, "Green Light AOM amp", 0, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+1+cmd.get_var('tof')+cmd.get_var('green_time')))
    prg.add(160000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+1+cmd.get_var('tof')))
    prg.add(160000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('hold_time_2')), enable=False)
    prg.add(160000000, "BEC_imaging_z_vertical", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')+1+cmd.get_var('tof')))
    prg.add(160000011, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('evap3_time')+cmd.get_var('hold_time')))
    prg.add(160030000, "Quad_RampUP")
    prg.add(160045000, "Evaporation_quad_rampdown_3ramps")
    prg.add(160084000, "Mirrors Imaging")
    prg.add(165034000, "Ramp_bias_down.sub")
    prg.add(170034000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(170034000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('sync_delay_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.77036e+09, 1.77036e+09, 5)
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
