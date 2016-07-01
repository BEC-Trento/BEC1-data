prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4299000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4259000, "Na Dark Spot Amp", 1)
    prg.add(-4249000, "Na Repumper MOT Amp", 1)
    prg.add(-2909000, "Shutter repump Na Open")
    prg.add(-2899000, "Shutter Probe Na Open")
    prg.add(-2409000, "Na Probe/Push (-) Amp", 1)
    prg.add(-2399000, "Na Probe/Push (+) Amp", 1)
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2000000, "Shutter 3DMOT cool Na Open")
    prg.add(-500000, "IGBT B comp y ON")
    prg.add(-451000, "IGBT 5 Open")
    prg.add(-450000, "IGBT 4 Open")
    prg.add(-441000, "Delta 1 Current", 40.000)
    prg.add(-440000, "Delta 2 Voltage", 30.0000)
    prg.add(0, "IGBT 1 pinch", -10.0000)
    prg.add(20, "IGBT 3 Open")
    prg.add(60, "IGBT 2 pinch+comp", -10.0000)
    prg.add(140, "IGBT 3 Close")
    prg.add(150, "IGBT 4 Close")
    prg.add(20150, "IGBT 1 pinch", -10.0000)
    prg.add(20160, "IGBT 2 pinch+comp", -10.0000)
    prg.add(20170, "IGBT 3 Open")
    prg.add(20180, "IGBT 4 Open")
    prg.add(20190, "IGBT 5 Open")
    prg.add(23650, "Na Repumper MOT Amp", 400)
    prg.add(24150, "Na Repumper1 (+) Amp", 1000)
    prg.add(24550, "Na Repumper Tune (+) freq", 2000.0)
    prg.add(24950, "Na Probe/Push (+) freq", 110.00)
    prg.add(25350, "Na Probe/Push (-) freq", 110.00)
    prg.add(25650, "Trig ON Stingray 1")
    prg.add(25750, "Na Probe/Push (+) Amp", 1000)
    prg.add(26150, "Na Probe/Push (-) Amp", 1000)
    prg.add(27150, "Na Probe/Push (-) Amp", 1)
    prg.add(27650, "Trig OFF Stingray 1")
    prg.add(276150, "Shutter Probe Na Close")
    prg.add(1025650, "Trig ON Stingray 1")
    prg.add(1026150, "Na Probe/Push (-) Amp", 1000)
    prg.add(1027150, "Na Probe/Push (-) Amp", 1)
    prg.add(1027650, "Trig OFF Stingray 1")
    prg.add(1036150, "Na Repumper MOT Amp", 1)
    prg.add(1046150, "Na Repumper1 (+) Amp", 1)
    prg.add(2025650, "Trig ON Stingray 1")
    prg.add(2027650, "Trig OFF Stingray 1")
    prg.add(3025650, "Trig ON Stingray 1")
    prg.add(3027650, "Trig OFF Stingray 1")
    prg.add(4026150, "B comp y", 0.0000, enable=False)
    prg.add(4125150, "IGBT B comp y OFF")
    return prg