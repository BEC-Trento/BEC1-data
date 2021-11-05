prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1500, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq')*1e6+cmd.get_var('RF_freq_delta')*1e3))
    prg.add(-900, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(230, "RF_freq", 0, functions=dict(frequency=lambda x: cmd.get_var('RF_freq2')*1e6-cmd.get_var('RF_freq_delta')*1e3, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(230, "RF_freq", 110, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_zero')*1e6, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(900, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime2'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(900, "Pulse uw with RF imaging m1", functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')), enable=False)
    prg.add(2100, "Pulse uw with RF imaging p1", functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')), enable=False)
    prg.add(3000, "RF_freq", 60, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    prg.add(3700, "RF_amp", 1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime_m1')+1e-3*cmd.get_var('marconi1_pulsetime_m1')))
    return prg
