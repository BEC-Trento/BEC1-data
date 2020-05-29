prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(109000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000)
    prg.add(114000, "RF Sweep Trig ON")
    prg.add(1164000, "RF Sweep Trig OFF")
    prg.add(1264000, "rf_pulse")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.12, 13.37, 1.01)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        marconi1_pulsetime = iters[j]
        cmd.set_var('marconi1_pulsetime', marconi1_pulsetime)
        print('\n')
        print('Run #%d/%d, with variables:\nmarconi1_pulsetime = %g\n'%(j+1, len(iters), marconi1_pulsetime))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
