prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_GM') + cmd.get_var('By_bottom') + cmd.get_var('By_kick'), time=lambda x: x - cmd.get_var('B_kick_time')))
    prg.add(0, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_GM') + cmd.get_var('By_bottom')))
    return prg
