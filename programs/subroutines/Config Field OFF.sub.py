prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(20, "IGBT 3 Open")
    prg.add(30, "IGBT 4 Open")
    prg.add(50, "IGBT 2 Open")
    prg.add(60, "IGBT 5 Open")
    prg.add(10069, "Delta 1 Current", 0.000)
    return prg
def commands(cmd):
    import numpy as np
    iters = [100, 200, 400, 600, 800, 1000]
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        push_amp1 = iters[j]
        cmd.set_var('push_amp', push_amp1)
        print('\n')
        print('Run #%d/%d, with variables:\npush_amp = %g\n'%(j+1, len(iters), push_amp1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
