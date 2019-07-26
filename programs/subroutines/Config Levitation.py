prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10, "IGBT 4 Close")
    prg.add(20, "Delta 1 Voltage", 1.6000)
    prg.add(2060, "IGBT 2 Open")
    prg.add(2070, "IGBT 3 Close")
    prg.add(2090, "IGBT 5 Open")
    prg.add(2100, "Delta 1 Current", 12.000, functions=dict(value=lambda x: cmd.get_var('Levitation_current')))
    return prg
