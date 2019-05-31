prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-300000, "B comp x", 700.0, functions=dict(value=lambda x: cmd.get_var('Bx_GM')))
    prg.add(-299000, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_GM')))
    prg.add(-298000, "B comp z", 0.8500, functions=dict(value=lambda x: cmd.get_var('Bz_GM')))
    prg.add(0, "GM ON")
    prg.add(7500, "GM amp(+) ramp", start_t=0, stop_x=750, n_points=15, start_x=1000, stop_t=1, functions=dict(start_x=lambda x: cmd.get_var('GM_amp')))
    prg.add(18000, "Na Gray molasses (+) freq", 117.50, functions=dict(frequency=lambda x: 100+(cmd.get_var('GM_det')/4), funct_enable=False))
    prg.add(18500, "Na Gray molasses (-) freq", 82.50, functions=dict(frequency=lambda x: 100-(cmd.get_var('GM_det')/4), funct_enable=False))
    prg.add(19000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=30, start_x=750, stop_t=3)
    prg.add(50000, "GM OFF")
    return prg
