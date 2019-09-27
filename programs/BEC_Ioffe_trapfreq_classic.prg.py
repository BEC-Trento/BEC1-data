prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(159943111, "MOT lights Off TTL.sub")
    prg.add(159947301, "Config Field OFF.sub")
    prg.add(159949001, "Gray Molasses 2017")
    prg.add(159949001, "Optical pumping", enable=False)
    prg.add(159985000, "Scope 2 Trigger ON")
    prg.add(159986000, "Scope 2 Trigger OFF")
    prg.add(160000000, "Load_Quad")
    prg.add(160000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(160000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(160000000, "IGBT B grad x OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(160000000, "B comp z", 0.0000, functions=dict(value=lambda x: cmd.get_var('Bz_GM'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(160000000, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_GM'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')))
    prg.add(160000000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')), enable=False)
    prg.add(160000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    prg.add(160000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')+1))
    prg.add(160010000, "Quad_RampUP")
    prg.add(160030000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(160040000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_time')*1e-3, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: x +cmd.get_var('evap1_time')))
    prg.add(160044000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')))
    prg.add(160044000, "IGBT B grad x ON", functions=dict(time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')), enable=False)
    prg.add(160050000, "B grad x ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=1000, functions=dict(time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time'), stop_x=lambda x: cmd.get_var('Bx_grad')), enable=False)
    prg.add(160050000, "B comp z ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.000, stop_t=1000.0000, functions=dict(time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time'), start_x=lambda x: cmd.get_var('Bz_GM'), stop_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_offset')), enable=False)
    prg.add(160050000, "B comp y ramp", start_t=0.0000, stop_x=0.000, n_points=200, start_x=0.000, stop_t=1000.0000, functions=dict(time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time'), start_x=lambda x: cmd.get_var('By_GM'), stop_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_offset')))
    prg.add(160060000, "Mirrors Imaging")
    prg.add(165000000, "Ramp_bias_down.sub")
    prg.add(170000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(170000000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(170000000, "B grad x", 0.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    return prg
def commands(cmd):
    import numpy as np
    a1 = np.arange(0, 30, 1)
    a2 = np.arange(40, 80, 1)
    iters = np.concatenate([a1, a2])
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time_21 = iters[j]
        cmd.set_var('hold_time_2', hold_time_21)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time_2 = %g\n'%(j+1, len(iters), hold_time_21))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
