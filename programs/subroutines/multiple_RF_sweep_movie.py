prg_comment = ""
prg_version = "0.7"

def program(prg, cmd):
    for n in range(0, cmd.get_var("n_frames")):
#        t_im=1e4*(cmd.get_var('tof_frame')+cmd.get_var('siglent1_sweep_time'))*(n+1)
        t_sweep=1e4*(cmd.get_var('siglent1_sweep_time')+cmd.get_var('tof_frame')+cmd.get_var('t_wait'))*n
        t_im=t_sweep+1e4*(cmd.get_var('siglent1_sweep_time')+cmd.get_var('tof_frame'))
        prg.add(t_sweep, "Rf Sweep Siglent" ) #siglent sweep
        #single frame imaging at time t_im
        frame_name = 'image%d'%n
        prg.add(t_im-300, "Trig ON Stingray 1", frame_name)
        prg.add(t_im, "Probe y AOM TTL")
        prg.add(t_im+100, "Trig OFF Stingray 1")

    return prg
