prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Pinning Lock", 0.2000)
    prg.add(100050, "TTL Pinning ON")
    prg.add(110050, "Pinning Lock", 0.0000)
    prg.add(110100, "TTL Pinning OFF")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(130, 200, 10)
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
