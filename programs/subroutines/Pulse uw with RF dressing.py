prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq')*1e6))
    prg.add(-400, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(110, "RF_freq", 110, functions=dict(frequency=lambda x: cmd.get_var('RF_freq2')*1e6, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(700, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime2'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(800, "RF_amp", 100, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp_dressing'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(1500, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_dressing')*1e6, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(2500, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('marconi1_pulsetime_dressing')*1e-3+cmd.get_var('dipole_hold3_time')+0.6404, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(2600, "RF_amp", 1, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+cmd.get_var('dipole_hold3_time')+1e-3*cmd.get_var('marconi1_pulsetime_dressing')+cmd.get_var('mix_time')))
    prg.add(3200, "RF_freq", 60, functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+cmd.get_var('dipole_hold3_time')+1e-3*cmd.get_var('marconi1_pulsetime_dressing')+cmd.get_var('mix_time')))
    return prg
