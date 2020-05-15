prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-400, "Evaporation freq", 0, functions=dict(frequency=lambda x: cmd.get_var('rf_freq1')*1e6))
    prg.add(0, "Evaporation amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('rf_amp')))
    prg.add(0, "Evaporation amp", 1, functions=dict(time=lambda x: cmd.get_var('rf_pulse_time')))
    return prg
