# Copyright (c) 2014, The Linux Foundation. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 and
# only version 2 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

class Board(object):
    """ Class to describe a board the parser knows how to parse
    socid = shared id unique to a board type
    board_num = human readable board number indicating the board type
                (e.g. 8960, 8974)
    ram_start = start of the DDR
    imem_start = start of location in which the watchdog address is stored
    smem_addr = start of the shared memory region
    phys_offset = physical offset of the board (CONFIG_PHYS_OFFSET)
    wdog_addr = absolute physical address to check for FIQs
    imem_file_name = file name corresponding to imem_start

    It is not recommended to create instances of this class directly.
    Instead, classes should derive from this class and set fiels appropriately
    for each socid

    """
    def __init__(self):
         self.socid = -1
         self.board_num = -1
         self.cpu = 'UNKNOWN'
         self.ram_start = 0
         self.imem_start = 0
         self.smem_addr = 0
         self.phys_offset = 0
         self.wdog_addr = 0
         self.imem_file_name = None

class Board8960(Board):
    def __init__(self, socid, board_num):
        super(Board8960, self).__init__()
        self.socid = socid
        self.board_num = board_num
        self.cpu = 'KRAIT'
        self.ram_start = 0x80000000
        self.imem_start = 0x2a03f000
        self.smem_addr = 0x0
        self.phys_offset = 0x80200000
        self.wdog_addr = 0x2a03f658
        self.imem_file_name = 'IMEM_C.BIN'

class Board8625(Board):
    def __init__(self, socid, board_num):
        super(Board8625, self).__init__()
        self.socid = socid
        self.board_num = board_num
        self.cpu = 'SCORPION'
        self.ram_start = 0
        self.imem_start = 0x0
        self.smem_addr = 0x00100000
        self.phys_offset = 0x00200000

class Board9615(Board):
    def __init__(self, socid):
        super(Board9615, self).__init__()
        self.socid = socid
        self.board_num = 9615
        self.cpu = 'CORTEXA5'
        self.ram_start = 0x40000000
        self.imem_start = 0
        self.smem_addr = 0x0
        self.phys_offset = 0x40800000

class Board8974(Board):
    def __init__(self, socid, board_num=8974):
        super(Board8974, self).__init__()
        self.socid = socid
        self.board_num = board_num
        self.cpu = 'KRAIT'
        self.ram_start = 0x0
        self.imem_start = 0xfe800000
        self.smem_addr = 0xfa00000
        self.phys_offset = 0x0
        self.wdog_addr = 0xfe805658
        self.imem_file_name = 'OCIMEM.BIN'

class Board9625(Board):
    def __init__(self, socid):
        super(Board9625, self).__init__()
        self.socid = socid
        self.board_num = 9625
        self.cpu = 'CORTEXA5'
        self.ram_start = 0x0
        self.imem_start = 0xfe800000
        self.smem_addr = 0x0
        self.phys_offset = 0x200000
        self.wdog_addr = 0xfe805658
        self.imem_file_name = 'OCIMEM.BIN'

class Board8626(Board):
    def __init__(self, socid, board_num=8626):
        super(Board8626, self).__init__()
        self.socid = socid
        self.board_num = board_num
        self.cpu = 'CORTEXA7'
        self.ram_start = 0x0
        self.imem_start = 0xfe800000
        self.smem_addr = 0x0fa00000
        self.phys_offset = 0x0
        self.wdog_addr = 0xfe805658
        self.imem_file_name = 'OCIMEM.BIN'

class Board8610(Board):
    def __init__(self, socid, board_num=8610):
        super(Board8610, self).__init__()
        self.socid = socid
        self.board_num = board_num
        self.cpu = 'CORTEXA7'
        self.ram_start = 0x0
        self.imem_start = 0xfe800000
        self.smem_addr = 0x0d900000
        self.phys_offset = 0x0
        self.wdog_addr = 0xfe805658
        self.imem_file_name = 'OCIMEM.BIN'

class Board9635(Board):
    def __init__(self, socid):
        super(Board9635, self).__init__()
        self.socid = socid
        self.board_num = 9635
        self.cpu = 'CORTEXA7'
        self.ram_start = 0x0
        self.smem_addr = 0x1100000
        self.phys_offset = 0
        self.wdog_addr = 0xfe805658
        self.imem_file_name = 'OCIMEM.BIN'

boards = []
boards.append(Board8974(socid=126))
boards.append(Board8974(socid=184))
boards.append(Board8974(socid=185))
boards.append(Board8974(socid=186))
boards.append(Board8974(socid=208))
boards.append(Board8974(socid=211))
boards.append(Board8974(socid=214))
boards.append(Board8974(socid=217))
boards.append(Board8974(socid=209))
boards.append(Board8974(socid=212))
boards.append(Board8974(socid=215))
boards.append(Board8974(socid=218))
boards.append(Board8974(socid=194))
boards.append(Board8974(socid=210))
boards.append(Board8974(socid=213))
boards.append(Board8974(socid=216))

