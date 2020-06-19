prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Probe y (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(5000, "Na Probe z (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_z_amp')))
    prg.add(10000, "Na Probe/Push (-) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(20000, "Na Probe y (+) freq", 0.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(25000, "Na Probe z (+) freq", 0.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(30000, "Na Probe/Push (-) freq", 0.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(35000, "TTL Probe y ON")
    prg.add(40000, "TTL Probe z ON")
    prg.add(45000, "Mirrors Imaging")
    prg.add(115000, "Shutter Probe/Push Open")
    prg.add(156245, "Shutter repump Na Open")
    prg.add(185000, "Na Repumper1 (+) Amp", 800, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(195000, "Na Repumper2 (+) Amp", 800, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(20005000, "TTL Repumper MOT ON")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 14, 3)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        cam2_position = iters[j]
        cmd.set_var('cam2_position', cam2_position)
        print('\n')
        print('Run #%d/%d, with variables:\ncam2_position = %g\n'%(j+1, len(iters), cam2_position))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
