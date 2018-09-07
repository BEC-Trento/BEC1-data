prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 15, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        x1 = iters[j]
        cmd.set_var('x', x1)
        print('\n')
        print('Run #%d/%d, with variables:\nx = %g\n'%(j+1, len(iters), x1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
