prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "All AOM On.sub")
    prg.add(100000, "All Shutter open 2023")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0, 10, 1)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        repeat = iters[j]
        cmd.set_var('repeat', repeat)
        print('\n')
        print('Run #%d/%d, with variables:\nrepeat = %g\n'%(j+1, len(iters), repeat))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
