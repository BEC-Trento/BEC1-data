prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2000, "Compensation gravity", enable=False)
    prg.add(0, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(start_x=lambda x: cmd.get_var('Dipole_x_DAC_V'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V_final')))
    prg.add(100, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(start_x=lambda x: cmd.get_var('Dipole_y_DAC_V'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V_final')))
    prg.add(2024100, "Pulse uw with RF dressing", enable=False)
    prg.add(4000000, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(time=lambda x: x+cmd.get_var('dipole_evap_time'), start_x=lambda x: cmd.get_var('Dipole_x_DAC_V_final'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V')))
    prg.add(4001000, "Dipole Trap y ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000, functions=dict(time=lambda x: x+cmd.get_var('dipole_evap_time'), start_x=lambda x: cmd.get_var('Dipole_y_DAC_V_final'), stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V')))
    prg.add(4001010, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=50, start_x=0.000, stop_t=200.0000, functions=dict(time=lambda x: x+cmd.get_var('dipole_evap_time'), start_x=lambda x: cmd.get_var('Gravity_current_comp')), enable=False)
    prg.add(7002000, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('dipole_evap_time')), enable=False)
    prg.add(7510000, "B comp x ramp", start_t=0, stop_x=0, n_points=50, start_x=5, stop_t=100, functions=dict(time=lambda x: x+cmd.get_var('dipole_evap_time'), start_x=lambda x: 5, stop_x=lambda x: cmd.get_var('Bx_dipole_trap')), enable=False)
    return prg
