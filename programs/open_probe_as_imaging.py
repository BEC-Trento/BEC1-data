prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000000, "Setup_imaging")
    prg.add(15000000, "open_probe")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-0.161, -0.16, 0.002)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Bx_bottom = iters[j]
        cmd.set_var('Bx_bottom', Bx_bottom)
        print('\n')
        print('Run #%d/%d, with variables:\nBx_bottom = %g\n'%(j+1, len(iters), Bx_bottom))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
