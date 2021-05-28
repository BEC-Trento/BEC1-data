prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-509000, "Dipole Trap x DAC V", 0.000)
    prg.add(-500000, "Dipole Trap y DAC V", 0.000)
    prg.add(-51000, "Dipole Trap y AOM (-) freq", 110.00)
    prg.add(-50000, "Dipole Trap x AOM (+) freq", 110.00)
    prg.add(0, "Dipole Trap y DAC V", 10.000, functions=dict(value=lambda x: cmd.get_var('Dipole_y_DAC_V')))
    prg.add(10000, "Dipole Trap x DAC V", 10.000, functions=dict(value=lambda x: cmd.get_var('Dipole_x_DAC_V')))
    return prg
