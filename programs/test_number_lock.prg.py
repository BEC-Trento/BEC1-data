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
    prg.add(110010000, "Quad_RampUP")
    prg.add(110060000, "Mirrors Imaging")
    prg.add(115000000, "Ramp_bias_down.sub")
    prg.add(116000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(125100000, "Evaporation amp", 1000, enable=False)
    prg.add(125116470, "Evaporation ramp", start_t=0.0000, func_args="a=6e6, b=10e6, duration=0.1, tau=0.5", n_points=500, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=100.0000, enable=False)
    prg.add(126136470, "Evaporation amp", 1, enable=False)
    prg.add(130000000, "Number_lock")
    prg.add(146137470, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=400, start_x=0.000, stop_t=2800.0000, functions=dict(stop_x=lambda x: cmd.get_var('Quad_rampdown2_current'), start_x=lambda x: 200))
    prg.add(181137470, "Setup_imaging")
    prg.add(181137470, "Config Field OFF.sub")
    prg.add(181137470, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.769e+09, 1.771e+09, 100000)
    np.random.shuffle(iters)
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
