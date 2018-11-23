prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(0, "Initialize Experiment.sub", enable=False)
    prg.add(2000000, "Pulse TTL2-12", polarity=1, pulse_t=2.00000)
    prg.add(2040000, "Pulse uw", polarity=1, pulse_t=2.00000)
    return prg
def commands(cmd):
    import os
    import numpy as np
    iters = np.arange(12.5, 50, 0.7)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        freq1 = iters[j]
        cmd.set_var('freq', freq1)
        comm = "python3 /home/stronzio/remote_device_marconi/MarconiComm.py %g"%(1e3*freq1)
        os.system(comm)
        print('\n')
        print('Run #%d/%d, with variables:\nfreq = %g\n'%(j+1, len(iters), freq1))
        cmd.run(wait_end=True, add_time=22000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