boards.append(Board9625(socid=134))
boards.append(Board9625(socid=148))
boards.append(Board9625(socid=149))
boards.append(Board9625(socid=150))
boards.append(Board9625(socid=151))
boards.append(Board9625(socid=152))
boards.append(Board9625(socid=173))
boards.append(Board9625(socid=174))
boards.append(Board9625(socid=175))


boards.append(Board8626(socid=145))
boards.append(Board8626(socid=158))
boards.append(Board8626(socid=159))
boards.append(Board8626(socid=198))
boards.append(Board8626(socid=199))
boards.append(Board8626(socid=200))
boards.append(Board8626(socid=205))
boards.append(Board8626(socid=219))
boards.append(Board8626(socid=220))
boards.append(Board8626(socid=222))
boards.append(Board8626(socid=223))
boards.append(Board8626(socid=224))


boards.append(Board8610(socid=147))
boards.append(Board8610(socid=161))
boards.append(Board8610(socid=162))
boards.append(Board8610(socid=163))
boards.append(Board8610(socid=164))
boards.append(Board8610(socid=165))
boards.append(Board8610(socid=166))

boards.append(Board8974(socid=178, board_num=8084))

boards.append(Board9635(socid=187))
boards.append(Board9635(socid=227))
boards.append(Board9635(socid=228))
boards.append(Board9635(socid=229))
boards.append(Board9635(socid=230))
boards.append(Board9635(socid=231))

boards.append(Board8960(socid=87, board_num=8960))
boards.append(Board8960(socid=122, board_num=8960))
boards.append(Board8960(socid=123, board_num=8260))
boards.append(Board8960(socid=124, board_num=8060))

boards.append(Board8960(socid=109, board_num=8064))
boards.append(Board8960(socid=130, board_num=8064))
boards.append(Board8960(socid=153, board_num=8064))

boards.append(Board8960(socid=116, board_num=8930))
boards.append(Board8960(socid=117, board_num=8930))
boards.append(Board8960(socid=118, board_num=8930))
boards.append(Board8960(socid=119, board_num=8930))
boards.append(Board8960(socid=154, board_num=8930))
boards.append(Board8960(socid=155, board_num=8930))
boards.append(Board8960(socid=156, board_num=8930))
boards.append(Board8960(socid=157, board_num=8930))
boards.append(Board8960(socid=160, board_num=8930))

boards.append(Board8960(socid=120, board_num=8627))
boards.append(Board8960(socid=121, board_num=8627))
boards.append(Board8960(socid=138, board_num=8960))
boards.append(Board8960(socid=139, board_num=8960))
boards.append(Board8960(socid=140, board_num=8960))
boards.append(Board8960(socid=141, board_num=8960))
boards.append(Board8960(socid=142, board_num=8930))
boards.append(Board8960(socid=143, board_num=8630))
boards.append(Board8960(socid=144, board_num=8630))

boards.append(Board9615(socid=104))
boards.append(Board9615(socid=105))
boards.append(Board9615(socid=106))
boards.append(Board9615(socid=107))

boards.append(Board8625(socid=88, board_num=8625))
boards.append(Board8625(socid=89, board_num=8625))
boards.append(Board8625(socid=96, board_num=8625))
boards.append(Board8625(socid=90, board_num=8625))
boards.append(Board8625(socid=91, board_num=8625))
boards.append(Board8625(socid=92, board_num=8625))
boards.append(Board8625(socid=97, board_num=8625))
boards.append(Board8625(socid=98, board_num=8625))
boards.append(Board8625(socid=99, board_num=8625))
boards.append(Board8625(socid=100, board_num=8625))
boards.append(Board8625(socid=101, board_num=8625))
boards.append(Board8625(socid=102, board_num=8625))
boards.append(Board8625(socid=103, board_num=8625))
boards.append(Board8625(socid=127, board_num=8625))
boards.append(Board8625(socid=128, board_num=8625))
boards.append(Board8625(socid=129, board_num=8625))
boards.append(Board8625(socid=131, board_num=8625))
boards.append(Board8625(socid=132, board_num=8625))
boards.append(Board8625(socid=133, board_num=8625))
boards.append(Board8625(socid=135, board_num=8625))


def get_supported_boards():
    """ Called by other part of the code to get a list of boards """
    return boards

def get_supported_ids():
    """ Returns a list of ids to be used with --force-hardware"""
    return list(set(b.board_num for b in boards))