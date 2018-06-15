prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-190000, "Na Probe/Push (+) OFF")
    prg.add(-99564, "Na Probe/Push (+) freq", 110.00)
    prg.add(-90000, "Na Probe/Push (-) freq", 110.00)
    prg.add(-10000, "Na Probe/Push (-) Amp", 1000)
    prg.add(0, "Na Probe/Push (+) Amp", 1000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.2, 3, 0.2)
    j = 0
    while(cmd.running):
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
