prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-15167, "B comp y", 1.0000, functions=dict(value=lambda x: cmd.get_var('By_OP')))
    prg.add(-10531, "B comp x", 1.6, functions=dict(value=lambda x: cmd.get_var('Bx_OP')))
    prg.add(135, "TTL Repumper MOT ON", enable=False)
    prg.add(1135, "TTL Repumper MOT OFF", enable=False)
    return prg
