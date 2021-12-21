
Input ignored
=============

**Problem**: the program doesn't get past input and aborts with a message eof while reading (....). Or the program seems to ignore some parts of input and as a consequence goes wrong somewhere. Or it seems that part of the input has not been read correctly or not at all. 

**Cause 1**. You have used tab characters in your input file. These are not normally visible when you edit your file, but they will affect the program's scanning of the input. When you use tab characters in the input, it is very likely that the program will do something wrong somewhere. Tabs may be ignored by the program, so that items that you believed were separate (by a tab!) are in fact read as contiguous. 

**Check**: the input file on tab characters. 

**Cause 2**: misusage of one of the block-type keys or general keys. 

A case that relatively often shows up is typing a title as first line of the input file, *without preceding it by the keyword title*. The program does not understand this as the title, but rather tries to interpret the first word as a keyword. This leads to an error if the first word is recognized as one of the pre-defined block-type keys (possibly abbreviated). 

**Check**: the input file on usage of block-type keys and on proper usage of a title. 

**Cause 3**: incorrect processing of expressions or unintended replacement of names by numerical values. Various kinds of mis-typing or incorrect usage of variables may cause this. 

**Check**: how the program sees input, *after parsing*. This can be done by rerunning the job, with as first line in input : print parser. 

This will cause the program to copy each input line *twice* to output, the second time after having parsed it. You may use StopAfter Input or StopAfter Init to let the program quit early so you can inspect what is going on with the input reading. 

