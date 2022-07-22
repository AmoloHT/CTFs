# Flag Box

## Informations

* Description: Find the flag from the following.
* File: Flag-Box
* Flag Format : BDSEC{Fl4g_h3r3}
* Author : marufmurtuza

## Getting the flag

I opened the "Flag-Box" file using Ghidra.

Functions:

```
0x01013f0 main
0x0101189 ox
```

main function:

```

undefined8 main(void)

{
  basic_ostream *this;
  int aiStack72 [11];
  int local_1c;
  int local_18;
  int local_14;
  int local_10;
  int local_c;
  
  local_18 = 0x159fd8;
  local_c = 1;
  std::operator<<((basic_ostream *)std::cout,
                  "\nWelcome to Flag-Box!\n\nPlease enter your 8 digit code to grab the flag:");
  std::basic_istream<char,std::char_traits<char>>::operator>>
            ((basic_istream<char,std::char_traits<char>> *)std::cin,&local_1c);
  for (local_10 = 8; -1 < local_10; local_10 = local_10 + -1) {
    aiStack72[local_10] = local_1c % 10;
    local_1c = local_1c / 10;
  }
  for (local_14 = 1; local_14 < 9; local_14 = local_14 + 1) {
    local_c = aiStack72[local_14] * local_c;
  }
  if (local_c == local_18) {
    this = std::operator<<((basic_ostream *)std::cout," ");
    std::basic_ostream<char,std::char_traits<char>>::operator<<
              ((basic_ostream<char,std::char_traits<char>> *)this,
               std::endl<char,std::char_traits<char>>);
    ox();
  }
  else {
    std::operator<<((basic_ostream *)std::cout,"\nSorry, wrong Code!\n\nBetter luck next time!");
  }
  return 0;
}
```

ox function:

```
undefined8 ox(void)

{
  basic_ostream *pbVar1;
  
  pbVar1 = std::operator<<((basic_ostream *)std::cout,'B');
  pbVar1 = std::operator<<(pbVar1,'D');
  pbVar1 = std::operator<<(pbVar1,'S');
  pbVar1 = std::operator<<(pbVar1,'E');
  pbVar1 = std::operator<<(pbVar1,'C');
  pbVar1 = std::operator<<(pbVar1,'{');
  pbVar1 = std::operator<<(pbVar1,'H');
  pbVar1 = std::operator<<(pbVar1,'u');
  pbVar1 = std::operator<<(pbVar1,'r');
  pbVar1 = std::operator<<(pbVar1,'r');
  pbVar1 = std::operator<<(pbVar1,'a');
  pbVar1 = std::operator<<(pbVar1,'h');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'U');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'g');
  pbVar1 = std::operator<<(pbVar1,'0');
  pbVar1 = std::operator<<(pbVar1,'t');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'i');
  pbVar1 = std::operator<<(pbVar1,'t');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'b');
  pbVar1 = std::operator<<(pbVar1,'u');
  pbVar1 = std::operator<<(pbVar1,'d');
  pbVar1 = std::operator<<(pbVar1,'d');
  pbVar1 = std::operator<<(pbVar1,'y');
  std::operator<<(pbVar1,'}');
  return 0;
}
```

Flag is being leaked by Ghidra decompile. Copy all the lines written "pbVar1" and paste it in a file called frag.txt.

flag.txt:

```
  pbVar1 = std::operator<<(pbVar1,'B');
  pbVar1 = std::operator<<(pbVar1,'D');
  pbVar1 = std::operator<<(pbVar1,'S');
  pbVar1 = std::operator<<(pbVar1,'E');
  pbVar1 = std::operator<<(pbVar1,'C');
  pbVar1 = std::operator<<(pbVar1,'{');
  pbVar1 = std::operator<<(pbVar1,'H');
  pbVar1 = std::operator<<(pbVar1,'u');
  pbVar1 = std::operator<<(pbVar1,'r');
  pbVar1 = std::operator<<(pbVar1,'r');
  pbVar1 = std::operator<<(pbVar1,'a');
  pbVar1 = std::operator<<(pbVar1,'h');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'U');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'g');
  pbVar1 = std::operator<<(pbVar1,'0');
  pbVar1 = std::operator<<(pbVar1,'t');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'i');
  pbVar1 = std::operator<<(pbVar1,'t');
  pbVar1 = std::operator<<(pbVar1,'_');
  pbVar1 = std::operator<<(pbVar1,'b');
  pbVar1 = std::operator<<(pbVar1,'u');
  pbVar1 = std::operator<<(pbVar1,'d');
  pbVar1 = std::operator<<(pbVar1,'d');
  pbVar1 = std::operator<<(pbVar1,'y');
```

I created a very simple script in Python to print only the flag characters.

flag.py:

```
frag = open('frag.txt', 'r').read().splitlines()
for character in frag:
    print(character[33], end='')
```

```
$ python3 frag.py
BDSEC{Hurrah_U_g0t_it_buddy}
```
