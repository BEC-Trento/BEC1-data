prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq')*1e6+cmd.get_var('RF_freq_delta')*1e3))
    prg.add(-1000, "RF_freq", 0, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_m1')*1e6+cmd.get_var('RF_freq_m1_delta')*1e3), enable=False)
    prg.add(-400, "RF_amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp')))
    prg.add(0, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(110, "RF_freq", 110, functions=dict(frequency=lambda x: cmd.get_var('RF_freq2')*1e6-cmd.get_var('RF_freq_delta')*1e3, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(700, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('marconi1_pulsetime2'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(750, "Probe z AOM TTL mix", functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')), enable=False)
    prg.add(800, "RF_amp", 100, functions=dict(amplitude=lambda x: cmd.get_var('RF_amp_dressing'), time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(1500, "RF_freq", 109, functions=dict(frequency=lambda x: cmd.get_var('RF_freq_zero')*1e6, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')))
    prg.add(2500, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('marconi1_pulsetime_dressing')*1e-3+cmd.get_var('dipole_mix_time')+cmd.get_var('dipole_hold3_time')-0.1, time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+1e-3*cmd.get_var('probe_z_pulsetime_mix')), enable=False)
    prg.add(3000, "Probe y AOM TTL long ", functions=dict(time=lambda x: x+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')), enable=False)
    return prg
