prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Mirrors MOT")
    prg.add(100, "B comp x", 1.4, functions=dict(value=lambda x: cmd.get_var('Bx_MOT')))
    prg.add(200, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_MOT')))
    prg.add(300, "B comp z", 0.8000, functions=dict(value=lambda x: cmd.get_var('Bz_MOT')))
    prg.add(400, "B grad x", 0.2000)
    prg.add(450, "IGBT B grad x OFF")
    prg.add(500, "Delta 1 Voltage", 6.0000)
    prg.add(1000, "Delta 2 Voltage", 0.0000, enable=False)
    prg.add(1500, "Mirrors MOT")
    prg.add(2000, "Pulse MOT Na OFF")
    prg.add(3000, "Na 3D MOT cool (-) ON")
    prg.add(3500, "Shutter 3DMOT cool Na Open")
    prg.add(4000, "Na 3D MOT cool (+) freq", 102.00, functions=dict(frequency=lambda x: 110+cmd.get_var('MOT3D_det')/2))
    prg.add(4500, "Na 3D MOT cool (-) freq", 118.00, functions=dict(frequency=lambda x: 110-cmd.get_var('MOT3D_det')/2))
    prg.add(5000, "Na 3D MOT cool (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('MOT3D_amp')))
    prg.add(5500, "Na 3D MOT cool (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('MOT3D_amp')))
    prg.add(6000, "Shutter Gray molasses Close")
    prg.add(6500, "AOM GM Amp ch1 (+)", 0)
    prg.add(7000, "Na Gray molasses (+) freq", 80.00)
    prg.add(7500, "AOM GM Amp ch2 (-)", 0)
    prg.add(8000, "Na Gray molasses (-) freq", 80.00)
    prg.add(8500, "Delta 1 Current", 12.000, functions=dict(value=lambda x: cmd.get_var('MOT_current')))
    prg.add(9000, "Shutter Dark Spot Open")
    prg.add(9500, "Shutter repump Na Open")
    prg.add(10000, "Na Repumper Tune (+) freq", 1712.0, functions=dict(frequency=lambda x: cmd.get_var('Rep_freq')))
    prg.add(10500, "Na Repumper1 (+) Amp", 1000)
    prg.add(11000, "Na Repumper2 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('DS_amp')))
    prg.add(11500, "TTL Dark Spot ON")
    prg.add(12000, "TTL Repumper MOT OFF")
    prg.add(12500, "Shutter EOM Na Open")
    prg.add(13500, "Na 2D MOT (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('MOT2D_amp')))
    prg.add(14000, "Na 2D MOT (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('MOT2D_amp')))
    prg.add(14500, "Na 2D MOT (-) freq", 100.50, functions=dict(frequency=lambda x: 95.5-cmd.get_var('MOT2D_det')/2))
    prg.add(15000, "Na 2D MOT (+) freq", 90.50, functions=dict(frequency=lambda x: 95.5+cmd.get_var('MOT2D_det')/2))
    prg.add(15500, "TTL Repumper GM OFF")
    prg.add(16000, "Na Zeeman slower (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('zs_amp')))
    prg.add(16500, "Na Zeeman slower (-) freq", 300.0, functions=dict(frequency=lambda x: cmd.get_var('zs_det')))
    prg.add(17000, "Shutter Probe/Push Open")
    prg.add(18000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('push_det')/2))
    prg.add(18500, "Na Push (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('push_det')/2))
    prg.add(19000, "Na Probe/Push (-) amp", 500, functions=dict(amplitude=lambda x: cmd.get_var('push_amp')))
    prg.add(19500, "Na Push (+) amp", 500, functions=dict(amplitude=lambda x: cmd.get_var('push_amp')))
    prg.add(20000, "TTL Push ON")
    prg.add(21000, "TTL Probe y OFF")
    prg.add(22000, "TTL Probe z OFF")
    prg.add(22500, "IGBT B comp x ON")
    prg.add(23000, "IGBT B comp y ON")
    prg.add(23500, "IGBT B comp z ON")
    prg.add(24000, "IGBT B grad x OFF")
    prg.add(24500, "Shutter Gray molasses Open")
    prg.add(25000, "Config MOT.sub")
    prg.add(40000, "Na Gray molasses (+) freq", 112.50)
    prg.add(42000, "Na Gray molasses (-) freq", 87.50)
    prg.add(44000, "AOM GM Amp ch1 (+)", 1000)
    prg.add(46000, "AOM GM Amp ch2 (-)", 1000)
    prg.add(1046000, "open_probe")
    prg.add(16025000, "MOT lights Off TTL.sub", enable=False)
    return prg
