prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-9000, "B comp x", 3500.0, functions=dict(value=lambda x: cmd.get_var('Bx_MT')))
    prg.add(-8000, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_MT')))
    prg.add(-7000, "B comp z", 0.0000, functions=dict(value=lambda x: cmd.get_var('Bz_MT')))
    prg.add(0, "IGBT 3 Open")
    prg.add(10, "IGBT 2 Close")
    return prg
