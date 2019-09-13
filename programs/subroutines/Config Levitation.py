prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10, "IGBT 4 Close")
    prg.add(20, "Delta 1 Voltage", 1.6000)
    prg.add(2060, "IGBT 2 Open")
    prg.add(2070, "IGBT 3 Close")
    prg.add(2090, "IGBT 5 Open")
    prg.add(2100, "Delta 1 Current", 12.000, functions=dict(value=lambda x: 2.232315e-6*cmd.get_var('tof')**3 - 1.164726e-3*cmd.get_var('tof')**2 + 1.986549e-1*cmd.get_var('tof') + 2.931988))
    prg.add(2100, "Delta 1 Current", 0.000, functions=dict(value=lambda x: cmd.get_var('Levitation_current')), enable=False)
    return prg
