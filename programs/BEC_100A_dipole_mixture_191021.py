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
    prg.add(219949011, "Scope 2 Trigger ON", enable=False)
    prg.add(219986000, "Scope 2 Trigger OFF", enable=False)
    prg.add(220000000, "Load_Quad")
    prg.add(220010000, "Quad_RampUP")
    prg.add(220060000, "Mirrors Imaging")
    prg.add(225000000, "Ramp_bias_down.sub")
    prg.add(226000000, "All AOM On.sub", functions=dict(time=lambda x: 10015.6899+cmd.get_var('QuadRampTime'), funct_enable=False))
    prg.add(240001000, "Evaporation_2ramps_keep_on")
    prg.add(240001400, "Transfer_to_dipole", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')))
    prg.add(240001500, "Synchronize.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')))
    prg.add(240002468, "Scope 1 Trigger Pulse", polarity=1, pulse_t=1.00000, functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_evap2_time')-1e-3*cmd.get_var('marconi1_pulsetime')-1e-3*cmd.get_var('marconi1_pulsetime2')-0.001))
    prg.add(240002468, "Pulse uw with RF double", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')+1), enable=False)
    prg.add(240002468, "Pulse uw with RF dressing", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')+1))
    prg.add(240002468, "Pulse uw with RF dressing collision", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')+1), enable=False)
    prg.add(240002475, "B grad comp ON", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_evap2_time')+cmd.get_var('dipole_mix_time')-cmd.get_var('grad_ramp_time')+1e-3*cmd.get_var('probe_z_pulsetime_mix')), enable=False)
    prg.add(240002599, "Dipole trap xy STANDBY", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')), enable=False)
    prg.add(240002620, "Setup_imaging", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')+cmd.get_var('dipole_mix_time')), enable=False)
    prg.add(240002720, "BEC_imaging_field_OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_mix_time')+cmd.get_var('dipole_hold3_time')+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+cmd.get_var('dipole_evap2_time')+1e-3*cmd.get_var('probe_z_pulsetime_mix')+0.13), enable=False)
    prg.add(240003420, "BEC_imaging_z_field_OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_mix_time')+cmd.get_var('dipole_hold3_time')+1e-3*cmd.get_var('marconi1_pulsetime')+1e-3*cmd.get_var('marconi1_pulsetime2')+cmd.get_var('dipole_evap2_time')+1e-3*cmd.get_var('probe_z_pulsetime_mix')+0.004), enable=False)
    prg.add(240003420, "BEC_imaging_4_frames", functions=dict(time=lambda x: +cmd.get_var('dipole_mix_time')), enable=False)
    prg.add(240015620, "Imaging_situ_tof", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')+cmd.get_var('dipole_mix_time')))
    prg.add(246000000, "Pulse uw OFF", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('end_of_ODT_transfer')+cmd.get_var('dipole_mix_time')))
    prg.add(248003420, "DarkSpotMOT_19.sub", functions=dict(time=lambda x: x+cmd.get_var('evap1_time')+cmd.get_var('evap2_time')+cmd.get_var('dipole_hold_time')+cmd.get_var('dipole_evap_time')+cmd.get_var('dipole_hold2_time')+cmd.get_var('dipole_mix_time')+cmd.get_var('tof')+cmd.get_var('tof2')+cmd.get_var('Quad_rampdown2_time')+cmd.get_var('magnetic_trap_hold')+cmd.get_var('dipole_hold3_time')+cmd.get_var('dipole_evap2_time')+1e-3*cmd.get_var('probe_z_pulsetime_mix')), enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(12, 16, 1)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        Levitation_current = iters[j]
        cmd.set_var('Levitation_current', Levitation_current)
        print('\n')
        print('Run #%d/%d, with variables:\nLevitation_current = %g\n'%(j+1, len(iters), Levitation_current))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
