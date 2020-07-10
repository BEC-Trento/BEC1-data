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
    prg.add(230000000, "Evaporation amp", 1000)
    prg.add(230010000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=330, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(230014000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')))
    prg.add(230014000, "Evaporation amp", 1, functions=dict(time=lambda x: x +cmd.get_var('evap1_time') + 0.98))
    prg.add(232014000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-0.034))
    prg.add(232014000, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')-2.135))
    prg.add(232014000, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3 * cmd.get_var('marconi1_pulsetime'), time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')), enable=False)
    prg.add(232014000, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')), enable=False)
    prg.add(232014000, "BEC_imaging_field_lock", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    prg.add(232114000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('hold_time')+cmd.get_var('tof')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-0.1001, -0.06, 0.002)
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
