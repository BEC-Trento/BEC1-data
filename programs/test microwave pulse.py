prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000)
    prg.add(10000170, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('marconi1_pulsetime')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1.77143e+09, 1.77165e+09, 30000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        marconi1_freq = iters[j]
        cmd.set_var('marconi1_freq', marconi1_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nmarconi1_freq = %g\n'%(j+1, len(iters), marconi1_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
