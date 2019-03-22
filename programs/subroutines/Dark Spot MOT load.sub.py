prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-400, "Na 3D MOT cool (-) freq", 120.00, functions=dict(frequency=lambda x: 110-cmd.get_var('MOT3D_det')/2))
    prg.add(0, "TTL Dark Spot ON")
    prg.add(400, "TTL Repumper MOT OFF")
    prg.add(800, "Na 3D MOT cool (+) freq", 100.00, functions=dict(frequency=lambda x: 110+cmd.get_var('MOT3D_det')/2))
    return prg
