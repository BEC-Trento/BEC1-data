prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq')*1e6))
    prg.add(-400, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(610, "RF_freq", 110, functions=dict(frequency=lambda x: cmd.get_var('RF_freq2')*1e6, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(700, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime2'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(800, "RF_amp", 100, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp_dressing'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime2')+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(1200, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_dressing'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime2')+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(1400, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime_dressing'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime2')+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(1600, "RF_amp", 1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+1e-3*cmd.get_var('marconi1_pulsetime_dressing')))
    return prg
