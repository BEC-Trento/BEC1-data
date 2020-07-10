prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(109000000, "Synchronize.sub", enable=False)
    prg.add(109943111, "MOT lights Off TTL.sub")
    prg.add(109947301, "Config Field OFF.sub")
    prg.add(109949001, "Gray Molasses 2017")
    prg.add(109949001, "Optical pumping", enable=False)
    prg.add(109949011, "Scope 2 Trigger ON")
    prg.add(109986000, "Scope 2 Trigger OFF")
    prg.add(110000000, "Load_Quad")
    prg.add(110010000, "Delta 1 Current ramp", start_t=0.0000, stop_x=100.000, n_points=151, start_x=0.000, stop_t=0.0000, functions=dict(start_x=lambda x: cmd.get_var('Quad_current'), stop_t=lambda x: cmd.get_var('Quad_rampup_time')))
    prg.add(110011000, "Delta 1 Voltage ramp", start_t=0.0000, stop_x=28.000, n_points=151, start_x=6.000, stop_t=0.0000, functions=dict(stop_t=lambda x: cmd.get_var('Quad_rampup_time')))
    prg.add(110060000, "Mirrors Imaging")
    prg.add(115000000, "Ramp_bias_down.sub")
    prg.add(116000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(130000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-0.0347))
    prg.add(130000000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-2.135))
    prg.add(130000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+0.241), enable=False)
    prg.add(130000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(130000000, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(130000000, "BEC_imaging_x", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(130000000, "BEC_imaging_xz", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(130000000, "BEC_imaging_yz", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(130000000, "BEC_imaging_xyz", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(130100000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(140100000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(140400000, "open_probe", functions=dict(time=lambda x: x+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(50, 1000, 100)
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
