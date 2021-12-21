AMSPipe protocol specification
##############################

.. index:: Pipe protocol
.. _PipeProtocol:

The AMSPipe protocol is a remote procedure call protocol used for communication between two processes on the same computer.
One of these processes is the "pipe master", submitting geometries and requests for calculations and receiving the results.
The other process is the "pipe worker", which listens for calls from the master, executes the requested calculations and returns their results.

Communication takes place over a pair of pipes, a "call pipe" (master to worker) and a "reply pipe" (worker to master).
Each pipe carries a sequence of messages, which are processed in order.
Each message is an associative object (like a JSON object or a Python dict) containing a single item.
The key of this item denotes the name of the message, while the value of this item is another object containing the payload.

Each message sent over the call pipe constitutes a method call.
The name of the message is equal to the name of the method being called, while the payload object contains any arguments.
For methods without arguments, the payload is an empty object.

Once the worker receives a call message, it will execute the specified method and potentially write a sequence of zero or more messages to the reply pipe, containing the results of the calculation.
After the execution of the method is completed, the worker will write a "return" messages to the reply pipe, denoting the success or failure of the method call.

Any method whose name starts with "Set" doesn't send a "return" message.
Instead, errors encountered during the execution of a Set method are buffered by the worker to be returned the next time a "return" message is generated.
While an error is buffered, any further method calls are ignored by the worker and are not executed.
Once a non-Set call is seen by the worker, such a call will also be discarded without being executed, but a "return" message will be immediately generated with the buffered error data.
The buffered error will then be cleared and normal processing of calls resumes.

As a special case, the "Exit" method may be called at any time and will be immediately executed by the worker, terminating the protocol session.
The "Exit" method never returns a "return" message, discarding any potentially buffered error.

All values are always in atomic units: Hartree for energies, Bohr for distances, Hartree/Bohr for gradients etc.

Low-level message encoding
==========================

All messages are encoded using Universal Binary JSON.
AMSPipe implementations MAY encode messages using the UBJSON optimized container format (with explicit length and/or strong typing).
Implementations MUST support decoding UBJSON containers whether or not they're written using optimized format.

UBJSON arrays in messages MUST NOT contain other arrays or objects.
Multi-dimensional arrays MUST be flattened on encoding (and unflattened on decoding as necessary).
Flattening SHOULD preserve the original order of elements in memory.
All arrays MUST be accompanied by an additional integer array holding the original dimensions before flattening.
The name of this auxiliary array is equal to the name of the main array with a ``_dim_`` suffix.
The dimensions are written in Fortran (column-major) order, so that the first value in the ``_dim_`` array corresponds to the index that changes the fastests when iterating over consecutive elements of the flattened array.

Arrays also MUST NOT contain elements of incompatible types.
The elements of an array MUST be either all integers, all real numbers, all Boolean, or all strings.
UBJSON type "char" is equivalent to a UBJSON "string" of length 1 (elements of type "char" and "string" MAY thus be mixed in an array).
An empty array is equivalent to an array that is not present at all.

When sending messages over stream transport mechanisms (such as UNIX pipes), each message MUST be prefixed with a 32-bit native endian integer length.

Return messages and error handling
==================================

The "return" message consists of the following fields:

* "status" (integer): Zero for success or one of the error codes listed below.
* "method" (string, optional): Name of the method in which the error occurred.
* "argument" (string, optional): Name of the argument in error.
* "message" (string, optional): Human-readable error message.

The "status" field can have one of the following values:

0: success
   No error, method executed successfully.

1: decode_error
   Message could not be decoded correctly (invalid UBJSON encoding or a violation of one of the constraints above).

2: logic_error
   Programmer error, such as methods called in an incorrect sequence or with an invalid worker state.

3: runtime_error
   An error occurred during the execution of a method (outside of the AMSPipe protocol).

4: unknown_version
   (Only returned from "Hello".) Requested protocol version is not supported by the worker.

5: unknown_method
   A method of the requested name is not supported by the worker.

6: unknown_argument
   The argument in "argument" is not known to the worker and couldn't be processed. If multiple arguments to given single call are unknown, "argument" will be set to the one at the lowest nesting depth (if an argument contains nested objects). If multiple fields at the same nesting depth are unknown, the first one in ASCII sort order will be returned.

7: invalid_argument
   An argument doesn't have the correct type or dimensions, or it has an invalid value.

Methods
=======

Hello(version)
--------------

* "version" (integer):

Attempt to activate a given version of the AMSPipe protocol. Only version 1 is defined at the moment.

