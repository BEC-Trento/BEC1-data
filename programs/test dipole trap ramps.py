prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Dipole trap xy STANDBY")
    prg.add(2000000, "Dipole trap xy ON")
    prg.add(7000000, "Dipole Trap x ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=200.0000, functions=dict(stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_x_DAC_V_final'), start_x=lambda x: cmd.get_var('Dipole_x_DAC_V')))
    prg.add(7010000, "Dipole Trap y ramp", start_t=0.0000, stop_x=2.000, n_points=100, start_x=4.000, stop_t=200.0000, functions=dict(stop_t=lambda x: cmd.get_var('dipole_evap_time'), stop_x=lambda x: cmd.get_var('Dipole_y_DAC_V_final'), start_x=lambda x: cmd.get_var('Dipole_y_DAC_V')))
    prg.add(37010000, "Dipole trap xy STANDBY")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(2, 20, 4)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof = iters[j]
        cmd.set_var('tof', tof)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
