prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(1, "B comp x ramp", start_t=0, stop_x=0, n_points=2, start_x=0, stop_t=0.02, functions=dict(stop_x=lambda x: cmd.get_var('Bx_dipole_zero'), start_x=lambda x: cmd.get_var('Bx_GM')+cmd.get_var('Bx_dipole_trap')))
    prg.add(51, "B comp y ramp", start_t=0, stop_x=0, n_points=2, start_x=0, stop_t=0.02, functions=dict(start_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_dipole_trap'), stop_x=lambda x: cmd.get_var('By_dipole_zero')))
    prg.add(101, "B comp z ramp", start_t=0.0000, stop_x=0.000, n_points=2, start_x=0.000, stop_t=0.0200, functions=dict(stop_x=lambda x: cmd.get_var('Bz_dipole_zero'), start_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_dipole_trap')))
    prg.add(500001, "B comp x ramp", start_t=0, stop_x=0, n_points=2, start_x=0, stop_t=0.02, functions=dict(start_x=lambda x: cmd.get_var('Bx_dipole_zero'), stop_x=lambda x: cmd.get_var('Bx_GM')+cmd.get_var('Bx_dipole_trap')))
    prg.add(500051, "B comp y ramp", start_t=0, stop_x=0, n_points=2, start_x=0, stop_t=0.02, functions=dict(start_x=lambda x: cmd.get_var('By_dipole_zero'), stop_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_dipole_trap')))
    prg.add(500101, "B comp z ramp", start_t=0.0000, stop_x=0.000, n_points=2, start_x=0.000, stop_t=0.0200, functions=dict(stop_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_dipole_trap'), start_x=lambda x: cmd.get_var('Bz_dipole_zero')))
    return prg
