prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01048)
    prg.add(100, "B comp x func", start_t=0.0000, func_args="amp=0.5, freq=100, offset=0.6", n_points=100, func="amp*sin(2*pi*freq*t) + offset", stop_t=500.0000)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(14.5, 50, 3)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        mod_freq = iters[j]
        cmd.set_var('mod_freq', mod_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nmod_freq = %g\n'%(j+1, len(iters), mod_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
