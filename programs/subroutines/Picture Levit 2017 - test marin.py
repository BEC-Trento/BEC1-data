prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B comp x ramp", start_t=0, stop_x=2000, n_points=20, start_x=1000, stop_t=1, enable=False)
    prg.add(0, "B comp y ramp", start_t=0, stop_x=5, n_points=20, start_x=0, stop_t=1, enable=False)
    prg.add(400, "Delta 1 Voltage", 5.0000)
    prg.add(500, "Delta 1 Current", 10.000)
    prg.add(900, "IGBT 5 Open")
    prg.add(1000, "IGBT 1 pinch", 10.0000, enable=False)
    prg.add(1000, "IGBT 4 Close")
    prg.add(1010, "Config Levitation zero current.sub")
    prg.add(1010, "B comp y ramp", start_t=0, stop_x=0, n_points=20, start_x=5, stop_t=1, enable=False)
    prg.add(1010, "B comp x ramp", start_t=0, stop_x=1369, n_points=20, start_x=2000, stop_t=1, enable=False)
    prg.add(105010, "Config Field OFF.sub")
    prg.add(115010, "Picture NaK for Levit 2017.sub")
    prg.add(4117010, "B comp y", 0.0000)
    return prg
