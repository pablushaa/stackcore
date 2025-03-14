# 💾 StackCore

> **StackCore** - стековый язык программирования, написанный специально для **eOS** (soon). Внешне код очень сильно напоминает ASM.

## ⚠️ Важно
> Настоятельно рекомендую ознакомится с [вики](https://github.com/pablushaa/stackcore/wiki/) данного проекта

## Таблица Опкодов

| Опкод              | Байткод | Назначение                                    | Параметры | Версия SC |
| ------------------ | ------- | --------------------------------------------- | --------- | --------- |
| `HLT`              | `0x00`  | Завершение работы програмы                    | -         | 1.0       |
| `JMP`              | `0x01`  | Безусловный переход по адресу                 | -         | 1.0       |
| `JEQ`              | `0x02`  | Условный переход по адресу                    | -         | 1.0       |
| `PUSHC`            | `0x0D`  | Помещение ASCII - символа в конец<br>стека    | `chr8`    | 1.0       |
| `PUSH8`            | `0x0E`  | Помещение 8-битного числа в<br>конец стека    | `int8`    | 1.0       |
| `PUSH16`           | `0x0F`  | Помещение 16-битного числа<br>в конец стека   | `int16`   | 1.0       |
| `PUSH`<br>`PUSH32` | `0x10`  | Помещение 32-битного числа<br>в конец стека   | `int32`   | 1.0       |
| `POP`              | `0x11`  | Удаление верхнего элемента стека              | -         | 1.0       |
| `STORE`            | `0x12`  | Перемещение верхнего элемента<br>стека в ПОЗУ | -         | 1.0       |
| `LOAD`             | `0x13`  | Загрузка элемента из ПОЗУ                     | -         | 1.0       |
| `FREE`             | `0x14`  | Очистка ячейки ПОЗУ                           | -         | 1.0       |
| `CLR`              | `0x15`  | Очистка стека                                 | -         | 1.0       |
| `ADD`              | `0x20`  | Сумма первых двух элементов стека             | -         | 1.0       |
| `SUB`              | `0x21`  | Разность первых двух элментов стека           | -         | 1.0       |
| `MUL`              | `0x22`  | Произведение первых двух элементов<br>стека   | -         | 1.0       |
| `DIV`              | `0x23`  | Частное первых двух элементов стека           | -         | 1.0       |
| `INC`              | `0x24`  | Инеремент первого элемента стека              | -         | 1.0       |
| `DEC`              | `0x25`  | Декремент первого элемента стека              | -         | 1.0       |
| `NEG`              | `0x26`  | Отрицание (0 -> 1, 1 -> 0, N -> -N)           | -         | 1.0       |
| `AND`              | `0x27`  | Логическое И                                  | -         | 1.0       |
| `OR`               | `0x28`  | Логическое ИЛИ                                | -         | 1.0       |
| `XOR`              | `0x29`  | Исключающее ИЛИ                               | -         | 1.0       |
| `CMP`              | `0x2A`  | a == b -> 0, a < b -> -1, a > b -> 1          | -         | 1.0       |
| `PRINT`            | `0x40`  | Вывод первого числа стека                     | -         | 1.0       |
| `PRINTC`           | `0x41`  | Вывод ASCII символа первого числа стека       | -         | 1.0       |
| `VOID`             | `0xFF`  | Пустота                                       | -         | 1.0       |
