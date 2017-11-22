prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Set MOT.sub")
    prg.add(1000000, "Delta 1 Current", 15.000)
    prg.add(1100000, "Delta 1 Voltage", 20.0000)
    prg.add(2000000, "Config Field OFF.sub", enable=False)
    prg.add(2100000, "Config All Rele Open")
    prg.add(3000000, "uniform B field x Rele IGBT config", enable=False)
    prg.add(4000000, "Config GRAD up.sub", enable=False)
    prg.add(5000000, "Config GRAD down.sub", enable=False)
    prg.add(6000000, "Config MOT.sub", enable=False)
    prg.add(7000000, "Config MT compr.sub", enable=False)
    prg.add(8000000, "Config MT not compr.sub", enable=False)
    prg.add(9000000, "Config Feshbach.sub", enable=False)
    prg.add(10000000, "Config pinch + comp.sub", enable=False)
    return prg
