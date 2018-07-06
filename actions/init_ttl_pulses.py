import libraries.ttlpulse as lib_ttlpulse

def action_list_init(action_list):

    action_list.add("Pulse uw", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Pulse uw ON", act_off_name="Pulse uw OFF"),
                    variables=dict(pulse_t=0.002, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
    action_list.add("Pulse TTL2-12", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="TTL2-12 ON", act_off_name="TTL2-12 OFF"),
                    variables=dict(pulse_t=1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="prova ttl pulse")
                    
    action_list.add("Pulse Trig Stingray 1", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Trig ON Stingray 1", act_off_name="Trig OFF Stingray 1"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
    action_list.add("Pulse Trig Stingray 2", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Trig ON Stingray 2", act_off_name="Trig OFF Stingray 2"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")

    action_list.add("Pulse Trig Extra Hamamatsu", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Trig Extra Hamamatsu ON", act_off_name="Trig Extra Hamamatsu OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")                  

    action_list.add("Pulse Repumper MOT", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="TTL Repumper MOT ON", act_off_name="TTL Repumper MOT OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
    action_list.add("Pulse MOT beams", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Na 3D MOT cool (-) ON", act_off_name="Na 3D MOT cool (-) OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
    action_list.add("Pulse Probe Na", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Na Probe/Push (+) ON", act_off_name="Na Probe/Push (+) OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
                    
    action_list.add("Pulse Bottom Evap", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Bottom Evaporation ON", act_off_name="Bottom Evaporation OFF"),
                    variables=dict(pulse_t=1.0, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")    
