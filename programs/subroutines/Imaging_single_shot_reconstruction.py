prg_comment = ""
prg_version = "0.7"


def program(prg, cmd):

    t_exposure = cmd.get_var('cam4_ExposureTime')*1e-3

    t_uw = 0.005  # end of uw pulse to probe
    t_pic = cmd.get_var('t_pic')*1e-3 + 0.004# 0.0478  # end of exposure to begin of next exposure (in theory)
    
    extractions = cmd.get_var('uw_pulsetime_list') # put the right pulsetime here\
    
    def shot_frame(t, uw_pulsetime, name, t_probe=0.0614, scope=False, kick=False):
        """ t = 0 is the camera trigger
            the scope is eventually triggered
        """
        name = 'im%d'%name if isinstance(name, int) else name
        prg.add(1e4*t, "Pulse Trig Stingray z", comment=name, polarity=1, pulse_t=0.1491)
#        prg.add(1e4*(t + 0.0034), "Pulse Trig Stingray y", comment=name, polarity=1, pulse_t=0.1491)

        if scope:
            prg.add(1e4*(t - 0.002), "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.0144)
        t += t_probe
        if uw_pulsetime > 0:
            prg.add(1e4*(t - t_uw - uw_pulsetime*1e-3), "Pulse uw ON")
            prg.add(1e4*(t - t_uw), "Pulse uw OFF")
        if kick:
            prg.add(1e4*t, "Probe y + z AOM TTL", delay=0.0304)
        else:
            prg.add(1e4*t, "Probe z AOM TTL")


        
#    t = 0  # ms    
#    for j, (t1, offset) in enumerate(zip(extractions, probe_offset)):
#        name = 'atoms'
#        # name = 'im%d'%j
#        shot_frame(t, t1*1e-3, offset)
#        t += t_exposure + t_pic
    
    t = 0
    shot_frame(t, 1.5, name=0, t_probe=t_exposure - 0.03, kick=True)  # 0.08
    
    t += t_exposure + t_pic
    shot_frame(t, 3, 'atoms', scope=True)
    
    t += 100
    shot_frame(t, 0, 'probe')
 
    # dark
    t += 100
    prg.add(1e4*t, "Pulse Trig Stingray z", comment='dark', polarity=1, pulse_t=0.0144)
#    prg.add(1e4*(t + 0.0034), "Pulse Trig Stingray y", comment='dark', polarity=1, pulse_t=0.1491) 

#    print(extractions)
#    print(type(extractions))
    return prg
