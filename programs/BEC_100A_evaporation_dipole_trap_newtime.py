prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "DarkSpotMOT_19.sub")
    prg.add(10000000, "Dipole trap xy STANDBY")
    prg.add(200000000, "Scope 4 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(219943111, "MOT lights Off TTL.sub")
    prg.add(219947301, "Config Field OFF.sub")
    prg.add(219949001, "Gray Molasses 2017")
    prg.add(219949011, "Scope 2 Trigger ON")
    prg.add(219986000, "Scope 2 Trigger OFF")
    prg.add(220000000, "Load_Quad")
    prg.add(220010000, "Quad_RampUP")
    prg.add(220060000, "Mirrors Imaging")
    prg.add(225000000, "Ramp_bias_down.sub")
    prg.add(226000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(240001000, "Evaporation_2ramps_keep_on")
    prg.add(240001400, "Dipole Trap xy evaporation")
    prg.add(240001450, "IGBT B grad x ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+10))
    prg.add(240001451, "B grad comp ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+12))
    prg.add(240001500, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')-cmd.get_var('sync_time')-1e-3*cmd.get_var('marconi1_pulsetime')-1e-3*cmd.get_var('marconi1_pulsetime2')-1e-3*cmd.get_var('marconi1_pulsetime_dressing')-0.5549))
    prg.add(240002409, "Scope 1 Trigger Pulse", polarity=1, pulse_t=1.00000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_evap2_time')-0.0107))
    prg.add(240002450, "Pulse uw with RF double", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')-cmd.get_var('marconi1_pulsetime')*1e-3-cmd.get_var('marconi1_pulsetime2')*1e-3-0.003), enable=False)
    prg.add(240002450, "Pulse uw with RF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')-cmd.get_var('marconi1_pulsetime')*1e-3+0.03), enable=False)
    prg.add(240002450, "Pulse uw dressing", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+0.103), enable=False)
    prg.add(240002450, "Pulse uw with RF dressing", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')-cmd.get_var('marconi1_pulsetime')*1e-3-cmd.get_var('marconi1_pulsetime2')*1e-3-0.003), enable=False)
    prg.add(240002468, "Evaporation freq", 5, functions=dict(frequency=lambda x: 5*1e6, time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.314))
    prg.add(240002468, "Evaporation amp", 1, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.21))
    prg.add(240002468, "Delta 1 Current ramp", start_t=0.0000, stop_x=0.000, n_points=100, start_x=100.000, stop_t=2000.0000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('magnetic_trap_hold'), start_x=lambda x: cmd.get_var('Quad_current_rampdown'), stop_t=lambda x: cmd.get_var('Quad_rampdown2_time'), stop_x=lambda x: cmd.get_var('Quad_rampdown2_current')))
    prg.add(240002468, "Config Field OFF.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.23+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')))
    prg.add(240002468, "Ramp_bias_field", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+0.33))
    prg.add(240002468, "Pulse uw with RF double", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_evap2_time')+0.0007), enable=False)
    prg.add(240002468, "Pulse uw with RF dressing", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_evap2_time')-1e-3*cmd.get_var('marconi1_pulsetime')-1e-3*cmd.get_var('marconi1_pulsetime2')-1e-3*cmd.get_var('marconi1_pulsetime_dressing')-0.5549))
    prg.add(240002620, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('tof')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')-37.361))
    prg.add(240002720, "BEC_imaging_field_OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')))
    prg.add(240003420, "BEC_imaging_z_field_OFF", enable=False)
    prg.add(248003420, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('mix_time')+cmd.get_var('tof')+cmd.get_var('tof2')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')))
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(108.987, 108.989, 0.0005)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        RF_freq = iters[j]
        cmd.set_var('RF_freq', RF_freq)
        print('\n')
        print('Run #%d/%d, with variables:\nRF_freq = %g\n'%(j+1, len(iters), RF_freq))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
