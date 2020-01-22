prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(109000000, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(109943111, "MOT lights Off TTL.sub")
    prg.add(109947301, "Config Field OFF.sub")
    prg.add(109949001, "Gray Molasses 2017")
    prg.add(109949001, "Optical pumping", enable=False)
    prg.add(109985000, "Scope 2 Trigger ON")
    prg.add(109986000, "Scope 2 Trigger OFF")
    prg.add(110000000, "Load_Quad")
    prg.add(110000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('hold_time_2')), enable=False)
    prg.add(110000000, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')-0.1))
    prg.add(110000000, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')-0.05))
    prg.add(110000000, "Green Light AOM amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('green_amp'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(110000000, "Green Light AOM amp", 0, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('tof')+0.173), enable=False)
    prg.add(110000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')), enable=False)
    prg.add(110000000, "BEC_imaging_z", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(110000000, "Config Levitation", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('hold_time_2')))
    prg.add(110000000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')-1))
    prg.add(110000000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('green_time')+cmd.get_var('hold_time_2')+cmd.get_var('tof')))
    prg.add(110010000, "Quad_RampUP")
    prg.add(110020000, "Evaporation amp", 1000, enable=False)
    prg.add(110020000, "Evaporation_setfull", ch0_amp=1000, ch0_freq=24000000.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(110030000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(110040000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_time')*1e-3, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: x +cmd.get_var('evap1_time')))
    prg.add(110041000, "Evaporation amp", 1, functions=dict(time=lambda x: x +cmd.get_var('evap1_time') + cmd.get_var('evap2_time')))
    prg.add(110044000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')))
    prg.add(110044000, "IGBT B grad x ON", functions=dict(time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')), enable=False)
    prg.add(110050000, "B grad x ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=1000, functions=dict(time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time'), stop_x=lambda x: cmd.get_var('Bx_grad')), enable=False)
    prg.add(110060000, "Mirrors Imaging")
    prg.add(110500000, "IGBT B grad x OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(110510000, "B grad x", 0.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(115000000, "Ramp_bias_down.sub")
    prg.add(120000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(120000000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.1, 10.1, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        hold_time_2 = iters[j]
        cmd.set_var('hold_time_2', hold_time_2)
        print('\n')
        print('Run #%d/%d, with variables:\nhold_time_2 = %g\n'%(j+1, len(iters), hold_time_2))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
