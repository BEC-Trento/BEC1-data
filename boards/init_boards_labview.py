import libraries.board as lib_board
def board_list_init(board_lst):
    board_lst.add("DDS20", lib_board.DdsBoard,
                  address=20,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 +500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 +500}))
    board_lst.add("DDS21", lib_board.DdsBoard,
                  address=21,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: 51 + (float(x)-1600-112.5)*1.0/1.6}))
    board_lst.add("DDS22", lib_board.DdsBoard,
                  address=22,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-119.5)*1.0/0.5 + 500}))
    board_lst.add("DDS23", lib_board.DdsBoard,
                  address=23,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS24", lib_board.DdsBoard,
                  address=24,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS25", lib_board.DdsBoard,
                  address=25,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS26", lib_board.DdsBoard,
                  address=26,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS27", lib_board.DdsBoard,
                  address=27,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS30", lib_board.DdsBoard,
                  address=30,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25}))
    board_lst.add("DDS31", lib_board.DdsBoard,
                  address=31,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 , 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500 }))
    board_lst.add("DDS32", lib_board.DdsBoard,
                  address=32,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 , 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS33", lib_board.DdsBoard,
                  address=33,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 , 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500 }))
    board_lst.add("DDS34", lib_board.DdsBoard,
                  address=34,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25 }))
    board_lst.add("DDS35", lib_board.DdsBoard,
                  address=35,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (-78.00 + float(x))/0.01, 2: lambda x: (-60.00 + float(x))/0.1 + 500}))
    board_lst.add("DDS19", lib_board.DdsBoard,
                  address=19,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-59.75)*1.0/0.25, 2: lambda x: (float(x)-59.75)*1.0/0.25 + 500}))
    board_lst.add("DDS50", lib_board.DdsBoard,
                  address=50,
                  parameters=dict(amp_to_lut={},
                                  freq_to_lut={}))
    board_lst.add("DDS51", lib_board.DdsBoard,
                  address=51,
                  parameters=dict(amp_to_lut={},
                                  freq_to_lut={}))
    board_lst.add("DDS52", lib_board.DdsBoard,
                  address=52,
                  parameters=dict(amp_to_lut={1: lambda x: (int(x)+4000)*1.0/10, 2: lambda x: (int(x)+4000)*1.0/10 + 500},
                                  freq_to_lut={1: lambda x: (float(x)-0.649)*10.0/0.001, 2: lambda x: (float(x)-0.649)*10.0/0.001 + 500}))
    board_lst.add("ANG60", lib_board.AnalogBoard,
                  address=60,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
    board_lst.add("ANG61", lib_board.AnalogBoard,
                  address=61,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32.767*1.0/10}))
    board_lst.add("ANG62", lib_board.AnalogBoard,
                  address=62,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
    board_lst.add("ANG63", lib_board.AnalogBoard,
                  address=63,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10}))
    board_lst.add("ANG64", lib_board.AnalogBoard,
                  address=64,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/30}))
    board_lst.add("ANG65", lib_board.AnalogBoard,
                  address=65,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/200}))
    board_lst.add("ANG66", lib_board.AnalogBoard,
                  address=66,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/30}))
    board_lst.add("ANG67", lib_board.AnalogBoard,
                  address=67,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/200}))
    board_lst.add("DDS10", lib_board.DdsBoard,
                  address=10,
                  parameters=dict(amp_to_lut={},
                                  freq_to_lut={}))
    board_lst.add("ANG69", lib_board.AnalogBoard,
                  address=69,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10.0}))
    board_lst.add("ANG70", lib_board.AnalogBoard,
                  address=70,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/10.0}))
    board_lst.add("ANG71", lib_board.AnalogBoard,
                  address=71,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*0.5/5.0}))
    board_lst.add("ANG72", lib_board.AnalogBoard,
                  address=72,
                  parameters=dict(ang_to_dig={1: lambda x: float(x)*32767*1.0/5.0}))
    board_lst.add("TTL0", lib_board.DigitalBoard,
                  address=0)
    board_lst.add("TTL1", lib_board.DigitalBoard,
                  address=1)
    board_lst.add("TTL2", lib_board.DigitalBoard,
                  address=2)
    board_lst.add("TTL3", lib_board.DigitalBoard,
                  address=3)
    board_lst.add("TTL4", lib_board.DigitalBoard,
                  address=4)

