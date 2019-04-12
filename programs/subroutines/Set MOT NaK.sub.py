prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(1000, "Delta 1 Current", 12.000)
    prg.add(1100, "Delta 2 Current", 200.000)
    prg.add(1200, "Delta 1 Voltage", 30.0000)
    prg.add(1300, "Delta 2 Voltage", 0.0000)
    prg.add(5000, "Mirrors MOT")
    prg.add(7200, "Pulse MOT Na OFF")
    prg.add(7400, "Na Probe/Push (+) ON")
    prg.add(7600, "Na 3D MOT cool (-) ON")
    prg.add(10000, "Shutter 3DMOT cool Na Open")
    prg.add(26000, "Na 3D MOT cool (+) freq", 98.50)
    prg.add(26500, "Na 3D MOT cool (-) freq", 121.50)
    prg.add(27000, "Na 3D MOT cool (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('MOT3D_amp')))
    prg.add(27500, "Na 3D MOT cool (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('MOT3D_amp')))
    prg.add(32000, "Shutter Gray molasses Close")
    prg.add(100000, "Shutter Repump2 Close")
    prg.add(110000, "Shutter repump Na Open")
    prg.add(120000, "Na Repumper Tune (+) freq", 1712.0, functions=dict(frequency=lambda x: cmd.get_var('Rep_freq')))
    prg.add(130000, "Na Repumper1 (+) Amp", 1000)
    prg.add(140000, "Na Repumper2 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(150000, "TTL Dark Spot OFF")
    prg.add(160000, "TTL Repumper MOT ON")
    prg.add(190000, "Shutter EOM Na Open")
    prg.add(195000, "Shutter Bragg Close")
    prg.add(200000, "Na 2D MOT (+) Amp", 1000)
    prg.add(210000, "Na 2D MOT (-) Amp", 1000)
    prg.add(220000, "Na 2D MOT (-) freq", 100.50)
    prg.add(230000, "Na 2D MOT (+) freq", 90.50)
    prg.add(290000, "TTL Repumper GM OFF")
    prg.add(300000, "Na Zeeman slower (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('zs_amp'), funct_enable=False))
    prg.add(310000, "Na Zeeman slower (-) freq", 300.0, functions=dict(frequency=lambda x: cmd.get_var('zs_det'), funct_enable=False))
    prg.add(330000, "Shutter Probe Na Close")
    prg.add(340000, "Shutter Push Na Open")
    prg.add(350000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('push_det')/2, funct_enable=False))
    prg.add(360000, "Na Probe/Push (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('push_det')/2, funct_enable=False))
    prg.add(370000, "Na Probe/Push (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('push_amp'), funct_enable=False))
    prg.add(380000, "Na Probe/Push (+) Amp", 1000)
    prg.add(390000, "Bcomp y Sign Minus", enable=False)
    prg.add(390000, "Bcomp y Sign Plus")
    prg.add(400000, "Bcomp z Sign Plus")
    prg.add(410000, "B comp x", 695.0, functions=dict(value=lambda x: cmd.get_var('B_comp_x')))
    prg.add(420000, "B comp y", 0.0700, functions=dict(value=lambda x: cmd.get_var('B_comp_y')))
    prg.add(430000, "B comp z", 0.7300, functions=dict(value=lambda x: cmd.get_var('B_comp_z')))
    prg.add(440000, "IGBT B comp x ON")
    prg.add(450000, "IGBT B comp y ON")
    prg.add(460000, "IGBT B comp z ON")
    prg.add(470000, "Bx Grad OFF")
    return prg
