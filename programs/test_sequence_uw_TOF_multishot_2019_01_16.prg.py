prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(10100000, "Picture SetRepumper")
    prg.add(10110000, "Picture SetImaging")
    prg.add(10610000, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(10829350, "Pulse Probe Na", polarity=1, pulse_t=0.00500)
    prg.add(10830096, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(10830440, "Pulse TTL2-12", polarity=1, pulse_t=0.95600)
    prg.add(10830450, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(10830470, "Pulse Probe Na", polarity=1, pulse_t=0.00500, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('uw_tau')))
    prg.add(11050570, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(11270120, "Pulse Probe Na", polarity=1, pulse_t=0.00500)
    prg.add(11270816, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(11271170, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau2')))
    prg.add(11271190, "Pulse Probe Na", polarity=1, pulse_t=0.00500, functions=dict(time=lambda x: x + 1e-3*cmd.get_var('uw_tau2')))
    prg.add(11491190, "Picture Levit 2017 - setup")
    prg.add(11493290, "Delta 1 Current", 13.200)
    prg.add(11511190, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(11983290, "Config Field OFF.sub")
    prg.add(11993320, "Picture FastStingray TOF Ready Trig2")
    prg.add(31993320, "All AOM On.sub")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 50, 4)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uw_tau1 = iters[j]
        cmd.set_var('uw_tau', uw_tau1)
        print('\n')
        print('Run #%d/%d, with variables:\nuw_tau = %g\n'%(j+1, len(iters), uw_tau1))
        cmd.run(wait_end=True, add_time=500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
