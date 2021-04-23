import libraries.board as lib_board
def board_list_init(board_lst):
#    board_lst.add("dds20", lib_board.DdsBoard,
#                  address=20,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 +500}))
    board_lst.add("dds21", lib_board.DdsBoard,
                  address=21,
                  parameters=dict(
                    parent='fpga1',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: 200 + (float(x)-1712)*1.0/0.4}))
                                  
    board_lst.add("dds22", lib_board.DdsBoard,
                  address=22,
                  parameters=dict(
                    parent='fpga1',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 
                                 2: lambda x: (float(x)-119.5)*1.0/0.5 + 500}))
                                 
    board_lst.add("dds23", lib_board.DdsBoard,
                  address=23,
                  parameters=dict(
                    parent='fpga1',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 
                                 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))

    board_lst.add("dds37", lib_board.DdsBoard,
                  address=37,
                  parameters=dict(
                    parent='fpga0',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 
                                 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
                                                                  
    board_lst.add("dds24", lib_board.DdsBoard,
                  address=24,
                  parameters=dict(
                    parent='fpga1',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 
                                 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
                                 
    board_lst.add("dds25", lib_board.DdsBoard,
                  address=25,
                  parameters=dict(
                    parent='fpga1',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 
                                 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
                                 
    board_lst.add("dds26", lib_board.DdsBoard,
                  address=26,
                   parameters=dict(
 #                   amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500,
 #                               2: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
 #                   freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500,
 #                                2: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
                    parent='fpga0',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 
                                 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
                    
 
                                 
    board_lst.add("dds27", lib_board.DdsBoard,
                  address=27,
                  parameters=dict(
                    parent='fpga0',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-59.75)/0.25, 
                                 2: lambda x: (float(x)-0.49625)/0.00375 + 500}))
#    board_lst.add("dds30", lib_board.DdsBoard,
#                  address=30,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25}))

# deleted old dds31 (K cooler) to make room for Gray Molasses from Fish
#    board_lst.add("dds31", lib_board.DdsBoard,
#                  address=31,
#                  parameters=dict(amp_to_lut={1: lambda x: 799 + int(x/10), 2: lambda x: 900 + int(x/10)},
#                                  freq_to_lut={1: lambda x: 401 + int(x/(4*0.125))}))
    board_lst.add("dds31", lib_board.DdsBoard,
                  address=31,
                  parameters=dict(
                    parent='fpga1',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-69.85)*1.0/0.15 , 
                                 2: lambda x: (float(x)-69.85)*1.0/0.15 + 500}))
                                 

#    board_lst.add("dds32", lib_board.DdsBoard,
#                  address=32,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 , 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
#    board_lst.add("dds33", lib_board.DdsBoard,
#                  address=33,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 , 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500 }))
#    board_lst.add("dds34", lib_board.DdsBoard,
#                  address=34,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 }))
#    board_lst.add("dds35", lib_board.DdsBoard,
#                  address=35,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
#                                  freq_to_lut={1: lambda x: (-78.00 + float(x))/0.01, 2: lambda x: (-60.00 + float(x))/0.1 + 500}))
#    board_lst.add("dds19", lib_board.DdsBoard,
#                  address=19,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
#                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    
#    board_lst.add("dds50", lib_board.DdsBoard,
#                  address=50,
#                  parameters=dict(amp_to_lut={},
#                                  freq_to_lut={}))
    
    board_lst.add("dds50", lib_board.DdsBoard,
                  address=50,
                  parameters=dict(
                    parent='fpga0',
                    amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 
                                2: lambda x: (int(x)+4000)*1.0/10 + 500},
                    freq_to_lut={1: lambda x: (float(x)-69.85)*1.0/0.15 , 
                                 2: lambda x: (float(x)-69.85)*1.0/0.15 + 500}))
                                  
    board_lst.add("dds51", lib_board.DdsBoard,
                  address=51,
                  parameters=dict(parent='fpga0',
                                  amp_to_lut={},
                                  freq_to_lut={}))
                                  
#    board_lst.add("dds52", lib_board.DdsBoard,
#                  address=52,
#                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
#                                  freq_to_lut={1: lambda x: (float(x)-0.649)*10.0/0.001, 2: lambda x: (float(x)-0.649)*10.0/0.001 + 500}))
    board_lst.add("ang60", lib_board.AnalogBoard,
                  address=60,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
                  
    board_lst.add("ang61", lib_board.AnalogBoard,
                  address=61,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
                    
    board_lst.add("ang62", lib_board.AnalogBoard,
                  address=62,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
                    
    board_lst.add("ang63", lib_board.AnalogBoard,
                  address=63,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
                    
    board_lst.add("ang64", lib_board.AnalogBoard,
                  address=64,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/30}))
                    
    board_lst.add("ang65", lib_board.AnalogBoard,
                  address=65,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/200}))
                  #parameters=dict(ang_to_dig={1: lambda x: int(x)}))
                  
    board_lst.add("ang66", lib_board.AnalogBoard,
                  address=66,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/30}))
                    
    board_lst.add("ang67", lib_board.AnalogBoard,
                  address=67,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/200}))
                    
    board_lst.add("dds10", lib_board.DdsBoard,
                  address=10,
                  parameters=dict(amp_to_lut={},
                                  freq_to_lut={}))
                                  
    board_lst.add("ang69", lib_board.AnalogBoard,
                  address=69,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10.0}))
                    
    board_lst.add("ang70", lib_board.AnalogBoard,
                  address=70,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10.0}))
                    
    board_lst.add("ang71", lib_board.AnalogBoard,
                  address=71,
                  parameters=dict(parent='fpga0',
                    ang_to_dig={1: lambda x: float(x)*32767*0.5/5.0}))
                    
    board_lst.add("ang72", lib_board.AnalogBoard,
                  address=72,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/5.0}))
                    
    board_lst.add("ang73", lib_board.AnalogBoard,
                  address=73,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/5000.0}))   
                         
    board_lst.add("ang74", lib_board.AnalogBoard,
                  address=74,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/5000.0}))
                    
    board_lst.add("ang75", lib_board.AnalogBoard,
                  address=75,
                  parameters=dict(
                    ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
                    
    board_lst.add("ttl0", lib_board.DigitalBoard, address=0, parameters={'parent': 'fpga0'})
    
#    board_lst.add("ttl1", lib_board.DigitalBoard, address=1)
    
    board_lst.add("ttl2", lib_board.DigitalBoard, address=2, parameters={'parent': 'fpga1'})
    
    board_lst.add("ttl3", lib_board.DigitalBoard, address=3, parameters={'parent': 'fpga1'})
    
    board_lst.add("ttl4", lib_board.DigitalBoard, address=4, parameters={'parent': 'fpga0'})

