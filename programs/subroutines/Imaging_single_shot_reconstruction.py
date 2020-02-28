prg_comment = ""
prg_version = "0.7"


def program(prg, cmd):

    t_exposure = cmd.get_var('cam4_ExposureTime')*1e-3

    t_uw = 0.005  # end of uw pulse to probe
    t_pic = 0.254   # cmd.get_var('t_pic')*1e-3 + 0.004  # roughly, end of exposure to begin of next one
    
    extractions = cmd.get_var('uw_pulsetime_list') # put the right pulsetime here    
    
    
    def shot_frame(t, uw_pulsetime, name, t_probe=0.0914, scope=False, kick=False):
        # t = 0 is the camera trigger
        name = 'im%d'%name if isinstance(name, int) else name
        prg.add(1e4*t, "Pulse Trig Stingray z", comment=name, polarity=1, pulse_t=0.1491)
#        prg.add(1e4*(t + 0.0034), "Pulse Trig Stingray y", comment=name, polarity=1, pulse_t=0.1491)
        t += t_probe
        if scope:
            prg.add(1e4*(t - 0.002), "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.0144)
        if uw_pulsetime > 0:
            prg.add(1e4*(t - t_uw - uw_pulsetime*1e-3), "Pulse uw ON")
            prg.add(1e4*(t - t_uw), "Pulse uw OFF")
        if kick:
            prg.add(1e4*t, "Probe y + z AOM TTL", delay=0.0304)
        else:
            prg.add(1e4*t, "Probe z AOM TTL")
    
    # each shot is a bit customized here, so i'm not writing a loop
    assert len(extractions) == 3
    tau1, tau2, tau3 = extractions
    
    t = 0
    # weak extraction, end of 1st exposure
    shot_frame(t, tau1, name=0, t_probe=t_exposure - 0.03, scope=False)
    
    t += t_exposure + t_pic
    # mid-strong extraction, end of 2st exposure
    shot_frame(t, tau2, name=1, t_probe=t_exposure - 0.03, kick=True, scope=True)
    
    t += t_exposure + t_pic
    # mid-strong extraction, begin of 3rd exposure
    shot_frame(t, tau3, name=2)
    
    t += 100
    shot_frame(t, 0, 'probe')
 
    t += 100
    prg.add(1e4*t, "Pulse Trig Stingray z", comment='dark', polarity=1, pulse_t=0.0144)
    

# -- "debug" sequence
#    t = 0
#    shot_frame(t, 4, name=0, t_probe=t_exposure - 0.03, kick=True, scope=True)
#    
#    t += t_exposure + t_pic
#    shot_frame(t, 4, 'atoms',)
#    
#    t += 100
#    shot_frame(t, 0, 'probe')
# 
#    t += 100
#    prg.add(1e4*t, "Pulse Trig Stingray z", comment='dark', polarity=1, pulse_t=0.0144)

    return prg
