prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "Delta 1 Voltage", 0.000000)
    prg.add(20000, "Delta 1 Current", 0.000000)
    prg.add(5000000, "Delta 1 Voltage", 10.000000)
    prg.add(10000000, "Delta 1 Current", 100.000000)
    prg.add(20000000, "Delta 1 Voltage", 30.000000)
    prg.add(25000000, "Delta 1 Current", 200.000000)
    prg.add(30000000, "Delta 1 Current", 50.000000)
    prg.add(35000000, "Delta 1 Voltage", 15.000000)
    prg.add(45000000, "Delta 1 Voltage", 0.000000)
    prg.add(50000000, "Delta 1 Current", 0.000000)
    return prg
