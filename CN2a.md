2. i) Write a Program to implement the data link layer farming methods such as --> character stuffing.

Character stuffing is also known as byte stuffing or character-oriented framing and is same as that of bit stuffing but byte stuffing actually operates on bytes whereas bit stuffing operates on bits. In byte stuffing, special byte that is basically known as ESC (Escape Character) that has predefined pattern is generally added to data section of the data stream or frame when there is message or character that has same pattern as that of flag byte.

But receiver removes this ESC and keeps data part that causes some problems or issues. In simple words, we can say that character stuffing is addition of 1 additional byte if there is presence of ESC or flag in text.
![Bit_Byte_Stuffing_1](https://user-images.githubusercontent.com/83952736/185725016-1701152f-c03f-4a1d-a14d-b16ea587ea56.jpg)

INPUT FORMAT

The first line contains a character that represents the starting delimiter.
The second line contains a character that represents the ending delimiter.
The third line contains the characters to be stuffed.   

OUTPUT FORMAT:
Contains a frame after character stuffing.
SAMPLE INPUT:
d

g

goodday



SAMPLE OUTPUT: 

dggooddddayg
