prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B comp x ramp", start_t=0, stop_x=0, n_points=110, start_x=0, stop_t=1, functions=dict(stop_x=lambda x: cmd.get_var('Bx_GM')+cmd.get_var('Bx_tof_imaging'), start_x=lambda x: cmd.get_var('Bx_GM') + cmd.get_var('Bx_dipole_trap')))
    prg.add(1000, "B comp y ramp", start_t=0, stop_x=0, n_points=110, start_x=0, stop_t=1, functions=dict(stop_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_tof_imaging'), start_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_dipole_trap')))
    prg.add(2000, "B comp z ramp", start_t=0.0000, stop_x=0.000, n_points=110, start_x=1.000, stop_t=1.0000, functions=dict(stop_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_tof_imaging'), start_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_dipole_trap')))
    return prg
