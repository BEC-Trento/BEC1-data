prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B comp x ramp", start_t=0, stop_x=0, n_points=100, start_x=0, stop_t=2, functions=dict(stop_x=lambda x: cmd.get_var('Bx_GM')+cmd.get_var('Bx_dipole_trap'), start_x=lambda x: cmd.get_var('Bx_GM')+cmd.get_var('Bx_bottom') , time=lambda x: x+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('Quad_rampdown2_time')))
    prg.add(10000, "B comp y ramp", start_t=0, stop_x=0, n_points=100, start_x=0, stop_t=50, functions=dict(stop_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_dipole_trap'), start_x=lambda x: cmd.get_var('By_GM')+cmd.get_var('By_bottom')))
    prg.add(20000, "B comp z ramp", start_t=0.0000, stop_x=0.000, n_points=100, start_x=1.000, stop_t=50.0000, functions=dict(stop_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_tof_imaging'), start_x=lambda x: cmd.get_var('Bz_GM')+cmd.get_var('Bz_bottom')))
    return prg
