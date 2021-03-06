prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(200, 1001, 100)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        push_amp = iters[j]
        cmd.set_var('push_amp', push_amp)
        print('\n')
        print('Run #%d/%d, with variables:\npush_amp = %g\n'%(j+1, len(iters), push_amp))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