Other methods (with the exception of "Hello" and "Exit") MUST NOT be called until a Hello has completed successfully.
Pipe masters SHOULD attempt a Hello with the highest supported protocol version and iterate downwards if an unknown_version error is returned.
Once a Hello has succeeded, it MUST NOT be called again during the lifetime of a pipe session.

Exit()
------

Terminate the worker and disconnect both pipes.
This method never returns.

The worker MAY also discard any remembered calculations.

SetCoords(coords)
-----------------

* "coords" (real(3,:)):

Replace the Cartesian coordinates in the current chemical system. The number of atoms must match.

SetLattice(vectors)
-------------------

* "vectors" (real(:,:)):

Replace the lattice matrix of the current chemical system. If "vectors" is absent or of dimensions (0,0), make the system non-periodic.

SetSystem(atomSymbols, coords, totalCharge)
-------------------------------------------

* "atomSymbols" (string(:)):
* "coords" (real(3,:)):
* "totalCharge" (real):

Define a new chemical system.

Solve(request, keepResults, prevTitle)
--------------------------------------

* "request" (object):
   * "title" (string): Unique string key identifying this calculation.
   * "quiet" (bool): If true, the worker SHOULD keep any standard output from the calculation to a minimum.
   * "gradients" (bool): Calculate gradients on atoms.
   * "stressTensor" (bool): Calculate the stress tensor.
   * "elasticTensor" (bool):
   * "hessian" (bool):
   * "dipoleMoment" (bool):
   * "dipoleGradients" (bool):
* "keepResults" (bool, default false): Remember worker state for future restart.
* "prevTitle" (string, optional): Title of a previously stored calculation to restart from.

Run a single point calculation on the current chemical system and return a "results" object if successful. If the calculation fails with a runtime error, a "results" object MAY still be returned (possibly with just some of the requested properties).

All Boolean fields in "request" default to false if not present.
All non-Boolean fields in "request" except for "title" are optional and their default values are worker-dependent.
The master SHOULD NOT explicitly set any Boolean fields in "request" to False.
The worker MAY raise an unknown argument error if an unknown Boolean is set to False.
The worker SHOULD raise an unknown argument error as usual if an unknown Boolean is set to True or if an unknown non-Boolean is set.
Workers SHOULD raise these errors before performing any time-consuming calculations so that the master can efficiently retry the call.

If "keepResults" is not specified or set to false, the worker will discard all data from the calculation after returning a "results" object.
If "keepResults" is set to true, the worker will remember any internal state related to the calculation.
This internal state can later be reused for restart by passing the "title" of the stored calculation as "prevTitle".
The pipe master SHOULD call DeleteResults to discard the stored state as soon as it is no longer needed.

A "results" object consists of the following fields.
Workers MAY include additional fields not listed here.
A master MUST NOT signal an error due to any fields it does not expect or understand.

* "results" (object):
   * "messages" (string(:)): Runtime error or warning messages generated by the calculation.
   * "energy" (real):
   * "gradients" (real(3,:)):
   * "stressTensor" (real(:,:)):
   * "elasticTensor" (real(:,:)):
   * "hessian" (real(:,:)):
   * "dipoleMoment" (real(:,:)):
   * "dipoleGradients" (real(:,:)):
   * "charges" (real(:)):

DeleteResults(title)
--------------------

* "title" (string): Title of a previously remembered calculation.

Discard any worker state corresponding to a previously remembered calculation.

Forward and backward compatibility considerations
-------------------------------------------------

The AMSPipe protocol is designed to support combining new masters with old workers and vice versa.
Major, incompatible changes in the protocol will be handled by increasing the protocol version number.
Negotiating a suitable protocol version is then handled by call(s) to Hello at the beginning of a pipe session.

The following requirements are in place to ensure that the protocol stays extensible within a single protocol version:

* Workers MUST raise an unknown_method error on any call to a method they don't implement. If the method name starts with Set, such an error will be buffered to be returned later. If the method name doesn't start with Set, a "return" message will be generated immediately.
* Workers MUST raise unknown_argument errors any time they encounter an argument to a known method that they don't know how to handle. The master SHOULD then retry the call without such an argument or choose an alternative sequence of calls if possible.
* The master SHOULD ignore unexpected messages of unsupported type on the reply pipe.

Namely, the following changes are permitted without increasing the protocol version number:

* Adding new methods to the protocol.
* Adding new optional arguments to existing methods.
* Adding new fields to returned objects.
* Adding new reply message types.
