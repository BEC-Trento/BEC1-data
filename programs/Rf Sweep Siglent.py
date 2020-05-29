prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "RF Sweep Trig ON")
    prg.add(0, "RF Sweep Trig OFF", functions=dict(time=lambda x: x+cmd.get_var('siglent1_sweep_time')))
    return prg
