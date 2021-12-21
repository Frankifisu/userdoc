
License file corrupt
====================

You may find that, after having installed the license file, the program still doesn't run and prints a message like 'your license file is corrupt'. To explain how this may come about, and how you overcome this, a few words on license files. 

Each license file consists of pairs of lines. The first of each pair is text that states, in more or less readable format typical aspects such as an expiration date, the version number of the software and so on. The second line contains the same information in encrypted format: a (long) string of characters that seem to make little sense. The program reads the license file and checks, with its internal encrypting formulas, that the two lines match. If not, it stops and prints the 'corrupt' message. So, there are two common reasons why it may happen to you: 

+ You are using a license file for another version of the software than your executables correspond to. Newer (major) releases may contain a different encrypting formula, so that the match in old license files is not recognized anymore. So, please verify that your license file and executable belong to the same major release.

+ More likely: the license file as it has been created has been modified in some way. Sometimes, people inspect it and 'clean it up' a little bit, for instance by removing 'redundant' spaces, or by making some other 'improvements'. Unfortunately, every such modification will destroy the encryption match and lead to the 'corrupt' error. Most of the times, however, the reason lies in the mailing system, by which the license file has been sent to you. If the encrypted line is rather long, the mailer may have cut it in two shorter lines. To verify (and correct) this: edit the license file and see if it consists of pairs of lines as described above. If not, re-unify the broken lines and try again.

+ Finally, the problem may lie in your OS, which may have inserted additional hidden CR characters (Carriage-Return) into the license file. You can remove them with our fix_license utility (in $AMSHOME/Install), see the Installation manual.

