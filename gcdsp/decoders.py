import gcdsp


Instruction = gcdsp.Instruction
InstructionExtension = gcdsp.InstructionExtension


class OpType:
    """Enumeration of the different operand encoding types which can be found
    in the GC DSP ISA. From DSPTables.h in Dolphin source code."""

    NONE = 0
    VAL = 1
    IMM = 2
    MEM = 3
    STR = 4
    ADDR_I = 5
    ADDR_D = 6

    REG = 0x8000
    REG04 = REG | 0x0400
    REG08 = REG | 0x0800
    REG18 = REG | 0x1800
    REGM18 = REG18
    REG19 = REG | 0x1900
    REGM19 = REG19
    REG1A = REG | 0x1a80
    REG1C = REG | 0x1c00
    ACCL = REG | 0x1c00
    ACCM = REG | 0x1e00
    ACCM_D = REG | 0x1e80
    ACC = REG | 0x2000
    ACC_D = REG | 0x2080
    AX = REG | 0x2200
    REGS_MASK = 0x3f80

    REF = REG | 0x4000
    PRG = REF | REG


opcodes = [
["NOP",0x0000,0xfffc,1,0,[],False,False],
["DAR",0x0004,0xfffc,1,1,[[OpType.REG,1,0,0,0x0003]],False,False],
["IAR",0x0008,0xfffc,1,1,[[OpType.REG,1,0,0,0x0003]],False,False],
["SUBARN",0x000c,0xfffc,1,1,[[OpType.REG,1,0,0,0x0003]],False,False],
["ADDARN",0x0010,0xfff0,1,2,[[OpType.REG,1,0,0,0x0003],[OpType.REG04,1,0,2,0x000c]],False,False],
["HALT",0x0021,0xffff,1,0,[],False,True],
["RETGE",0x02d0,0xffff,1,0,[],False,False],
["RETL",0x02d1,0xffff,1,0,[],False,False],
["RETG",0x02d2,0xffff,1,0,[],False,False],
["RETLE",0x02d3,0xffff,1,0,[],False,False],
["RETNZ",0x02d4,0xffff,1,0,[],False,False],
["RETZ",0x02d5,0xffff,1,0,[],False,False],
["RETNC",0x02d6,0xffff,1,0,[],False,False],
["RETC",0x02d7,0xffff,1,0,[],False,False],
["RETx8",0x02d8,0xffff,1,0,[],False,False],
["RETx9",0x02d9,0xffff,1,0,[],False,False],
["RETxA",0x02da,0xffff,1,0,[],False,False],
["RETxB",0x02db,0xffff,1,0,[],False,False],
["RETLNZ",0x02dc,0xffff,1,0,[],False,False],
["RETLZ",0x02dd,0xffff,1,0,[],False,False],
["RETO",0x02de,0xffff,1,0,[],False,False],
# ["RET",0x02df,0xffff,1,0,[],False,True],
["RTI",0x02ff,0xffff,1,0,[],False,True],
["CALLGE",0x02b0,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLL",0x02b1,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLG",0x02b2,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLLE",0x02b3,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLNZ",0x02b4,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLZ",0x02b5,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLNC",0x02b6,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLC",0x02b7,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLx8",0x02b8,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLx9",0x02b9,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLxA",0x02ba,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLxB",0x02bb,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLLNZ",0x02bc,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLLZ",0x02bd,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALLO",0x02be,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["CALL",0x02bf,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,True],
["IFGE",0x0270,0xffff,1,0,[],False,False],
["IFL",0x0271,0xffff,1,0,[],False,False],
["IFG",0x0272,0xffff,1,0,[],False,False],
["IFLE",0x0273,0xffff,1,0,[],False,False],
["IFNZ",0x0274,0xffff,1,0,[],False,False],
["IFZ",0x0275,0xffff,1,0,[],False,False],
["IFNC",0x0276,0xffff,1,0,[],False,False],
["IFC",0x0277,0xffff,1,0,[],False,False],
["IFx8",0x0278,0xffff,1,0,[],False,False],
["IFx9",0x0279,0xffff,1,0,[],False,False],
["IFxA",0x027a,0xffff,1,0,[],False,False],
["IFxB",0x027b,0xffff,1,0,[],False,False],
["IFLNZ",0x027c,0xffff,1,0,[],False,False],
["IFLZ",0x027d,0xffff,1,0,[],False,False],
["IFO",0x027e,0xffff,1,0,[],False,False],
["IF",0x027f,0xffff,1,0,[],False,True],
["JGE",0x0290,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JL",0x0291,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JG",0x0292,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JLE",0x0293,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JNZ",0x0294,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JZ",0x0295,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JNC",0x0296,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JC",0x0297,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JMPx8",0x0298,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JMPx9",0x0299,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JMPxA",0x029a,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JMPxB",0x029b,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JLNZ",0x029c,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JLZ",0x029d,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JO",0x029e,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,False],
["JMP",0x029f,0xffff,2,1,[[OpType.ADDR_I,2,1,0,0xffff]],False,True],
["JRGE",0x1700,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRL",0x1701,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRG",0x1702,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRLE",0x1703,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRNZ",0x1704,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRZ",0x1705,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRNC",0x1706,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRC",0x1707,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JMPRx8",0x1708,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JMPRx9",0x1709,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JMPRxA",0x170a,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JMPRxB",0x170b,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRLNZ",0x170c,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRLZ",0x170d,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JRO",0x170e,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["JMPR",0x170f,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,True],
["CALLRGE",0x1710,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRL",0x1711,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRG",0x1712,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRLE",0x1713,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRNZ",0x1714,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRZ",0x1715,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRNC",0x1716,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRC",0x1717,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRx8",0x1718,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRx9",0x1719,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRxA",0x171a,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRxB",0x171b,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRLNZ",0x171c,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRLZ",0x171d,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLRO",0x171e,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,False],
["CALLR",0x171f,0xff1f,1,1,[[OpType.REG,1,0,5,0x00e0]],False,True],
["SBCLR",0x1200,0xff00,1,1,[[OpType.IMM,1,0,0,0x0007]],False,False],
["SBSET",0x1300,0xff00,1,1,[[OpType.IMM,1,0,0,0x0007]],False,False],
["LSL",0x1400,0xfec0,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.IMM,1,0,0,0x003f]],False,False],
["LSR",0x1440,0xfec0,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.IMM,1,0,0,0x003f]],False,False],
["ASL",0x1480,0xfec0,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.IMM,1,0,0,0x003f]],False,False],
["ASR",0x14c0,0xfec0,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.IMM,1,0,0,0x003f]],False,False],
["LSRN",0x02ca,0xffff,1,0,[],False,False],
["ASRN",0x02cb,0xffff,1,0,[],False,False],
#["LRI",0x0080,0xffe0,2,2,[[OpType.REG,1,0,0,0x001f],[OpType.IMM,2,1,0,0xffff]],False,False],
["LR",0x00c0,0xffe0,2,2,[[OpType.REG,1,0,0,0x001f],[OpType.MEM,2,1,0,0xffff]],False,False],
["SR",0x00e0,0xffe0,2,2,[[OpType.MEM,2,1,0,0xffff],[OpType.REG,1,0,0,0x001f]],False,False],
#["MRR",0x1c00,0xfc00,1,2,[[OpType.REG,1,0,5,0x03e0],[OpType.REG,1,0,0,0x001f]],False,False],
["SI",0x1600,0xff00,2,2,[[OpType.MEM,1,0,0,0x00ff],[OpType.IMM,2,1,0,0xffff]],False,False],
["ADDIS",0x0400,0xfe00,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,1,0,0,0x00ff]],False,False],
["CMPIS",0x0600,0xfe00,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,1,0,0,0x00ff]],False,False],
["LRIS",0x0800,0xf800,1,2,[[OpType.REG18,1,0,8,0x0700],[OpType.IMM,1,0,0,0x00ff]],False,False],
["ADDI",0x0200,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["XORI",0x0220,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["ANDI",0x0240,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["ORI",0x0260,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["CMPI",0x0280,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["ANDF",0x02a0,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["ANDCF",0x02c0,0xfeff,2,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.IMM,2,1,0,0xffff]],False,False],
["ILRR",0x0210,0xfefc,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.PRG,1,0,0,0x0003]],False,False],
["ILRRD",0x0214,0xfefc,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.PRG,1,0,0,0x0003]],False,False],
["ILRRI",0x0218,0xfefc,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.PRG,1,0,0,0x0003]],False,False],
["ILRRN",0x021c,0xfefc,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.PRG,1,0,0,0x0003]],False,False],
["LOOP",0x0040,0xffe0,1,1,[[OpType.REG,1,0,0,0x001f]],False,True],
["BLOOP",0x0060,0xffe0,2,2,[[OpType.REG,1,0,0,0x001f],[OpType.ADDR_I,2,1,0,0xffff]],False,True],
["LOOPI",0x1000,0xff00,1,1,[[OpType.IMM,1,0,0,0x00ff]],False,True],
["BLOOPI",0x1100,0xff00,2,2,[[OpType.IMM,1,0,0,0x00ff],[OpType.ADDR_I,2,1,0,0xffff]],False,True],
["LRR",0x1800,0xff80,1,2,[[OpType.REG,1,0,0,0x001f],[OpType.PRG,1,0,5,0x0060]],False,False],
["LRRD",0x1880,0xff80,1,2,[[OpType.REG,1,0,0,0x001f],[OpType.PRG,1,0,5,0x0060]],False,False],
#["LRRI",0x1900,0xff80,1,2,[[OpType.REG,1,0,0,0x001f],[OpType.PRG,1,0,5,0x0060]],False,False],
["LRRN",0x1980,0xff80,1,2,[[OpType.REG,1,0,0,0x001f],[OpType.PRG,1,0,5,0x0060]],False,False],
["SRR",0x1a00,0xff80,1,2,[[OpType.PRG,1,0,5,0x0060],[OpType.REG,1,0,0,0x001f]],False,False],
["SRRD",0x1a80,0xff80,1,2,[[OpType.PRG,1,0,5,0x0060],[OpType.REG,1,0,0,0x001f]],False,False],
# ["SRRI",0x1b00,0xff80,1,2,[[OpType.PRG,1,0,5,0x0060],[OpType.REG,1,0,0,0x001f]],False,False],
#["SRRN",0x1b80,0xff80,1,2,[[OpType.PRG,1,0,5,0x0060],[OpType.REG,1,0,0,0x001f]],False,False],
["LRS",0x2000,0xf800,1,2,[[OpType.REG18,1,0,8,0x0700],[OpType.MEM,1,0,0,0x00ff]],False,False],
["SRS",0x2800,0xf800,1,2,[[OpType.MEM,1,0,0,0x00ff],[OpType.REG18,1,0,8,0x0700]],False,False],
["XORR",0x3000,0xfc80,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.REG1A,1,0,9,0x0200]],True,False],
["ANDR",0x3400,0xfc80,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.REG1A,1,0,9,0x0200]],True,False],
["ORR",0x3800,0xfc80,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.REG1A,1,0,9,0x0200]],True,False],
["ANDC",0x3c00,0xfe80,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.ACCM_D,1,0,8,0x0100]],True,False],
["ORC",0x3e00,0xfe80,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.ACCM_D,1,0,8,0x0100]],True,False],
["XORC",0x3080,0xfe80,1,2,[[OpType.ACCM,1,0,8,0x0100],[OpType.ACCM_D,1,0,8,0x0100]],True,False],
["NOT",0x3280,0xfe80,1,1,[[OpType.ACCM,1,0,8,0x0100]],True,False],
["LSRNRX",0x3480,0xfc80,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.REG1A,1,0,9,0x0200]],True,False],
["ASRNRX",0x3880,0xfc80,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.REG1A,1,0,9,0x0200]],True,False],
["LSRNR",0x3c80,0xfe80,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.ACCM_D,1,0,8,0x0100]],True,False],
["ASRNR",0x3e80,0xfe80,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.ACCM_D,1,0,8,0x0100]],True,False],
["ADDR",0x4000,0xf800,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.REG18,1,0,9,0x0600]],True,False],
["ADDAX",0x4800,0xfc00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.AX,1,0,9,0x0200]],True,False],
["ADD",0x4c00,0xfe00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.ACC_D,1,0,8,0x0100]],True,False],
["ADDP",0x4e00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["SUBR",0x5000,0xf800,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.REG18,1,0,9,0x0600]],True,False],
["SUBAX",0x5800,0xfc00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.AX,1,0,9,0x0200]],True,False],
["SUB",0x5c00,0xfe00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.ACC_D,1,0,8,0x0100]],True,False],
["SUBP",0x5e00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
#["MOVR",0x6000,0xf800,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.REG18,1,0,9,0x0600]],True,False],
["MOVAX",0x6800,0xfc00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.AX,1,0,9,0x0200]],True,False],
["MOV",0x6c00,0xfe00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.ACC_D,1,0,8,0x0100]],True,False],
#["MOVP",0x6e00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["ADDAXL",0x7000,0xfc00,1,2,[[OpType.ACC,1,0,8,0x0100],[OpType.REG18,1,0,9,0x0200]],True,False],
["INCM",0x7400,0xfe00,1,1,[[OpType.ACCM,1,0,8,0x0100]],True,False],
["INC",0x7600,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["DECM",0x7800,0xfe00,1,1,[[OpType.ACCM,1,0,8,0x0100]],True,False],
["DEC",0x7a00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["NEG",0x7c00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["MOVNP",0x7e00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["NX",0x8000,0xf700,1,0,[],True,False],
["CLR",0x8100,0xf700,1,1,[[OpType.ACC,1,0,11,0x0800]],True,False],
["CMP",0x8200,0xff00,1,0,[],True,False],
["MULAXH",0x8300,0xff00,1,0,[],True,False],
["CLRP",0x8400,0xff00,1,0,[],True,False],
["TSTPROD",0x8500,0xff00,1,0,[],True,False],
["TSTAXH",0x8600,0xfe00,1,1,[[OpType.REG1A,1,0,8,0x0100]],True,False],
#["M2",0x8a00,0xff00,1,0,[],True,False],
#["M0",0x8b00,0xff00,1,0,[],True,False],
#["CLR15",0x8c00,0xff00,1,0,[],True,False],
#["SET15",0x8d00,0xff00,1,0,[],True,False],
#["SET16",0x8e00,0xff00,1,0,[],True,False],
#["SET40",0x8f00,0xff00,1,0,[],True,False],
["MUL",0x9000,0xf700,1,2,[[OpType.REG18,1,0,11,0x0800],[OpType.REG1A,1,0,11,0x0800]],True,False],
["ASR16",0x9100,0xf700,1,1,[[OpType.ACC,1,0,11,0x0800]],True,False],
["MULMVZ",0x9200,0xf600,1,3,[[OpType.REG18,1,0,11,0x0800],[OpType.REG1A,1,0,11,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
["MULAC",0x9400,0xf600,1,3,[[OpType.REG18,1,0,11,0x0800],[OpType.REG1A,1,0,11,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
["MULMV",0x9600,0xf600,1,3,[[OpType.REG18,1,0,11,0x0800],[OpType.REG1A,1,0,11,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
#["MULX",0xa000,0xe700,1,2,[[OpType.REGM18,1,0,11,0x1000],[OpType.REGM19,1,0,10,0x0800]],True,False],
["ABS",0xa100,0xf700,1,1,[[OpType.ACC,1,0,11,0x0800]],True,False],
#["MULXMVZ",0xa200,0xe600,1,3,[[OpType.REGM18,1,0,11,0x1000],[OpType.REGM19,1,0,10,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
["MULXAC",0xa400,0xe600,1,3,[[OpType.REGM18,1,0,11,0x1000],[OpType.REGM19,1,0,10,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
["MULXMV",0xa600,0xe600,1,3,[[OpType.REGM18,1,0,11,0x1000],[OpType.REGM19,1,0,10,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
["TST",0xb100,0xf700,1,1,[[OpType.ACC,1,0,11,0x0800]],True,False],
#["MULC",0xc000,0xe700,1,2,[[OpType.ACCM,1,0,12,0x1000],[OpType.REG1A,1,0,11,0x0800]],True,False],
["CMPAR",0xc100,0xe700,1,2,[[OpType.ACC,1,0,12,0x1000],[OpType.REG1A,1,0,11,0x0800]],True,False],
["MULCMVZ",0xc200,0xe600,1,3,[[OpType.ACCM,1,0,12,0x1000],[OpType.REG1A,1,0,11,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
["MULCAC",0xc400,0xe600,1,3,[[OpType.ACCM,1,0,12,0x1000],[OpType.REG1A,1,0,11,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
#["MULCMV",0xc600,0xe600,1,3,[[OpType.ACCM,1,0,12,0x1000],[OpType.REG1A,1,0,11,0x0800],[OpType.ACC,1,0,8,0x0100]],True,False],
#["MADDX",0xe000,0xfc00,1,2,[[OpType.REGM18,1,0,8,0x0200],[OpType.REGM19,1,0,7,0x0100]],True,False],
#["MSUBX",0xe400,0xfc00,1,2,[[OpType.REGM18,1,0,8,0x0200],[OpType.REGM19,1,0,7,0x0100]],True,False],
#["MADDC",0xe800,0xfc00,1,2,[[OpType.ACCM,1,0,9,0x0200],[OpType.REG19,1,0,7,0x0100]],True,False],
#["MSUBC",0xec00,0xfc00,1,2,[[OpType.ACCM,1,0,9,0x0200],[OpType.REG19,1,0,7,0x0100]],True,False],
["LSL16",0xf000,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["MADD",0xf200,0xfe00,1,2,[[OpType.REG18,1,0,8,0x0100],[OpType.REG1A,1,0,8,0x0100]],True,False],
["LSR16",0xf400,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False],
["MSUB",0xf600,0xfe00,1,2,[[OpType.REG18,1,0,8,0x0100],[OpType.REG1A,1,0,8,0x0100]],True,False],
["ADDPAXZ",0xf800,0xfc00,1,2,[[OpType.ACC,1,0,9,0x0200],[OpType.AX,1,0,8,0x0100]],True,False],
["CLRL",0xfc00,0xfe00,1,1,[[OpType.ACCL,1,0,11,0x0800]],True,False],
["MOVPZ",0xfe00,0xfe00,1,1,[[OpType.ACC,1,0,8,0x0100]],True,False]
]


opcodes_ext = [
#["XXX",0x0000,0x00fc,1,1,[[OpType.VAL,1,0,0,0x00ff]],False,False],
["DR",0x0004,0x00fc,1,1,[[OpType.REG,1,0,0,0x0003]],False,False],
["IR",0x0008,0x00fc,1,1,[[OpType.REG,1,0,0,0x0003]],False,False],
["NR",0x000c,0x00fc,1,1,[[OpType.REG,1,0,0,0x0003]],False,False],
["MV",0x0010,0x00f0,1,2,[[OpType.REG18,1,0,2,0x000c],[OpType.REG1C,1,0,0,0x0003]],False,False],
#["S",0x0020,0x00e4,1,2,[[OpType.PRG,1,0,0,0x0003],[OpType.REG1C,1,0,3,0x0018]],False,False],
["SN",0x0024,0x00e4,1,2,[[OpType.PRG,1,0,0,0x0003],[OpType.REG1C,1,0,3,0x0018]],False,False],
# ["L",0x0040,0x00c4,1,2,[[OpType.REG18,1,0,3,0x0038],[OpType.PRG,1,0,0,0x0003]],False,False],
#["LN",0x0044,0x00c4,1,2,[[OpType.REG18,1,0,3,0x0038],[OpType.PRG,1,0,0,0x0003]],False,False],
#["LS",0x0080,0x00ce,1,2,[[OpType.REG18,1,0,4,0x0030],[OpType.ACCM,1,0,0,0x0001]],False,False],
["SL",0x0082,0x00ce,1,2,[[OpType.ACCM,1,0,0,0x0001],[OpType.REG18,1,0,4,0x0030]],False,False],
["LSN",0x0084,0x00ce,1,2,[[OpType.REG18,1,0,4,0x0030],[OpType.ACCM,1,0,0,0x0001]],False,False],
["SLN",0x0086,0x00ce,1,2,[[OpType.ACCM,1,0,0,0x0001],[OpType.REG18,1,0,4,0x0030]],False,False],
#["LSM",0x0088,0x00ce,1,2,[[OpType.REG18,1,0,4,0x0030],[OpType.ACCM,1,0,0,0x0001]],False,False],
["SLM",0x008a,0x00ce,1,2,[[OpType.ACCM,1,0,0,0x0001],[OpType.REG18,1,0,4,0x0030]],False,False],
["LSNM",0x008c,0x00ce,1,2,[[OpType.REG18,1,0,4,0x0030],[OpType.ACCM,1,0,0,0x0001]],False,False],
["SLNM",0x008e,0x00ce,1,2,[[OpType.ACCM,1,0,0,0x0001],[OpType.REG18,1,0,4,0x0030]],False,False],
["LDAX",0x00c3,0x00cf,1,2,[[OpType.AX,1,0,4,0x0010],[OpType.PRG,1,0,5,0x0020]],False,False],
["LDAXN",0x00c7,0x00cf,1,2,[[OpType.AX,1,0,4,0x0010],[OpType.PRG,1,0,5,0x0020]],False,False],
["LDAXM",0x00cb,0x00cf,1,2,[[OpType.AX,1,0,4,0x0010],[OpType.PRG,1,0,5,0x0020]],False,False],
["LDAXNM",0x00cf,0x00cf,1,2,[[OpType.AX,1,0,4,0x0010],[OpType.PRG,1,0,5,0x0020]],False,False],
["LD",0x00c0,0x00cc,1,3,[[OpType.REGM18,1,0,4,0x0020],[OpType.REGM19,1,0,3,0x0010],[OpType.PRG,1,0,0,0x0003]],False,False],
["LDN",0x00c4,0x00cc,1,3,[[OpType.REGM18,1,0,4,0x0020],[OpType.REGM19,1,0,3,0x0010],[OpType.PRG,1,0,0,0x0003]],False,False],
#["LDM",0x00c8,0x00cc,1,3,[[OpType.REGM18,1,0,4,0x0020],[OpType.REGM19,1,0,3,0x0010],[OpType.PRG,1,0,0,0x0003]],False,False],
["LDNM",0x00cc,0x00cc,1,3,[[OpType.REGM18,1,0,4,0x0020],[OpType.REGM19,1,0,3,0x0010],[OpType.PRG,1,0,0,0x0003]],False,False]
]


(
    NO_AR0, NO_AR1, NO_AR2, NO_AR3,
    NO_IX0, NO_IX1, NO_IX2, NO_IX3,
    NO_R08, NO_R09, NO_R0A, NO_R0B,
    NO_ST0, NO_ST1, NO_ST2, NO_ST3,
    NO_AC0H, NO_AC1H,
    NO_CONFIG, NO_SR,
    NO_PRODL, NO_PRODM1, NO_PRODH, NO_PRODM2,
    NO_AX0L, NO_AX1L, NO_AX0H, NO_AX1H,
    NO_AC0L, NO_AC1L, NO_AC0M, NO_AC1M,
) = range(32)


def get_register_range(context, first, last):
    return context.registers[first:last + 1]


class Reg:
    (
        ALL, ADDR, ACM, AXH, ACCUM,
        REG18_2, REG19_2, REG18_4, REG1C_4,
    ) = range(9)

    def __init__(self, reg_class, mask, shift, invert=False):
        self.reg_class = reg_class
        self.mask = mask
        self.shift = shift
        self.invert = invert

    def get_reg_class(self, context):
        def reg_range(first, last):
            return get_register_range(context, first, last)

        if self.reg_class == self.ALL:
            return context.registers
        if self.reg_class == self.ADDR:
            return reg_range(NO_AR0,  NO_AR3)
        if self.reg_class == self.ACM:
            return reg_range(NO_AC0M, NO_AC1M)
        if self.reg_class == self.AXH:
            return reg_range(NO_AX0H, NO_AX1H)
        if self.reg_class == self.ACCUM:
            return context.long_accumulators

        if self.reg_class == self.REG18_2:
            return [context.registers[NO_AX0L], context.registers[NO_AX0H]]
        if self.reg_class == self.REG19_2:
            return [context.registers[NO_AX1L], context.registers[NO_AX1H]]
        if self.reg_class == self.REG18_4:
            return reg_range(NO_AX0L, NO_AC1M)
        if self.reg_class == self.REG1C_4:
            return reg_range(NO_AC0L, NO_AC1M)
        else:
            assert False

    def extract(self, context, instruction):
        value = (instruction.opcode_value & self.mask) >> self.shift
        return self.get_reg_class(context)[value]


SR_BIT_MUL = 13
SR_BIT_40_MODE = 14
SR_BIT_UNSIGNED = 15


def build_sr_test(ctx, disas, bld, bit_no):
    """Return an instruction that computes the `bit_no`nth SR bit."""
    sr_reg = ctx.registers[NO_SR]
    bit_mask = sr_reg.type.create(1 << bit_no)
    return bld.build_ne(
        bld.build_and(sr_reg.build_load(bld), bit_mask),
        sr_reg.type.create(0)
    )


def build_sr_set(ctx, disas, bld, bit_no, clear):
    """
    Build instruction that set (0 if `clear`, 1 otherwise) `bit_no`nth SR bit.
    """
    sr_reg = ctx.registers[NO_SR]
    sr_val = sr_reg.build_load(bld)
    bit_mask = sr_reg.type.create(1 << bit_no)
    if clear:
        sr_val = bld.build_and(
            sr_val,
            bld.build_xor(bit_mask, sr_reg.type.create(-1))
        )
    else:
        sr_val = bld.build_or(sr_val, bit_mask)
    sr_reg.build_store(bld, sr_val)


def build_same_memory_area_test(ctx, disas, bld, addr1, addr2):
    """
    Build and return instructions that compute whether `addr1` and `addr2` are
    two integer values representing addresses that point to the same memory
    area.
    """
    return bld.build_eq(
        bld.build_lshr(addr1, addr1.type.create(10)),
        bld.build_lshr(addr2, addr2.type.create(10)),
    )


def build_increase_addr_reg(ctx, disas, bld, addr_reg, idx_reg=None):
    """
    Increase an address register, handling circular buffers.

    If `idx_reg` is None, `addr_reg` is increment. Otherwise, the value of the
    register `idx_reg` is used as the increase amount.
    """
    bb_start = bld.current_basic_block
    if idx_reg:
        bb_overflow = bld.create_basic_block()
        bb_underflow = bld.create_basic_block()
        bb_next = bld.create_basic_block()

    half_type = ctx.half_type

    # First, compute the candidate next address.
    wr_reg = ctx.addr_to_wr[addr_reg]
    addr_reg_val = addr_reg.build_load(bld)
    one = half_type.create(1)
    incr_val = one if idx_reg is None else idx_reg.build_load(bld)
    next_addr = bld.build_add(addr_reg_val, incr_val)
    wr_reg_val = wr_reg.build_load(bld)

    mx_val = bld.build_lshl(bld.build_or(wr_reg_val, one), one)
    # Keep the simple incrementation case separate so that it can generate
    # simpler code. TODO: understand exactly why the simple case is not the
    # same as the complex one with constant folding...
    if idx_reg:
        dar_val = bld.build_and(
            bld.build_xor(bld.build_xor(next_addr, addr_reg_val), incr_val),
            mx_val
        )
        bld.build_branch(
            bld.build_sge(incr_val, half_type.create(0)),
            bb_overflow, bb_underflow,
        )

        # Handle possible overflow on the buffer boundary.
        bld.position_at_end(bb_overflow)
        has_overflowed = bld.build_ugt(dar_val, wr_reg_val)
        overflow_val = bld.build_select(
            has_overflowed,
            bld.build_sub(next_addr, bld.build_add(wr_reg_val, one)),
            next_addr
        )
        bld.build_jump(bb_next)

        # Handle possible underflow on the buffer boundary.
        bld.position_at_end(bb_underflow)
        has_underflowed = bld.build_ule(
            bld.build_and(
                bld.build_xor(
                    bld.build_add(bld.build_add(next_addr, wr_reg_val), one),
                    next_addr
                ),
                dar_val
            ),
            wr_reg_val
        )
        underflow_val = bld.build_select(
            has_underflowed,
            bld.build_add(next_addr, bld.build_add(wr_reg_val, one)),
            next_addr
        )
        bld.build_jump(bb_next)

        # Finally, store the result back in the source register.
        bld.position_at_end(bb_next)
        new_addr = bld.build_phi([
            (bb_overflow, overflow_val),
            (bb_underflow, underflow_val),
        ])
    else:
        has_overflowed = bld.build_ugt(
            bld.build_xor(next_addr, addr_reg_val),
            mx_val
        )
        new_addr = bld.build_select(
            has_overflowed,
            bld.build_sub(next_addr, bld.build_add(wr_reg_val, one)),
            next_addr
        )
    addr_reg.build_store(bld, new_addr)


def match_middle_accumulator(ctx, reg):
    """
    If reg is the middle part of an accumulator register, return the
    corresponding long accumulator.  Return None otherwise.
    """
    ac0m_reg, ac1m_reg = get_register_range(ctx, NO_AC0M, NO_AC1M)
    if reg in (ac0m_reg, ac1m_reg):
        return (
            ctx.long_accumulators[0]
            if reg == ac0m_reg else
            ctx.long_accumulators[1]
        )
    else:
        return None


def build_store_extend_acc(ctx, disas, bld, reg, value):
    """Extend `value` to the whole 40-bit register `reg`."""
    dest_high_reg, dest_mid_reg, dest_low_reg = reg.registers

    # Store the extended value in the whole acculumator: low part (16 lowest
    # bits) are 0 and the 8 upper ones are sign extended.
    sext_type = ctx.create_int_type(24)
    sext_value = bld.build_lshr(
        bld.build_sext(sext_type, value),
        sext_type.create(16)
    )
    dest_high_reg.build_store(bld,
        bld.build_trunc(dest_high_reg.type, sext_value)
    )
    dest_mid_reg.build_store(bld, value)
    dest_low_reg.build_store(bld, dest_low_reg.type.create(0))


# TODO: remove code duplication between the two following helpers:

def build_store_maybe_extend_acc(ctx, disas, bld, reg, value):
    """
    If reg is the middle part of an accumulator register and if the SR register
    requires it, extend the value to the whole 40-bit register. Otherwise, only
    store value to the register.
    """
    match = match_middle_accumulator(ctx, reg)
    if match:
        _, dest_mid_reg, _ = match.registers
        bb_extend = bld.create_basic_block()
        bb_regular = bld.create_basic_block()
        bb_next = bld.create_basic_block()

        # First test if the extension is actually required by the SR register.
        bld.build_branch(
            build_sr_test(ctx, disas, bld, SR_BIT_40_MODE),
            bb_extend, bb_regular
        )

        # If it is, extend.
        bld.position_at_end(bb_extend)
        build_store_extend_acc(ctx, disas, bld, match, value)
        bld.build_jump(bb_next)

        # Otherwise, just move to middle part.
        bld.position_at_end(bb_regular)
        dest_mid_reg.build_store(bld, value)
        bld.build_jump(bb_next)

        bld.position_at_end(bb_next)
    else:
        reg.build_store(bld, value)


def build_load_maybe_extend_acc(ctx, disas, bld, reg):
    """
    If reg is the middle part of an accumulator register, return its extended
    (saturated) value.  Otherwise, just return its value.
    """
    value = reg.build_load(bld)
    match = match_middle_accumulator(ctx, reg)
    if match:
        high_reg, mid_reg, low_reg = match.registers

        bb_start = bld.current_basic_block
        bb_extend = bld.create_basic_block()
        bb_saturate = bld.create_basic_block()
        bb_next = bld.create_basic_block()

        # First test if the extension is actually required by the SR register.
        bld.build_branch(
            build_sr_test(ctx, disas, bld, SR_BIT_40_MODE),
            bb_extend, bb_next
        )

        # If it is, then as soon as the high accumulator part is non-null,
        # saturate the result.
        bld.position_at_end(bb_extend)
        high_reg_val = high_reg.build_load(bld)
        bld.build_branch(
            bld.build_ne(high_reg_val, high_reg.type.create(0)),
            bb_saturate, bb_next
        )

        # Get a different result depending on the signedness of the accumulator
        # register.  Remember that the high 8 bits of the high part of the
        # accumulator is garbage.
        bld.position_at_end(bb_saturate)
        high_sign_val = bld.build_trunc(ctx.byte_type, high_reg_val)
        ret_saturated_val = bld.build_select(
            bld.build_sge(high_sign_val, ctx.byte_type.create(0)),
            mid_reg.type.create(0x7fff),
            mid_reg.type.create(0x8000)
        )
        bld.build_jump(bb_next)

        # If not, store the value in the regular register.
        bld.position_at_end(bb_next)
        return bld.build_phi([
            (bb_start, value),
            (bb_extend, value),
            (bb_saturate, ret_saturated_val),
        ])

    else:
        return value


# Product modes: determine how to extend input values before computing a
# product.
(
    # Both operands are sign-extended.
    MUL_SIGNED,
    # Both operands are zero-extended.
    MUL_UNSIGNED,
    # Left operand is zero-extened while right operand is sign-extended.
    MUL_MIXED,
) = range(3)


def build_multiply(ctx, disas, bld, left, right, mul_mode):
    """
    Build and return instructions to compute the product of `left` and `right`.

    `left` and `right` must be 16-bit values; they will be extended to 64-bit
    ones according to `mul_mode` and to the corresponding SR register bits
    before the product. Moreover, the result is double if required by the SR
    register.
    """
    assert left.type == ctx.half_type
    assert right.type == ctx.half_type
    assert mul_mode in (MUL_SIGNED, MUL_UNSIGNED, MUL_MIXED)

    bb_start = bld.current_basic_block
    bb_prod = bb_start
    bb_double = bld.create_basic_block()
    bb_next = bld.create_basic_block()

    # First, extend operands as needed.
    if mul_mode == MUL_SIGNED:
        left_ext = bld.build_sext(ctx.double_type, left)
        right_ext = bld.build_sext(ctx.double_type, right)
    elif mul_mode in (MUL_UNSIGNED, MUL_MIXED):
        # Sign-extend both unless the SR register allows something else.
        bb_specific = bld.create_basic_block()
        bb_sign_extend = bld.create_basic_block()
        bb_prod = bld.create_basic_block()

        bld.build_branch(
            build_sr_test(ctx, disas, bld, SR_BIT_UNSIGNED),
            bb_specific, bb_sign_extend
        )

        # SR register allows something else!
        bld.position_at_end(bb_specific)
        if mul_mode == MUL_UNSIGNED:
            left_spec = bld.build_zext(ctx.double_type, left)
            right_spec = bld.build_zext(ctx.double_type, right)
        else:
            left_spec = bld.build_zext(ctx.double_type, left)
            right_spec = bld.build_sext(ctx.double_type, right)
        bld.build_jump(bb_prod)

        # SR register allows only sign-extension...
        bld.position_at_end(bb_sign_extend)
        left_sext = bld.build_sext(ctx.double_type, left)
        right_sext = bld.build_sext(ctx.double_type, right)
        bld.build_jump(bb_prod)

        # Collect possible results and move on.
        bld.position_at_end(bb_prod)
        left_ext = bld.build_phi([
            (bb_specific, left_spec),
            (bb_sign_extend, left_sext),
        ])
        right_ext = bld.build_phi([
            (bb_specific, right_spec),
            (bb_sign_extend, right_sext),
        ])

    prod_val = bld.build_mul(left_ext, right_ext)
    # If the corresponding SR bit is clear then double each product.
    bld.build_branch(
        build_sr_test(ctx, disas, bld, SR_BIT_MUL),
        bb_next, bb_double
    )

    bld.position_at_end(bb_double)
    double_val = bld.build_mul(prod_val, prod_val.type.create(2))
    bld.build_jump(bb_next)

    bld.position_at_end(bb_next)
    return bld.build_phi([
        (bb_prod, prod_val),
        (bb_double, double_val),
    ])


def build_multiply_mulx(ctx, disas, bld, left_reg, right_reg):
    """
    Build and return instructions to compute the product of `left` and `right`
    as MULX instructions family does.
    """
    def match(left_no, right_no):
        return (
            left_reg == ctx.registers[left_no]
            and right_reg == ctx.registers[right_no]
        )

    left_op, right_op = left_reg, right_reg

    if match(NO_AX0L, NO_AX1L):
        mul_mode = MUL_UNSIGNED
    elif match(NO_AX0L, NO_AX1H):
        mul_mode = MUL_MIXED
    elif match(NO_AX0H, NO_AX1L):
        left_op, right_op = right_reg, left_reg
        mul_mode = MUL_MIXED
    else:
        mul_mode = MUL_SIGNED

    return build_multiply(
        ctx, disas, bld,
        left_op.build_load(bld),
        right_op.build_load(bld),
        mul_mode
    )


def build_multiply_add(ctx, disas, bld, left_reg, right_reg):
    """
    Build instructions to compute and store the product + sum of `left`,
    `right` and the PROD register as MADD instructions family does.
    """
    prod_val = bld.build_zext(
        ctx.double_type,
        build_load_prod(ctx, disas, bld)
    )
    left_val = left_reg.build_load(bld)
    right_val = right_reg.build_load(bld)
    mul_val = build_multiply(ctx, disas, bld, left_val, right_val, MUL_SIGNED)

    build_store_prod(
        ctx, disas, bld,
        bld.build_add(prod_val, mul_val)
    )


def build_multiply_sub(ctx, disas, bld, left_reg, right_reg):
    """
    Build instructions to compute and store the product + difference of `left`,
    `right` and the PROD register as MSUB instructions family does.
    """
    prod_val = bld.build_zext(
        ctx.double_type,
        build_load_prod(ctx, disas, bld)
    )
    left_val = left_reg.build_load(bld)
    right_val = right_reg.build_load(bld)
    mul_val = build_multiply(ctx, disas, bld, left_val, right_val, MUL_SIGNED)

    build_store_prod(
        ctx, disas, bld,
        bld.build_sub(mul_val, prod_val)
    )


def build_store_prod(ctx, disas, bld, value):
    assert value.type == ctx.double_type
    prod_l, prod_m1, prod_h, prod_m2 = get_register_range(
        ctx, NO_PRODL, NO_PRODM2)

    prod_l.build_store(bld, bld.build_trunc(ctx.half_type, value))

    m1_val = bld.build_lshl(value, value.type.create(16))
    m1_val = bld.build_trunc(ctx.half_type, m1_val)
    prod_m1.build_store(bld, m1_val)

    h_val = bld.build_lshl(value, value.type.create(32))
    h_val = bld.build_trunc(ctx.byte_type, h_val)
    h_val = bld.build_zext(ctx.half_type, h_val)
    prod_h.build_store(bld, h_val)

    prod_m2.build_store(bld, prod_m2.type.create(0))


def build_load_prod(ctx, disas, bld, round_low=False):
    """
    Build and return instructions to compute PROD register as a 48-bit value.

    If `round_low`, round the low part of PROD before.
    """
    prod_m2_val, prod_high_val, prod_m1_val, prod_low_val = (
        ctx.prod_register.build_load_comp(bld)
    )

    prod_type = ctx.create_int_type(48)
    # Add prod.h.
    prod_val = bld.build_lshl(
        bld.build_sext(prod_type,
            bld.build_trunc(ctx.byte_type, prod_high_val)
        ),
        prod_type.create(32)
    )
    # Add prod.m1 and prod.m2.
    prod_val = bld.build_add(prod_val,
        bld.build_lshl(
            bld.build_add(
                bld.build_sext(prod_type, prod_m1_val),
                bld.build_sext(prod_type, prod_m2_val),
            ),
            prod_type.create(16)
        )
    )
    # Add prod.l.
    result = bld.build_add(prod_val,
        bld.build_sext(prod_type, prod_low_val)
    )

    if round_low:
        complement = bld.build_select(
            bld.build_ne(
                bld.build_and(result, result.type.create(0x10000)),
                result.type.create(0)
            ),
            result.type.create(0x8000),
            result.type.create(0x7fff),
        )
        result = bld.build_and(
            bld.build_add(result, complement),
            result.type.create(0x00000000ffff)
        )
    return result


class CLR15(Instruction):
    name            = 'CLR15'
    opcode          = 0x8c00
    opcode_mask     = 0xff00
    operands_format = []

    def decode(self, ctx, disas, bld):
        build_sr_set(ctx, disas, bld, SR_BIT_UNSIGNED, True)


class M2(Instruction):
    name            = 'M2'
    opcode          = 0x8a00
    opcode_mask     = 0xff00
    operands_format = []

    def decode(self, ctx, disas, bld):
        build_sr_set(ctx, disas, bld, SR_BIT_MUL, True)


class M0(Instruction):
    name            = 'M0'
    opcode          = 0x8b00
    opcode_mask     = 0xff00
    operands_format = []

    def decode(self, ctx, disas, bld):
        build_sr_set(ctx, disas, bld, SR_BIT_MUL, False)


class MADDC(Instruction):
    name            = 'MADDC'
    opcode          = 0xe800
    opcode_mask     = 0xfc00
    operands_format = [
        Reg(Reg.ACM, 0x0200, 9),
        Reg(Reg.AXH, 0x0100, 8),
    ]
    is_extended = True

    def decode(self, ctx, disas, bld):
        s_reg, t_reg = self.decode_operands(ctx)
        build_multiply_add(ctx, disas, bld, s_reg, t_reg)


class MADDX(Instruction):
    name            = 'MADDX'
    opcode          = 0xe000
    opcode_mask     = 0xfc00
    operands_format = [
        Reg(Reg.REG18_2, 0x0200, 9),
        Reg(Reg.REG19_2, 0x0100, 8),
    ]
    is_extended = True

    def decode(self, ctx, disas, bld):
        s_reg, t_reg = self.decode_operands(ctx)
        build_multiply_add(ctx, disas, bld, s_reg, t_reg)


class MOVP(Instruction):
    name            = 'MOVP'
    opcode          = 0x6e00
    opcode_mask     = 0xfe00
    operands_format = [
        Reg(Reg.ACCUM, 0x0100, 8),
    ]
    is_extended = True

    def decode(self, ctx, disas, bld):
        acc_reg, = self.decode_operands(ctx)

        prod_val = build_load_prod(ctx, disas, bld)
        acc_reg.build_store_comp(bld,
            # prod.h
            bld.build_trunc(
                ctx.registers[NO_PRODH].type,
                bld.build_lshr(prod_val, prod_val.type.create(32))
            ),
            # prod.m1
            bld.build_trunc(
                ctx.registers[NO_PRODM1].type,
                bld.build_lshr(prod_val, prod_val.type.create(16))
            ),
            # prod.l
            bld.build_trunc(ctx.registers[NO_PRODL].type, prod_val),
        )

        # TODO: update SR register


class MOVR(Instruction):
    name            = 'MOVR'
    opcode          = 0x6000
    opcode_mask     = 0xf800
    operands_format = [
        Reg(Reg.ACCUM,   0x0100, 8),
        Reg(Reg.REG18_4, 0x0600, 9),
    ]
    is_extended     = True

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)

        build_store_extend_acc(
            ctx, disas, bld,
            dest_reg, src_reg.build_load(bld)
        )
        # TODO: update SR register


class MRR(Instruction):
    name            = 'MRR'
    opcode          = 0x1c00
    opcode_mask     = 0xfc00
    operands_format = [
        Reg(Reg.ALL, 0x03e0, 5),
        Reg(Reg.ALL, 0x001f, 0),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)

        src_val = src_reg.build_load(bld)
        build_store_maybe_extend_acc(ctx, disas, bld, dest_reg, src_val)


class MSUBC(Instruction):
    name            = 'MSUBC'
    opcode          = 0xec00
    opcode_mask     = 0xfc00
    operands_format = [
        Reg(Reg.ACM, 0x0200, 9),
        Reg(Reg.AXH, 0x0100, 8),
    ]
    is_extended = True

    def decode(self, ctx, disas, bld):
        s_reg, t_reg = self.decode_operands(ctx)
        build_multiply_sub(ctx, disas, bld, s_reg, t_reg)


class MSUBX(Instruction):
    name            = 'MSUBX'
    opcode          = 0xe400
    opcode_mask     = 0xfc00
    operands_format = [
        Reg(Reg.REG18_2, 0x0200, 9),
        Reg(Reg.REG19_2, 0x0100, 8),
    ]
    is_extended = True

    def decode(self, ctx, disas, bld):
        s_reg, t_reg = self.decode_operands(ctx)
        build_multiply_sub(ctx, disas, bld, s_reg, t_reg)


class MULC(Instruction):
    name            = 'MULC'
    opcode          = 0xc000
    opcode_mask     = 0xe700
    operands_format = [
        Reg(Reg.ACM, 0x1000, 12),
        Reg(Reg.AXH, 0x0800, 11),
    ]
    is_extended     = True

    def decode(self, ctx, disas, bld):
        acm_reg, axh_reg = self.decode_operands(ctx)

        acm_val = acm_reg.build_load(bld)
        axh_val = axh_reg.build_load(bld)
        prod_val = build_multiply(
            ctx, disas, bld,
            acm_val, axh_val, MUL_SIGNED
        )
        build_store_prod(ctx, disas, bld, prod_val)


class MULCMV(Instruction):
    name            = 'MULCMV'
    opcode          = 0xc600
    opcode_mask     = 0xe600
    operands_format = [
        Reg(Reg.ACM,   0x1000, 12),
        Reg(Reg.AXH,   0x0800, 11),
        Reg(Reg.ACCUM, 0x0100, 8),
    ]
    is_extended     = True

    def decode(self, ctx, disas, bld):
        acm_reg, axh_reg, accum_reg = self.decode_operands(ctx)

        acm_val = acm_reg.build_load(bld)
        axh_val = axh_reg.build_load(bld)
        prod_old_values = ctx.prod_register.build_load_comp(bld)
        prod_old_values.pop(0)

        prod_new_val = build_multiply(
            ctx, disas, bld,
            acm_val, axh_val, MUL_SIGNED
        )
        build_store_prod(ctx, disas, bld, prod_new_val)
        accum_reg.build_store_comp(bld, *prod_old_values)


class MULX(Instruction):
    name            = 'MULX'
    opcode          = 0xa000
    opcode_mask     = 0xe700
    operands_format = [
        Reg(Reg.REG18_2, 0x1000, 12),
        Reg(Reg.REG19_2, 0x0800, 11),
    ]
    is_extended     = True

    def decode(self, ctx, disas, bld):
        s_reg, t_reg = self.decode_operands(ctx)
        build_store_prod(
            ctx, disas, bld,
            build_multiply_mulx(ctx, disas, bld, s_reg, t_reg)
        )


class MULXMVZ(Instruction):
    name            = 'MULXMVZ'
    opcode          = 0xa200
    opcode_mask     = 0xe600
    operands_format = [
        Reg(Reg.REG18_2, 0x1000, 12),
        Reg(Reg.REG19_2, 0x0800, 11),
        Reg(Reg.ACCUM,   0x0100, 8),
    ]
    is_extended     = True

    def decode(self, ctx, disas, bld):
        src_reg, t_reg, r_reg = self.decode_operands(ctx)

        prod = build_load_prod(ctx, disas, bld, round_low=True)
        acc_high, acc_mid, acc_low = r_reg.registers
        acc_low.build_store(bld, bld.build_trunc(acc_low.type, prod))
        acc_mid.build_store(bld, bld.build_trunc(acc_mid.type,
            bld.build_lshr(prod, prod.type.create(16))
        ))
        acc_high.build_store(bld, bld.build_sext(acc_high.type,
            bld.build_trunc(
                ctx.byte_type,
                bld.build_lshr(prod, prod.type.create(32))
            )
        ))

        build_store_prod(
            ctx, disas, bld,
            build_multiply_mulx(ctx, disas, bld, src_reg, t_reg)
        )
        # TODO: update SR register


class LRI(Instruction):
    name            = 'LRI'
    opcode          = 0x0080
    opcode_mask     = 0xffe0
    operands_format = [
        Reg(Reg.ALL, 0x001f, 0),
    ]
    have_extra_operand = True

    def decode(self, ctx, disas, bld):
        dest_reg, = self.decode_operands(ctx)
        build_store_maybe_extend_acc(
            ctx, disas, bld,
            dest_reg, ctx.half_type.create(self.extra_operand)
        )


class LRRI(Instruction):
    name            = 'LRRI'
    opcode          = 0x1900
    opcode_mask     = 0xff80
    operands_format = [
        Reg(Reg.ALL,  0x001f, 0),
        Reg(Reg.ADDR, 0x0060, 5),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)

        src_reg_val = src_reg.build_load(bld)
        load_addr   = bld.build_bitcast(ctx.pointer_type, src_reg_val)
        load_val    = bld.build_load(load_addr)

        build_store_maybe_extend_acc(ctx, disas, bld, dest_reg, load_val)
        build_increase_addr_reg(ctx, disas, bld, src_reg)


class SRRI(Instruction):
    name            = 'SRRI'
    opcode          = 0x1b00
    opcode_mask     = 0xff80
    operands_format = [
        Reg(Reg.ADDR, 0x0060, 5),
        Reg(Reg.ALL,  0x001f, 0),
    ]

    def decode(self, ctx, disas, bld):
        addr_reg, src_reg = self.decode_operands(ctx)

        src_value = build_load_maybe_extend_acc(ctx, disas, bld, src_reg)
        addr_value = bld.build_bitcast(
            ctx.pointer_type,
            addr_reg.build_load(bld)
        )
        bld.build_store(addr_value, src_value)
        build_increase_addr_reg(ctx, disas, bld, addr_reg)


class RET(Instruction):
    name            = 'RET'
    opcode          = 0x02df
    opcode_mask     = 0xffff
    operands_format = []

    def decode(self, ctx, disas, bld):
        bld.build_ret()
        disas.stop_basic_block()


class SET15(Instruction):
    name            = 'SET15'
    opcode          = 0x8d00
    opcode_mask     = 0xff00
    operands_format = []

    def decode(self, ctx, disas, bld):
        build_sr_set(ctx, disas, bld, SR_BIT_UNSIGNED, False)


class SET16(Instruction):
    name            = 'SET15'
    opcode          = 0x8e00
    opcode_mask     = 0xff00
    operands_format = []

    def decode(self, ctx, disas, bld):
        build_sr_set(ctx, disas, bld, SR_BIT_40_MODE, False)


class SET40(Instruction):
    name            = 'SET15'
    opcode          = 0x8f00
    opcode_mask     = 0xff00
    operands_format = []

    def decode(self, ctx, disas, bld):
        build_sr_set(ctx, disas, bld, SR_BIT_40_MODE, False)


class SRRN(Instruction):
    name            = 'SRRN'
    opcode          = 0x1b80
    opcode_mask     = 0xff80
    operands_format = [
        Reg(Reg.ADDR, 0x0060, 5),
        Reg(Reg.ALL,  0x001f, 0),
    ]

    def decode(self, ctx, disas, bld):
        addr_reg, src_reg = self.decode_operands(ctx)

        store_addr = bld.build_bitcast(
            ctx.pointer_type, addr_reg.build_load(bld)
        )
        store_val = build_load_maybe_extend_acc(ctx, disas, bld, src_reg)
        bld.build_store(store_addr, store_val)
        build_increase_addr_reg(
            ctx, disas, bld,
            addr_reg, ctx.addr_to_ix[addr_reg]
        )


class Ext_L(InstructionExtension):
    name            = 'L'
    opcode          = 0x0040
    opcode_mask     = 0x00c4
    operands_format = [
        Reg(Reg.REG18_4, 0x0038, 3),
        Reg(Reg.ADDR,    0x0003, 0),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)

        src_reg_val = src_reg.build_load(bld)
        load_addr   = bld.build_bitcast(ctx.pointer_type, src_reg_val)
        load_val    = bld.build_load(load_addr)

        build_store_maybe_extend_acc(ctx, disas, bld, dest_reg, load_val)
        build_increase_addr_reg(ctx, disas, bld, src_reg)


class Ext_LDM(InstructionExtension):
    name            = 'LDM'
    opcode          = 0x00c8
    opcode_mask     = 0x00cc
    operands_format = [
        Reg(Reg.REG18_2, 0x0020, 5),
        Reg(Reg.REG19_2, 0x0010, 4),
        Reg(Reg.ADDR,    0x0003, 0),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, r_reg, src_reg = self.decode_operands(ctx)

        addr_input = src_reg.build_load(bld)
        load_addr = bld.build_bitcast(ctx.pointer_type, addr_input)
        dest_reg.build_store(bld, bld.build_load(load_addr))

        addr_3 = ctx.registers[NO_AR3].build_load(bld)
        addr_selected = bld.build_select(
            build_same_memory_area_test(ctx, disas, bld, addr_input, addr_3),
            addr_input, addr_3
        )
        load_addr = bld.build_bitcast(ctx.pointer_type, addr_selected)
        r_reg.build_store(bld, bld.build_load(load_addr))

        build_increase_addr_reg(ctx, disas, bld, src_reg)
        build_increase_addr_reg(
            ctx, disas, bld,
            ctx.registers[NO_AR3],
            ctx.registers[NO_IX3]
        )


class Ext_LN(InstructionExtension):
    name            = 'LN'
    opcode          = 0x0044
    opcode_mask     = 0x00c4
    operands_format = [
        Reg(Reg.REG18_4, 0x0038, 3),
        Reg(Reg.ADDR,    0x0003, 0),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)

        load_addr = bld.build_bitcast(
            ctx.pointer_type,
            src_reg.build_load(bld)
        )
        load_val = bld.build_load(load_addr)
        build_store_maybe_extend_acc(ctx, disas, bld, dest_reg, load_val)
        build_increase_addr_reg(
            ctx, disas, bld,
            src_reg, ctx.addr_to_ix[src_reg]
        )


class Ext_LS(InstructionExtension):
    name            = 'LS'
    opcode          = 0x0080
    opcode_mask     = 0x00ce
    operands_format = [
        Reg(Reg.REG18_4, 0x0030, 4),
        Reg(Reg.ACM,     0x0001, 0),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)
        ar0 = ctx.registers[NO_AR0]
        ar3 = ctx.registers[NO_AR3]

        bld.build_store(
            bld.build_bitcast(ctx.pointer_type, ar3.build_load(bld)),
            build_load_maybe_extend_acc(ctx, disas, bld, src_reg)
        )
        bld.build_rstore(
            dest_reg,
            bld.build_load(
                bld.build_bitcast(ctx.pointer_type, ar0.build_load(bld))
            )
        )
        build_increase_addr_reg(ctx, disas, bld, ar0)
        build_increase_addr_reg(ctx, disas, bld, ar3)


class Ext_LSM(InstructionExtension):
    name            = 'LSM'
    opcode          = 0x0088
    opcode_mask     = 0x00ce
    operands_format = [
        Reg(Reg.REG18_4, 0x0030, 4),
        Reg(Reg.ACM,     0x0001, 0),
    ]

    def decode(self, ctx, disas, bld):
        dest_reg, src_reg = self.decode_operands(ctx)
        ar0 = ctx.registers[NO_AR0]
        ar3 = ctx.registers[NO_AR3]

        bld.build_store(
            bld.build_bitcast(ctx.pointer_type, ar3.build_load(bld)),
            build_load_maybe_extend_acc(ctx, disas, bld, src_reg)
        )
        bld.build_rstore(
            dest_reg,
            bld.build_load(
                bld.build_bitcast(ctx.pointer_type, ar0.build_load(bld))
            )
        )
        build_increase_addr_reg(ctx, disas, bld, ar0)
        build_increase_addr_reg(ctx, disas, bld, ar3, ctx.registers[NO_IX3])


class Ext_S(InstructionExtension):
    name            = 'S'
    opcode          = 0x0020
    opcode_mask     = 0x00e4
    operands_format = [
        Reg(Reg.ADDR,    0x0003, 0),
        Reg(Reg.REG18_4, 0x0018, 3),
    ]

    def decode(self, ctx, disas, bld):
        addr_reg, src_reg = self.decode_operands(ctx)

        src_value = build_load_maybe_extend_acc(ctx, disas, bld, src_reg)
        addr_value = bld.build_bitcast(
            ctx.pointer_type,
            addr_reg.build_load(bld)
        )
        bld.build_store(addr_value, src_value)
        build_increase_addr_reg(ctx, disas, bld, addr_reg)


class Ext_XXX(InstructionExtension):
    name            = 'XXX'
    opcode          = 0x0000
    opcode_mask     = 0x00fc
    operands_format = []

    def decode(self, ctx, disas, bld):
        pass
