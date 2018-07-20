prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Mirrors Imaging")
    prg.add(20000, "Na Probe/Push (+) ON")
    prg.add(100000, "Shutter Probe Na Open")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 3, 1)
    j = 0
    while(cmd.running):
        asd1 = iters[j]
        cmd.set_var('asd', asd1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nasd = %g\n'%(j+1, len(iters), asd1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
