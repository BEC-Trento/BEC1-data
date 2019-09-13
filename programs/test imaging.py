prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Mirrors Imaging")
    prg.add(10000000, "BEC_imaging")
    prg.add(10000512, "Scope 1 Trigger ON")
    prg.add(10000562, "Scope 1 Trigger OFF")
    prg.add(15000000, "Na Probe/Push (+) ON")
    prg.add(15010000, "Shutter Probe Na Open")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-0.5, 0, 0.05)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Bx_bottom1 = iters[j]
        cmd.set_var('Bx_bottom', Bx_bottom1)
        print('\n')
        print('Run #%d/%d, with variables:\nBx_bottom = %g\n'%(j+1, len(iters), Bx_bottom1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
