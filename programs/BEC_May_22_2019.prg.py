prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON")
    prg.add(99943111, "MOT lights Off TTL.sub")
    prg.add(99947301, "Config Field OFF.sub")
    prg.add(99949001, "Gray Molasses 2017")
    prg.add(99980000, "Scope 1 Trigger OFF")
    prg.add(99985000, "Scope 2 Trigger ON")
    prg.add(99986000, "Scope 2 Trigger OFF")
    prg.add(100000000, "Load_Quad")
    prg.add(105000000, "Ramp_bias_down.sub")
    prg.add(110000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(130000000, "Quad_RampDOWN", functions=dict(time=lambda x: 10000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(132001000, "Config Field OFF.sub", functions=dict(time=lambda x: 10000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown_time')))
    prg.add(132051000, "BEC_imaging", functions=dict(time=lambda x: 10000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('tof')))
    prg.add(158575000, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: 10000+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown_time')+cmd.get_var('tof')+1000))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 4, 0.3)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        By_img1 = iters[j]
        cmd.set_var('By_img', By_img1)
        print('\n')
        print('Run #%d/%d, with variables:\nBy_img = %g\n'%(j+1, len(iters), By_img1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
