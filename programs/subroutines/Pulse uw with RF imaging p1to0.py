prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "RF_freq", 108, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_p1')*1e6+cmd.get_var('RF_freq_delta')*1e3))
    prg.add(-400, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime_p1')))
    prg.add(540, "RF_amp", 1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    prg.add(1520, "RF_freq", 60, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime_m1')), enable=False)
    return prg
