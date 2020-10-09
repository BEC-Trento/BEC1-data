prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B comp x", 0.0, functions=dict(value=lambda x: cmd.get_var('Bx_GM') + cmd.get_var('Bx_bottom') + cmd.get_var('Bx_kick'), time=lambda x: x - cmd.get_var('B_kick_time')))
    prg.add(0, "B comp x", 0.0, functions=dict(value=lambda x: cmd.get_var('Bx_GM') + cmd.get_var('Bx_bottom')))
    return prg
