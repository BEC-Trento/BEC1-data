prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-70000, "IGBT B comp z OFF")
    prg.add(-55000, "IGBT 1 pinch", -10.0000)
    prg.add(-54990, "IGBT 2 pinch+comp", -10.0000)
    prg.add(-54980, "IGBT 3 Open")
    prg.add(-54970, "IGBT 4 Open")
    prg.add(-54960, "IGBT 5 Open")
    prg.add(-50000, "IGBT B comp z OFF")
    prg.add(-18000, "B comp y", 1.0000)
    prg.add(0, "Picture NaK.sub")
    prg.add(0, "Picture NaK Repump Off.sub", enable=False)
    prg.add(0, "Picture NaK Hamamatsu.sub", enable=False)
    prg.add(0, "Picture NaK TrigSlow.sub", enable=False)
    prg.add(3501000, "Shutter Optical Levit Close", enable=False)
    prg.add(4002000, "B comp y", 0.0000, enable=False)
    prg.add(4101000, "IGBT B comp y OFF", enable=False)
    prg.add(8501000, "Optical Levit ON", enable=False)
    return prg
