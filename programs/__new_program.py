prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Ramp_bias_field")
    prg.add(10000000, "Config Levitation")
    prg.add(10169500, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=50, start_x=0.000, stop_t=1.0000, functions=dict(stop_t=lambda x: cmd.get_var('levitation_switch_off_time'), start_x=lambda x: cmd.get_var('Levitation_current')))
    prg.add(10169900, "Scope 1 Trigger Pulse", polarity=1, pulse_t=1.00000)
    prg.add(10170000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('levitation_switch_off_time')))
    return prg
