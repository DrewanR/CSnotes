---
tags:
  - CM1101
aliases:
  - Radix Numbers
---
## Radix Number Systems

| English     | Base | Digits           | Use |
| ----------- |:----:| ---------------- | --- |
| Decimal     |  10  | 0123456789       | Humans    |
| Binary      |  2   | 01               | What computers use    |
| Octal       |  8   | 01234567         |     |
| Hexadecimal |  16  | 0123456789ABCDEF | Easily converts to binary as 4 binary digits equals one hex one    |

Subscript is used to denote which base is currently being used. If no subscript is present, we often assume that when the subscript is not present it is in decimal form. Only new/weaker areas have been detailed below.
## Decimal to Binary Conversion
For the digits to the left of the decimal point, use the reminder method. (refer to [[4 - Data representation.pdf|pdf]], its the method I already use). For digits after the decimal point, use the multiplication method:

NOTE: the numbers in the square brackets are getting multiplied.
![[CM1101 03 10 2023 1000 Drawing.excalidraw]]
Rounding will often need to occur.
Practice [[Drawing 2023-10-03 13.38.12.excalidraw|here]].
## Why is binary used with computers
Ones and zeros are used, as they are represented by either a high or low voltage. This means that variance in voltages doesn't break everything.
![[Pasted image 20231003140729.png]]
## Converting Between Decimal and Octal 
The reminder method can be used here, where you divide by 8 instead, the reminder is the bit. The multiplication method presumably works the same way.
## Range and Precision
### Fixed point
| Range     | Minimum number to maximum                    |
| --------- | -------------------------------------------- |
| Precision | Minimum difference between two adjacent nums |
There is a trade-off to having a greater range or greater precision
## Negative Numbers & Two's compliment
To represent negative numbers one has to sacrifice one bit. Sign and magnitude can be used, however this results in a +0 and -0. The main method is two's compliment.

This is where the the lowest bit, say there is 8 bits, the 2^7 digit becomes -2^7.

You can subtract numbers by adding a negative number. `x - y = x + -y`

Converting a negative number to two's compliment:
1) Carry out a standard binary conversion of the magnitude;
2) Fill up the spaces with zeros;
3) Invert all the bits (0 becomes 1, and 1 becomes 0)
4) Finally, add 1
Example: to store the integer -12 in 8 bit register
1) 12 → 1100
2) 1100 → 00001100
3) 00001100 → 11110011
4) 11110011 + 1 = 11110100

