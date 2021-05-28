prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(5000000, "Dipole trap xy STANDBY")
    prg.add(10000000, "Dipole trap xy ON")
    prg.add(20000000, "Dipole trap xy STANDBY")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.3, 1.51, 0.04)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        evap2_fend = iters[j]
        cmd.set_var('evap2_fend', evap2_fend)
        print('\n')
        print('Run #%d/%d, with variables:\nevap2_fend = %g\n'%(j+1, len(iters), evap2_fend))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
