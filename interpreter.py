import struct
stack = []
ram = [0] * 128

def get32Num(b: list):
    b = bytes(b)
    return struct.unpack("<i", b)[0]

def get16Num(b: list):
    b = bytes(b)
    return struct.unpack("<h", b)[0]

with open("result", "rb") as file:
    a = list(file.read())
    if a[:4] == [56, 78, 14, 88]:
        print("file is executable!")
        print(a)
        pc = 4
        while pc < len(a):
            if a[pc] == 0x00: # hlt
                print("HALT")
                break
            elif a[pc] == 0x01: # jmp
                pc = stack.pop() + 3
            elif a[pc] == 0x02: # jeq
                if len(stack) > 1:
                    addr = stack.pop()
                    n = stack.pop()
                    if n == 0:
                        pc = addr + 3
            elif a[pc] == 0x0D: # pushc
                stack.append(a[pc + 1])
                pc += 1
            elif a[pc] == 0x0E: # push8
                stack.append(a[pc + 1])
                pc += 1
            elif a[pc] == 0x0F: # push16
                stack.append(get16Num(a[pc +1: pc + 3]))
                pc += 2
            elif a[pc] == 0x10: # push32
                stack.append(get32Num(a[pc +1: pc + 5]))
                pc += 4
            elif a[pc] == 0x11: # pop
                stack.pop()
            elif a[pc] == 0x12: # store
                addr = stack.pop()
                ram[addr] = stack.pop()
            elif a[pc] == 0x13: # load
                addr = stack.pop()
                stack.append(ram[addr])
            elif a[pc] == 0x14: # free
                addr = stack.pop()
                ram[addr] = 0
                pc += 4
            elif a[pc] == 0x15: # clr
                stack.clear()
            elif a[pc] == 0x20: # add
                stack.append(stack.pop() + stack.pop())
            elif a[pc] == 0x21: # sub
                stack.append(stack.pop() - stack.pop())
            elif a[pc] == 0x22: # mul
                stack.append(stack.pop() * stack.pop())
            elif a[pc] == 0x23: # div
                stack.append(stack.pop() // stack.pop())
            elif a[pc] == 0x24: # inc
                stack.append(stack.pop() + 1)
            elif a[pc] == 0x25: # dec
                stack.append(stack.pop() - 1)
            elif a[pc] == 0x26: # neg
                A = stack.pop()
                if A == 0:
                    stack.append(1)
                elif A == 1:
                    stack.append(0)
                else:
                    stack.append(-A)
            elif a[pc] == 0x27: # and
                A = bool(stack.pop())
                B = bool(stack.pop())
                stack.append(int(bool(A and B)))
            elif a[pc] == 0x28: # or
                A = bool(stack.pop())
                B = bool(stack.pop())
                stack.append(int(A or B))
            elif a[pc] == 0x29: # xor
                A = bool(stack.pop())
                B = bool(stack.pop())
                stack.append(int(A ^ B))
            elif a[pc] == 0x2A: # cmp
                A = stack.pop()
                B = stack.pop()
                if A == B:
                    stack.append(0)
                if A < B:
                    stack.append(-1)
                if A > B:
                    stack.append(1)
            elif a[pc] == 0x40: # print
                print(stack.pop(), end="")
            elif a[pc] == 0x41: # printc
                print(chr(stack.pop()), end="")
            pc += 1
print("")
print(stack)
#print(ram)