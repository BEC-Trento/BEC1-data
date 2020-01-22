prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):

    t = 0
    d = 'z'  # y or z
    for j in range(cmd.get_var("movie_n_frames")):
        t = j * cmd.get_var("movie_time_interval")
        t_uw = t
        t_img = t + cmd.get_var("hold_time_2")
        prg.add(1e4*t_uw, "Pulse uw", polarity=1, pulse_t=1e-3*cmd.get_var("marconi1_pulsetime"))
        # imaging unpacked: atoms
        name = "atoms_%d"%j
#        name = 'atoms'
        print(name, t_img)
        prg.add(1e4*(t_img - 0.03), "Pulse Trig Stingray %s"%d, comment=name, polarity=1, pulse_t=0.10000)
        prg.add(1e4*t_img, "Probe %s AOM TTL"%d,)

    
    # probe
    t = t_img + 100
    name = 'probe'
    print(name, t)
    prg.add(1e4*(t - 0.03), "Pulse Trig Stingray %s"%d, comment=name, polarity=1, pulse_t=0.10000)
    prg.add(1e4*t, "Probe %s AOM TTL"%d,)

 
    # dark
    t += 100
    name = 'dark'
    print(name, t)
    prg.add(1e4*t, "Pulse Trig Stingray %s"%d, comment=name, polarity=1, pulse_t=0.10000)

#    prg.add(1e4 * (movie_time + cmd.get_var("hold_time_2")), "BEC_imaging",) 
    return prg
