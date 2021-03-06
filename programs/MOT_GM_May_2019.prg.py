prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(1000000, "Scope 1 Trigger ON", enable=False)
    prg.add(1010000, "Scope 1 Trigger OFF", enable=False)
    prg.add(202943111, "MOT lights Off TTL.sub", enable=False)
    prg.add(202943111, "MOT lights Off TTL_GM.sub")
    prg.add(202945000, "Config Field OFF.sub")
    prg.add(202948001, "Gray Molasses 2017")
    prg.add(202948012, "Scope 2 Trigger ON")
    prg.add(202948112, "Scope 2 Trigger OFF")
    prg.add(203000257, "Setup_imaging_GM")
    prg.add(203000257, "Scope 1 Trigger ON", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(203000267, "BEC_imaging", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(203006947, "Scope 1 Trigger OFF", functions=dict(time=lambda x: x+cmd.get_var('tof')))
    prg.add(212956047, "DarkSpotMOT_19.sub", enable=False)
    prg.add(213256047, "open_probe", enable=False)
    prg.add(213356047, "Na Gray molasses (+) freq", 112.50, enable=False)
    prg.add(213456047, "Na Gray molasses (-) freq", 87.50, enable=False)
    prg.add(213756047, "AOM GM Amp ch1 (+)", 1000, enable=False)
    prg.add(213856047, "AOM GM Amp ch2 (-)", 1000, enable=False)
    prg.add(213956047, "Mirror x RIGHT Out", enable=False)
    prg.add(214056047, "Mirror z TOP Out", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 6, 1)
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
