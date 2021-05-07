prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1500000, "Dipole Trap y AOM (-) freq", 110.00, functions=dict(frequency=lambda x: cmd.get_var('Dipole_y_AOM_freq')))
    prg.add(-1000000, "Dipole Trap y AOM (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Dipole_y_AOM_amp')))
    prg.add(0, "Dipole Trap y DAC V", 4.0000, functions=dict(value=lambda x: cmd.get_var('Dipole_y_DAC_V')))
    prg.add(10000, "Dipole Trap y DAC V", 0.0000, functions=dict(time=lambda x: x+cmd.get_var('evap3_time')))
    prg.add(10020, "Dipole Trap x AOM (+) Amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap3_time')))
    prg.add(10520, "Dipole Trap x AOM (+) freq", 60.00, functions=dict(time=lambda x: x+cmd.get_var('evap3_time')))
    return prg
