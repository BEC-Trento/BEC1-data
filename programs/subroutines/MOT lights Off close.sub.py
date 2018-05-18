prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-11600, "Na Probe/Push (+) Amp", 1)
    prg.add(-10300, "Na Probe/Push (-) Amp", 1)
    prg.add(-9300, "Na Zeeman slower (-) Amp", 1)
    prg.add(-8300, "Na 2D MOT (+) Amp", 1)
    prg.add(-6700, "TTL Repumper MOT OFF")
    prg.add(-1500, "Na Repumper1 (+) Amp", 1)
    prg.add(-1300, "TTL Dark Spot OFF")
    prg.add(0, "Na 3D MOT cool (-) Amp", 1)
    prg.add(600, "Na 3D MOT cool (+) Amp", 1)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(610, 640, 5)
    j = 0
    while(cmd.running):
        b1 = iters[j]
        cmd.set_var('b', b1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nb = %g\n'%(j+1, len(iters), b1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
