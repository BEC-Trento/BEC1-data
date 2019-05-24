prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-10000, "Delta 2 Voltage", 30.0000)
    prg.add(-8000, "Delta 1 Current", 200.000, functions=dict(value=lambda x: cmd.get_var('Quad_current')))
    prg.add(-500, "Delta 1 Voltage", 30.0000, functions=dict(value=lambda x: cmd.get_var('Quad_voltage'), funct_enable=False), enable=False)
    prg.add(0, "Config MOT.sub")
    prg.add(120, "ConfigMOT_to_Ioffe.sub")
    prg.add(50000, "Delta 1 Voltage", 28.0000)
    return prg
