prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01000)
    prg.add(170, "Pulse uw", polarity=1, pulse_t=0.00200, functions=dict(pulse_t=lambda x: cmd.get_var('marconi1_pulsetime')))
    return prg
