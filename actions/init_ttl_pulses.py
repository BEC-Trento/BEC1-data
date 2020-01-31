import libraries.ttlpulse as lib_ttlpulse

def action_list_init(action_list):

    action_list.add("Scope 1 Trigger Pulse", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Scope 1 Trigger ON", act_off_name="Scope 1 Trigger OFF"),
                    variables=dict(pulse_t=0.01, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")

    action_list.add("Scope 2 Trigger Pulse", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Scope 2 Trigger ON", act_off_name="Scope 2 Trigger OFF"),
                    variables=dict(pulse_t=0.0123, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                                        
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
                    variables=dict(pulse_t=0.1, polarity=1, comment="image0"),
                    var_formats=dict(pulse_t="%.5f", polarity="%d", comment="%s"),
                    )
                    
    action_list.add("Pulse Trig Stingray y", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Trig ON Stingray 1", act_off_name="Trig OFF Stingray 1"),
                    variables=dict(pulse_t=0.1, polarity=1, comment="image0"),
                    var_formats=dict(pulse_t="%.5f", polarity="%d", comment="%s"),
                    )
                    
    action_list.add("Pulse Trig Stingray x", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Trig ON Stingray x", act_off_name="Trig OFF Stingray x"),
                    variables=dict(pulse_t=0.1, polarity=1, comment="image0"),
                    var_formats=dict(pulse_t="%.5f", polarity="%d", comment="%s"),
                    )
                    
    action_list.add("Pulse Trig Stingray z", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Trig ON Stingray z", act_off_name="Trig OFF Stingray z"),
                    variables=dict(pulse_t=0.1, polarity=1, comment="image0"),
                    var_formats=dict(pulse_t="%.5f", polarity="%d", comment="%s"),
                    )

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

    action_list.add("Pulse Probe y", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="TTL Probe y ON", act_off_name="TTL Probe y OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")

    action_list.add("Pulse Probe z", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="TTL Probe z ON", act_off_name="TTL Probe z OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")

    action_list.add("Pulse Freq sweep Probe Na", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Na Probe/Push Freq Sweep ON", act_off_name="Na Probe/Push Freq Sweep OFF"),
                    variables=dict(pulse_t=0.1, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
                    
    action_list.add("Pulse RFO Bottom Evap", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="Bottom Evaporation ON", act_off_name="Bottom Evaporation OFF"),
                    variables=dict(pulse_t=1.0, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse")
                    
                    
    action_list.add("Pulse RFO Sweep Trig", lib_ttlpulse.TTLPulse,
                    categories=["ttl pulses"],
                    parameters=dict(act_on_name="RFO Sweep Trig ON", act_off_name="RFO Sweep Trig OFF"),
                    variables=dict(pulse_t=1.0, polarity=1),
                    var_formats=dict(pulse_t="%.5f", polarity="%d"),
                    comment="ttl pulse") 
