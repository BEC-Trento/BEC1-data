prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-40000, "B grad x", 0.0000, functions=dict(value=lambda x: cmd.get_var('Bx_grad')))
    prg.add(0, "IGBT B grad x ON")
    prg.add(0, "IGBT B grad x OFF", functions=dict(time=lambda x: x + cmd.get_var('B_kick_time')))
    return prg
