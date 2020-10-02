prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-13460, "Setup_imaging", functions=dict(time=lambda x: x + cmd.get_var('tof') - 1), enable=False)
    prg.add(0, "Config Levitation")
    prg.add(0, "Config Field OFF.sub", functions=dict(time=lambda x: x + cmd.get_var('tof') - 1))
    prg.add(0, "BEC_imaging", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    return prg
