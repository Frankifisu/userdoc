
Recover from Crash
==================

A calculation may terminate in two ways: controlled or uncontrolled. Controlled termination includes cases where the program itself detects an error and decides that continuation of the calculation is impossible or pointless. In all such cases the standard exit routine is executed, resulting in an output section with some final information. This also ensures that the general result file adf.rkf is closed properly and all relevant information flushed to it. 

*Uncontrolled* termination may occur, for instance when some bug causes the program to divide by zero, violate memory access restrictions, etc. Usually this leads to an immediate abort of the program by the Operating System and hence loss of control by the program. In such situations the information on adf.rkf may be incomplete because some of the data are kept in memory until the final termination of the program is carried out. It would be a terrible nuisance to see all time spent so far being lost. To remedy this ADF supports a check point file, named TAPE13, to help you recover at least some, if not most, of the results: not for analysis, but for continuation from a point not too long before the fatal condition occurred. TAPE13 can be used, just like adf.rkf, as a normal restart file in the ADF part of the input. See the restart key.
For restarting, for example, a geometry optimization, one should use the file ams.rkf, which is produced by the AMS driver, which should be used in the AMS part of the input.

