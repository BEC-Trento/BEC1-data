prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1210, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000, enable=False)
    prg.add(0, "Dipole Trap x DAC V", 0.000)
    prg.add(1000, "Dipole Trap y DAC V", 0.000)
    prg.add(2000, "Dipole Trap x AOM (+) Amp", 1000)
    prg.add(3000, "Dipole Trap y AOM (-) Amp", 1000)
    prg.add(4000, "Dipole Trap x AOM (+) freq", 60.00)
    prg.add(5000, "Dipole Trap y AOM (-) freq", 60.00)
    prg.add(1000000, "Dipole Trap x DAC V", 5.000, functions=dict(value=lambda x: cmd.get_var('Dipole_x_DAC_V')))
    prg.add(1010000, "Dipole Trap y DAC V", 5.000, functions=dict(value=lambda x: cmd.get_var('Dipole_y_DAC_V')))
    return prg
