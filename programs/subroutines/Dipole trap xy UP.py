prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-60509000, "Dipole Trap x DAC V", 0.000)
    prg.add(-60500000, "Dipole Trap y DAC V", 0.000)
    prg.add(-60051000, "Dipole Trap y AOM (-) freq", 110.00)
    prg.add(-60020000, "Dipole Trap x AOM (+) freq", 110.00)
    prg.add(0, "Dipole Trap y ramp", start_t=0.0000, stop_x=4.000, n_points=100, start_x=-0.050, stop_t=10.0000, functions=dict(stop_t=lambda x: cmd.get_var('dipole_turn_on_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V')), enable=False)
    prg.add(4, "Dipole Trap y DAC V", 10.000, functions=dict(value=lambda x: cmd.get_var('Dipole_y_DAC_V')))
    prg.add(40, "Dipole Trap x ramp", start_t=0.0000, stop_x=5.000, n_points=100, start_x=0.050, stop_t=10.0000, functions=dict(stop_t=lambda x: cmd.get_var('dipole_turn_on_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V')), enable=False)
    prg.add(10000, "Dipole Trap x DAC V", 10.000, functions=dict(value=lambda x: cmd.get_var('Dipole_x_DAC_V')))
    return prg
