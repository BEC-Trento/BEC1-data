prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Dipole trap xy ON", functions=dict(time=lambda x: x+cmd.get_var('dipole_delay_time')))
    prg.add(0, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=100, start_x=100.000, stop_t=2000.0000, functions=dict(stop_t=lambda x: cmd.get_var('Quad_rampdown2_time'), stop_x=lambda x: cmd.get_var('Quad_rampdown2_current'), start_x=lambda x: cmd.get_var('Quad_current_rampdown'), time=lambda x: x+cmd.get_var('magnetic_trap_hold')))
    prg.add(0, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')))
    prg.add(2100, "Evaporation amp", 1)
    prg.add(3100, "Evaporation freq", 5, functions=dict(frequency=lambda x: 5e6))
    prg.add(100000, "Ramp_bias_field")
    return prg
