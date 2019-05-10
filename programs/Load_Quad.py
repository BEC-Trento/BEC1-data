prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Delta 1 Current", 15.000, functions=dict(value=lambda x: cmd.get_var('Quad_current')))
    prg.add(50, "Delta 1 Voltage", 15.0000)
    prg.add(1000, "Config MOT.sub")
    return prg
