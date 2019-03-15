prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Zeeman slower (-) freq", 305.0, functions=dict(frequency=lambda x: cmd.get_var('zs_det')))
    return prg
