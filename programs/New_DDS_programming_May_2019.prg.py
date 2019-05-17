prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Evaporation freq", 10000000)
    prg.add(10000000, "Evaporation freq", 20000000)
    prg.add(30000000, "Evaporation freq", 30000000)
    prg.add(50000000, "Evaporation ramp", start_t=0.0000, func_args="fstart=45000000, fend=25000000, tau=1", n_points=500, func="(fstart - fend)*exp(-t/tau) + fend", stop_t=5000.0000)
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
