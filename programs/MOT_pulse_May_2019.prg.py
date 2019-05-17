prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(40000, "Scope 1 Trigger ON")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(10104200, "Config Field OFF.sub", enable=False)
    prg.add(10200000, "TTL Dark Spot OFF", enable=False)
    prg.add(10300000, "Scope 1 Trigger OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 20, 2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        x1 = iters[j]
        cmd.set_var('x', x1)
        print('\n')
        print('Run #%d/%d, with variables:\nx = %g\n'%(j+1, len(iters), x1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
