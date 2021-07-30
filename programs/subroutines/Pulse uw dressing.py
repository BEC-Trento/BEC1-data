prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_dressing')*1e6))
    prg.add(-400, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp_dressing')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('mix_time')-1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(400, "RF_amp", 1, functions=dict(time=lambda x: x+cmd.get_var('mix_time')))
    prg.add(810, "RF_freq", 60, functions=dict(time=lambda x: x+cmd.get_var('mix_time')))
    return prg
