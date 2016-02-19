prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(1000, "General Trigger OFF")
    prg.add(10000, "Config Feshbach.sub")
    prg.add(100000, "Delta 1 Voltage", 0.000000)
    prg.add(110000, "Delta 2 Voltage", 30.000000)
    prg.add(120000, "Delta 1 Current", 200.000000)
    prg.add(130000, "Delta 2 Current", 0.000000)
    prg.add(999990, "General Trigger ON")
    prg.add(1500000, "Delta 1 Current", 200.000000, enable=False)
    prg.add(1501000, "Delta 2 Voltage", 30.000000, enable=False)
    prg.add(1502000, "Delta 2 Current", 200.000000, enable=False)
    prg.add(10000000, "Config Field OFF.sub")
    return prg
