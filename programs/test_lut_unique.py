prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(9999900, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(10000000, "Evaporation amp", 1000)
    prg.add(10010000, "Evaporation freq", 54000000)
    prg.add(11010000, "Evaporation amp", 0)
    prg.add(11500000, "Evaporation amp", 1)
    prg.add(12500000, "Evaporation amp", 0)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-0.3, -0.1, 0.02)
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
