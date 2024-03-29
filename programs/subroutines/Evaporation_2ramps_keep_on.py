prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Evaporation amp", 1000)
    prg.add(1000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=330, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fstart')*1e6, cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap1_time')*1e-3, cmd.get_var('evap1_tau')), stop_t=lambda x: cmd.get_var('evap1_time')))
    prg.add(2000, "Evaporation ramp", start_t=0.0000, func_args="a=40e6, b=4e6, duration=10, tau=1", n_points=340, func="(b - a * exp(-duration / tau) + (a - b) * exp(-t / tau)) / (1 - exp(-duration / tau))", stop_t=5000.0000, functions=dict(func_args=lambda x: 'a={}, b={}, duration={}, tau={}'.format(cmd.get_var('evap1_fend')*1e6, cmd.get_var('evap2_fend')*1e6, cmd.get_var('evap2_time')*1e-3, cmd.get_var('evap2_tau')), stop_t=lambda x: cmd.get_var('evap2_time'), time=lambda x: x +cmd.get_var('evap1_time')))
    prg.add(24000, "Quad_RampDOWN", functions=dict(time=lambda x: x + cmd.get_var('evap1_time')))
    return prg
