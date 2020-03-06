prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Evaporation_setfull", ch0_amp=1000, ch0_freq=24000000.000, ch1_freq=24000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=1)
    prg.add(10000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=330, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(20000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=340, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_time')*1e-3, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: x +cmd.get_var('evap1_time')), enable=False)
    prg.add(24000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')))
    prg.add(30000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=340, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap3_fend')*1e6, cmd.get_var('evap3_time')*1e-3, cmd.get_var('evap3_tau')), stop_t=lambda x: cmd.get_var('evap3_time'), time=lambda x: x +cmd.get_var('evap1_time')+cmd.get_var('evap2_time')), enable=False)
    prg.add(31000, "Evaporation amp", 1, functions=dict(time=lambda x: x +cmd.get_var('evap1_time') + cmd.get_var('evap2_time') + cmd.get_var('evap3_time')))
    prg.add(34000, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=151, start_x=0.000, stop_t=0.0000, functions=dict(time=lambda x: x + cmd.get_var('evap1_time') + cmd.get_var('evap2_time'), start_x=lambda x: cmd.get_var('Quad_current_rampdown'), stop_t=lambda x: cmd.get_var('Quad_rampdown2_time'), stop_x=lambda x: cmd.get_var('Quad_rampdown2_current')))
    return prg
