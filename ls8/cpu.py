"""CPU functionality."""

import sys

LDI  = 0b10000010
PRN  = 0b01000111
HLT  = 0b00000001
MULT = 0b10100010



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram=[0] * 256
        self.pc=0
        self.reg=[0] * 8



    def load(self):
        """Load a program into memory."""


        running = True
        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def LDI(self):
        reg_num = self.ram_read()


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op ==  "MULT":
            self.reg[self.ram[reg_a]] *= self.reg[self.ram[reg_b]]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def MULT(self):
        self.alu('MULT', self.pc+1, self.pc+2)
        self.pc += 3

    def ram_read(self):
        index = self.ram[self.pc + 1]
        print(self.reg[index])

    
    def ram_write(self, operand_a,operand_b):
        self.reg[operand_a] = operand_b  

    def run(self):
        """Run the CPU."""
        self.running = True
        while self.running:
            command = self.ram[self.pc]
            if command == HLT:
                self.running = False
                self.pc = 0
            if command == PRN:
                self.ram_read()
                self.pc += 2
            if command == LDI:
                operand_a = self.ram[self.pc + 1]
                operand_b = self.ram[self.pc + 2]
                self.ram_write(operand_a, operand_b)
                self.pc += 3



