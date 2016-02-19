prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "TTL3 OFF")
    prg.add(100000, "DDS10 test", 200.000000)
    prg.add(110000, "DDS10 test", 700.000000)
    prg.add(10000000, "DDS10 test", 80.000000)
    prg.add(10010000, "DDS10 test", 580.000000)
    prg.add(20000000, "DDS10 test", 420.000000)
    prg.add(20010000, "DDS10 test", 920.000000)
    prg.add(30000000, "DDS10 test", 300.000000)
    prg.add(30010000, "TTL3 ON")
    prg.add(30020000, "TTL3 OFF")
    prg.add(40050000, "DDS10 test", 800.000000)
    prg.add(50000000, "DDS10 test", 1001.000000)
    prg.add(60010000, "DDS10 test", 1002.000000)
    prg.add(70000000, "DDS10 test", 500.000000)
    prg.add(80010000, "DDS10 test", 1000.000000)
    prg.add(80020000, "DDS10 test", 250.000000)
    prg.add(80090000, "DDS10 test", 750.000000)
    return prg
