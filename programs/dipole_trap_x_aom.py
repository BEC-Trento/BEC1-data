prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Dipole Trap x AOM (+) Amp", 1)
    prg.add(2000000, "Dipole Trap x AOM (+) Amp", 1000)
    prg.add(7000000, "Dipole Trap x AOM (+) freq", 110.00)
    prg.add(9000000, "Dipole Trap y AOM (-) Amp", 1000)
    prg.add(10000000, "Dipole Trap y AOM (-) freq", 110.00)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(5, 50, 5)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof = iters[j]
        cmd.set_var('tof', tof)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=101)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
