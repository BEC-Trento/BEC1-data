prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL2-12 ON")
    prg.add(10000000, "TTL2-12 OFF", functions=dict(time=lambda x: cmd.get_var('x')))
    prg.add(10000000, "TTL2-12 ON")
    prg.add(20000000, "TTL2-12 OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(500, 2000, 500)
    j = 0
    while(cmd.running):
        x1 = iters[j]
        cmd.set_var('x', x1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nx = %g\n'%(j+1, len(iters), x1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
