prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100, "Rabi preparation 2")
    prg.add(3370150, "ReleConfigBackForGravityComp")
    prg.add(3870150, "Rabi pulse New Antena")
    prg.add(3874450, "Bx Grad Pulse", enable=False)
    prg.add(9884450, "Bx Grad OFF", functions=dict(time=lambda x: x+cmd.get_var('dt'), funct_enable=False))
    prg.add(9884550, "TTL2 5 OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(4, 20, 4)
    j = 0
    while(cmd.running):
        dt1 = iters[j]
        cmd.set_var('dt', dt1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ndt = %g\n'%(j+1, len(iters), dt1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
