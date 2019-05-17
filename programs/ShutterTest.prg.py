prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "All AOM On.sub")
    prg.add(2000000, "All Shutter Close.sub")
    prg.add(10000000, "All Shutter Open.sub")
    prg.add(10000500, "Scope 1 Trigger ON")
    prg.add(20000500, "Scope 1 Trigger OFF")
    prg.add(21800000, "All Shutter Close.sub")
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
