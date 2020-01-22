prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(109945000, "Config Field OFF.sub", enable=False)
    prg.add(109958001, "Gray Molasses 2017", enable=False)
    prg.add(109958012, "Scope 2 Trigger ON")
    prg.add(109958112, "Scope 2 Trigger OFF")
    prg.add(109959112, "B comp x", 5.0)
    prg.add(109969112, "B comp x", 1.0)
    prg.add(109972000, "MOT lights Off TTL_GM.sub", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(109972257, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(109982257, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(109983257, "Setup_imaging_GM", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(109983267, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(109989947, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(119939047, "DarkSpotMOT_19.sub", enable=False)
    prg.add(120939047, "AOM GM Amp ch1 (+)", 200, enable=False)
    prg.add(120940047, "AOM GM Amp ch2 (-)", 200, enable=False)
    prg.add(120941047, "Na Gray molasses (+) freq", 112.50, enable=False)
    prg.add(120942047, "Na Gray molasses (-) freq", 87.50, enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 20, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof = iters[j]
        cmd.set_var('tof', tof)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
