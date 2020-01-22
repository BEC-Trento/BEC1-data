prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(59000000, "Synchronize.sub", enable=False)
    prg.add(59943111, "MOT lights Off TTL.sub")
    prg.add(59947301, "Config Field OFF.sub")
    prg.add(59949001, "Gray Molasses 2017")
    prg.add(59949001, "Optical pumping", enable=False)
    prg.add(59949011, "Scope 2 Trigger ON")
    prg.add(59986000, "Scope 2 Trigger OFF")
    prg.add(60000000, "Load_Quad")
    prg.add(60010000, "Quad_RampUP")
    prg.add(60060000, "Mirrors Imaging")
    prg.add(65000000, "Ramp_bias_down.sub")
    prg.add(66000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(70000000, "Number_lock", enable=False)
    prg.add(80000000, "Evaporation_quad_rampdown_3ramps", enable=False)
    prg.add(110000000, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=200, start_x=200.000, stop_t=3000.0000)
    prg.add(145000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, functions=dict(time=lambda x: x - 0.00123))
    prg.add(145000000, "Setup_imaging")
    prg.add(145100000, "Config Field OFF.sub")
    prg.add(145100000, "BEC_imaging", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(155100000, "DarkSpotMOT_19.sub", enable=False)
    prg.add(155400000, "open_probe")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-16, 15, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_det = iters[j]
        cmd.set_var('probe_det', probe_det)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_det = %g\n'%(j+1, len(iters), probe_det))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
