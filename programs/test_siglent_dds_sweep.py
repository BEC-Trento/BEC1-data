prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(5000000, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000)
    prg.add(5000026, "Rf Sweep Siglent", functions=dict(time=lambda x: x + cmd.get_var('_delay')))
    prg.add(5000026, "Evaporation_setfull", ch1_freq=24000000.000, ch0_amp=1000, ch0_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1, functions=dict(ch0_freq=lambda x: 1e6 * cmd.get_var('siglent1_freq_start')))
    prg.add(5000426, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.082e6, freq2=1.084e6, duration=10", n_points=1, func="freq1+ (freq2-freq1)/duration *t", stop_t=5000.0000, functions=dict(func_args=lambda x: 'freq1={f1}, freq2={f2}, duration={duration}'.format(f1=1e6*cmd.get_var('siglent1_freq_start'), f2=1e6*cmd.get_var('siglent1_freq_stop'), duration=1e-3*cmd.get_var('siglent1_sweep_time')), stop_t=lambda x: cmd.get_var('siglent1_sweep_time'), n_points=lambda x: int(cmd.get_var('siglent1_sweep_time') / 0.04)))
    prg.add(5000826, "Evaporation amp", 1, functions=dict(time=lambda x: x + cmd.get_var('siglent1_sweep_time')))
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
