# StackCore compiler
import struct

result = [56, 78, 14, 88]

with open("result", "+wb") as result_file:
    with open("main.sc") as file:
        line = file.readline().replace("\n", "").split()
        while line:
            if line[0].lower() == "hlt": # завершение работы проги
                result.append(0x00)
            elif line[0].lower() == "jmp": # безусловный переход по адресу (смещение PC)
                result.append(0x01)
            elif line[0].lower() == "jeq": # переход, если вершина = 0
                result.append(0x02)
            elif line[0].lower() == "pushc":
                result.append(0x0D)
                num = ord(line[1])
                if 0 <= num < 128:
                    result.append(num)
                else:
                    print("OTVAL EPTA >>> invalid character")
                    exit(1)
            elif line[0].lower() == "push8": # поместить 8-битное значение в стек
                result.append(0x0E)
                if line[1][:2] == "0x":
                    num = int(line[1][2:], 16)
                else:
                    num = int(line[1])
                result.extend(list(struct.pack("b", num)))
            elif line[0].lower() == "push16": # поместить 16-битное значение в стек
                result.append(0x0F)
                if line[1][:2] == "0x":
                    num = int(line[1][2:], 16)
                else:
                    num = int(line[1])
                result.extend(list(struct.pack("<h", num)))
            elif line[0].lower() == "push32" or line[0].lower() == "push": # поместить 32-битное значение в стек
                result.append(0x10)
                if line[1][:2] == "0x":
                    num = int(line[1][2:], 16)
                else:
                    num = int(line[1])
                result.extend(list(struct.pack("<i", num)))
            elif line[0].lower() == "pop": # удалить верх стека
                result.append(0x11)
            elif line[0].lower() == "store": # сохранить верхний элемент стека в псевдо-озу
                result.append(0x12)
            elif line[0].lower() == "load": # загружает элемент в стек из псевдо-озу
                result.append(0x13)
            elif line[0].lower() == "free": # очистка ячейки ОЗУ
                result.append(0x14)
            elif line[0].lower() == "clr": # очистка стека
                result.append(0x15)
            elif line[0].lower() == "add": # сложение верхнего и нижнего (и их удаление!!!)
                result.append(0x20)
            elif line[0].lower() == "sub": # вычитание из верхнего элемента нижнего
                result.append(0x21)
            elif line[0].lower() == "mul": # умножение
                result.append(0x22)
            elif line[0].lower() == "div": # деление верхнего элемента на нижний
                result.append(0x23)
            elif line[0].lower() == "inc": # инкремент первого элемента
                result.append(0x24)
            elif line[0].lower() == "dec": # декремент первого элемента
                result.append(0x25)
            elif line[0].lower() == "neg": # отрицание
                result.append(0x26)
            elif line[0].lower() == "and": # логическое И
                result.append(0x27)
            elif line[0].lower() == "or": # логическое ИЛИ
                result.append(0x29)
            elif line[0].lower() == "xor": # исключающее ИЛИ
                result.append(0x29)
            elif line[0].lower() == "cmp": # a == b -> 0; a < b -> -1; a > b -> 1
                result.append(0x2A)
            elif line[0].lower() == "print": # вывод первой чиселки из стека
                result.append(0x40)
            elif line[0].lower() == "printc": # вывод ascii символа первого числа из стека
                result.append(0x41)
            elif line[0].lower() == "void":
                result.append(0xff)
            else:
                print("error: invalid progremmer: " + line)
                exit()
            
            line = file.readline().replace("\n", "").split()
    #print(result)
    print(f"total: {len(result)} bytes")
    result_file.write(bytearray(result))