prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(1100000, "All AOM On.sub")
    prg.add(2100000, "Shutter Probe Na Open")
    prg.add(22100000, "Shutter Probe Na Close")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(-3, 4, 2)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        probe_det1 = iters[j]
        cmd.set_var('probe_det', probe_det1)
        print('\n')
        print('Run #%d/%d, with variables:\nprobe_det = %g\n'%(j+1, len(iters), probe_det1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
