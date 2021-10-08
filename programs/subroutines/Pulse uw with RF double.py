prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq')*1e6+cmd.get_var('RF_freq_delta')*1e3))
    prg.add(-400, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(700, "RF_amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp_dressing')))
    prg.add(830, "RF_freq", 110, functions=dict(frequency=lambda x: cmd.get_var('RF_freq2')*1e6-cmd.get_var('RF_freq_delta')*1e3, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(830, "RF_freq", 0, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_zero')*1e6, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(900, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime2'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(1400, "RF_freq", 60, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(1900, "RF_amp", 1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    return prg
