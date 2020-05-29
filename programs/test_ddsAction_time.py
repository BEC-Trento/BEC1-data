prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(5000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01556)
    prg.add(5100, "Evaporation amp", 1000)
    prg.add(5410, "Evaporation amp", 1)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.5, 4, 0.2)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        siglent1_sweep_time = iters[j]
        cmd.set_var('siglent1_sweep_time', siglent1_sweep_time)
        print('\n')
        print('Run #%d/%d, with variables:\nsiglent1_sweep_time = %g\n'%(j+1, len(iters), siglent1_sweep_time))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
