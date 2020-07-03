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
    prg.add(210010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=100.000, n_points=151, start_x=0.000, stop_t=0.0000, functions=dict(start_x=lambda x: cmd.get_var('Quad_current'), stop_t=lambda x: cmd.get_var('Quad_rampup_time')))
    prg.add(210011000, "Delta 1 Voltage ramp", start_t=0.0000, stop_x=28.000, n_points=151, start_x=6.000, stop_t=0.0000, functions=dict(stop_t=lambda x: cmd.get_var('Quad_rampup_time')))
    prg.add(210060000, "Mirrors Imaging")
    prg.add(215000000, "Ramp_bias_down.sub")
    prg.add(216000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(230000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')-0.1))
    prg.add(230000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-2.135))
    prg.add(230000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+0.241), enable=False)
    prg.add(230000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(230000000, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(230000000, "BEC_imaging_x", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(230000000, "BEC_imaging_xz", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(230000000, "BEC_imaging_yz", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(230000000, "BEC_imaging_xyz", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(230100000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(240100000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(240400000, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-0.104, -0.101, 0.001)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Bx_bottom = iters[j]
        cmd.set_var('Bx_bottom', Bx_bottom)
        print('\n')
        print('Run #%d/%d, with variables:\nBx_bottom = %g\n'%(j+1, len(iters), Bx_bottom))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=99)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
