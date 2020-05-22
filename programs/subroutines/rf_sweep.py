prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-400, "Evaporation freq", 0, functions=dict(frequency=lambda x: cmd.get_var('rf_freq1')*1e6))
    prg.add(0, "Evaporation amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('rf_amp')))
    prg.add(400, "Evaporation ramp", start_t=0.0000, func_args="freq1=1.082e6, freq2=1.084e6, duration=10", n_points=25, func="freq1+ (freq2-freq1)/duration *t", stop_t=10.0000, functions=dict(func_args=lambda x: 'freq1={}, freq2={}, duration={}'.format(cmd.get_var('rf_freq1')*1e6, cmd.get_var('rf_freq2')*1e6, cmd.get_var('rf_pulse_time')*1e-3), stop_t=lambda x: cmd.get_var('rf_pulse_time'), n_points=lambda x: cmd.get_var('rf_number_points')))
    prg.add(800, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('rf_pulse_time')))
    return prg
