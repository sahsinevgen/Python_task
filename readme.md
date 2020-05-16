
  What is it?
  -----------

  This is my encoder. It can encode or decode your text using caesar's, vigener's, or vernam's cipher if you know key.
  Also you can collect frequency of using letters in your text and use it to hack the caesar's cipher.

  How to use it
  -------------

  ```
  python3 main.py <0> --input_file <1> --output_file <2> --cipher <3> --key <4> --frequency_file <5>
  ```
  0) target that you want to do. It's encode, decode, get_frequencies or hack.
  1) Input file name. You may not write this argument then will be used standart input.
  2) Output file name. You may not write this argument then will be used standart output.
  3) Cipher name: caesar, vigener or vernam.
  4) Key. It's number (1-26) if you choose caesar's cipher, string if you choose vigener's cipher and string no less then text in the input file.
  5) Name of file with frequencies. It will be used only if your target is hack, you may not 

  TODO
  ----
  Fix problems with Russian letters