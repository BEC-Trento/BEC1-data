prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(start_x=lambda x: cmd.get_var('Dipole_x_DAC_V'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V_final')))
    prg.add(100, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(start_x=lambda x: cmd.get_var('Dipole_y_DAC_V'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V_final')))
    prg.add(2000000, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V'), start_x=lambda x: cmd.get_var('Dipole_x_DAC_V_final'), time=lambda x: x+cmd.get_var('dipole_evap_time')))
    prg.add(2001000, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V'), start_x=lambda x: cmd.get_var('Dipole_y_DAC_V_final'), time=lambda x: x+cmd.get_var('dipole_evap_time')))
    return prg
