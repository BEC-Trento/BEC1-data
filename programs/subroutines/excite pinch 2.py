prg_comment = ""
prg_version = "0.7"
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
    prg.add(490000, "Delta 2 Voltage", 30.0000, enable=False)
    prg.add(490500, "TTL2-12 ON")
    prg.add(491000, "Delta 1 Current ramp", start_t=0.0000, stop_x=1.000, n_points=200, start_x=0.000, stop_t=48.0000)
    prg.add(991000, "TTL2-12 OFF")
    prg.add(992000, "IGBT 1 pinch", -10.0000)
    prg.add(992100, "IGBT 4 Open")
    prg.add(992200, "IGBT 5 Open")
    prg.add(992400, "Delta 1 Current", 0.000)
    prg.add(997000, "ReleConfigBacktoSG2")
    prg.add(1492000, "IGBT 5 Open")
    return prg
