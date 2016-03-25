prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", -10.0000)
    prg.add(100, "IGBT 2 pinch+comp", -10.0000)
    prg.add(200, "IGBT 3 Open")
    prg.add(300, "IGBT 4 Close")
    prg.add(400, "IGBT 5 Open")
    prg.add(500, "IGBT 6 Open")
    prg.add(1000, "Rele 5 Close")
    prg.add(2000, "Rele 3 Open")
    prg.add(3000, "Rele 4 Close")
    prg.add(490000, "Delta 2 Voltage", 30.0000)
    prg.add(491000, "Delta 1 Current", 200.000)
    prg.add(597990, "IGBT 1 pinch", 10.0000)
    prg.add(599490, "IGBT 1 pinch", -10.0000)
    prg.add(599590, "IGBT 4 Open")
    prg.add(599690, "IGBT 5 Open")
    prg.add(599890, "Delta 1 Current", 0.000)
    prg.add(604490, "ReleConfigBacktoSG2")
    prg.add(1099490, "IGBT 5 Open")
    return prg
