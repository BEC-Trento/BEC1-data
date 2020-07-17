prg_comment = ""
prg_version = "0.7"

def program(prg, cmd):

    frame_name = 'probe0'
    t_probe0 = -3 * 1e4
    t_trig = 1e4*(cmd.get_var('siglent1_sweep_time')+cmd.get_var('tof_frame') - 24)
    prg.add(t_trig - 700, "Trig ON Stingray 1", frame_name)
    prg.add(t_probe0, "Probe y AOM TTL")
    prg.add(t_trig + 120, "Trig OFF Stingray 1")
    
    for n in range(0, cmd.get_var("n_frames")):
#        t_im=1e4*(cmd.get_var('tof_frame')+cmd.get_var('siglent1_sweep_time'))*(n+1)
        t_sweep=1e4*(cmd.get_var('siglent1_sweep_time')+cmd.get_var('tof_frame')+cmd.get_var('t_wait'))*n
        t_im=t_sweep+1e4*(cmd.get_var('siglent1_sweep_time')+cmd.get_var('tof_frame'))
        prg.add(t_sweep, "Rf Sweep Siglent" ) #siglent sweep
        prg.add(t_sweep+0.1e4, "Pulse uw", pulse_t = cmd.get_var('tof_frame'))
        #single frame imaging at time t_im
        frame_name = 'image%d'%n
        prg.add(t_im-700, "Trig ON Stingray 1", frame_name)
        prg.add(1.0*t_im, "Probe y AOM TTL")
        prg.add(t_im+120, "Trig OFF Stingray 1")
        
        
    # probe: only probe
    t_probe = 1e4*cmd.get_var('n_frames') * (cmd.get_var('siglent1_sweep_time') +cmd.get_var('tof_frame') + cmd.get_var('t_wait'))+1e4*(cmd.get_var('siglent1_sweep_time')+cmd.get_var('tof_frame'))
    
    frame_name = 'probe'
    prg.add(t_probe-700, "Trig ON Stingray 1", frame_name)
    prg.add(t_probe, "Probe y AOM TTL")
    prg.add(t_probe+120, "Trig OFF Stingray 1")

    
    # dark: no probe pulse
    t_dark= t_probe + 1e4*111
    frame_name = 'dark'
#   print(name, t)
    prg.add(t_dark-1e4*20, "Shutter Probe/Push Close") #close the shutter 20 ms before the stingray trigger
    prg.add(t_dark-700, "Trig ON Stingray 1", frame_name)
    prg.add(t_dark+120, "Trig OFF Stingray 1")   


    return prg
