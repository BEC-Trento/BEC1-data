prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-8000, "Delta 1 Current", 50.000, functions=dict(value=lambda x: cmd.get_var('Quad_current')))
    prg.add(-500, "Delta 1 Voltage", 20.0000, functions=dict(value=lambda x: cmd.get_var('Quad_voltage'), funct_enable=False))
    prg.add(0, "Config MOT.sub")
    return prg
