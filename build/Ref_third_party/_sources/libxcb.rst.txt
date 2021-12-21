libxcb
------

Description: 
  A C binding to the X11 protocol.

  The xcb-util module provides a number of libraries which sit on top of
  libxcb, the core X protocol library, and some of the extension
  libraries. These experimental libraries provide convenience functions
  and interfaces which make the raw X protocol more usable. Some of the
  libraries also provide client-side code which is not strictly part of
  the X protocol but which have traditionally been provided by Xlib.

  - xcb-util-image
    Port of Xlib's XImage and XShmImage functions on top of libxcb    
  - xcb-util-keysyms
    keysyms: Standard X key constants and conversion to/from keycodes
  - xcb-util-renderutil
    Convenience functions for the Render extension
  - xcb-util-wm 
    Client and window-manager helper library on top of libxcb

  Several libxcb and libxcb-util shared library files are included to support Qt5 GUI components that depend on it.
  

Website: 
  `https://xcb.freedesktop.org/ <https://xcb.freedesktop.org/>`__ 

 
License: 
  MIT

Libxcb License and Copyright:
  .. code-block:: none

    Copyright (C) 2001-2006 Bart Massey, Jamey Sharp, and Josh Triplett.

    All Rights Reserved.

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated
    documentation files (the "Software"), to deal in the
    Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute,
    sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall
    be included in all copies or substantial portions of the
    Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
    KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
    BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

    Except as contained in this notice, the names of the authors
    or their institutions shall not be used in advertising or
    otherwise to promote the sale, use or other dealings in this
    Software without prior written authorization from the
    authors.


xcb-util-image License and Copyright:
  .. code-block:: none
    
    Copyright © 2007-2008 Bart Massey <bart@cs.pdx.edu>
    Copyright © 2008 Julien Danjou <julien@danjou.info>
    Copyright © 2008 Keith Packard <keithp@keithp.com>

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use, copy,
    modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY
    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    Except as contained in this notice, the names of the authors or
    their institutions shall not be used in advertising or otherwise to
    promote the sale, use or other dealings in this Software without
    prior written authorization from the authors.


xcb-util-renderutil License and Copyright:
  .. code-block:: none

    Copyright © 2000 Keith Packard

    Permission to use, copy, modify, distribute, and sell this software and its
    documentation for any purpose is hereby granted without fee, provided that
    the above copyright notice appear in all copies and that both that
    copyright notice and this permission notice appear in supporting
    documentation, and that the name of Keith Packard not be used in
    advertising or publicity pertaining to distribution of the software without
    specific, written prior permission.  Keith Packard makes no
    representations about the suitability of this software for any purpose.  It
    is provided "as is" without express or implied warranty.

    KEITH PACKARD DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
    INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
    EVENT SHALL KEITH PACKARD BE LIABLE FOR ANY SPECIAL, INDIRECT OR
    CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
    DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
    TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.

    Copyright © 2006 Jamey Sharp.

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
    ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    Except as contained in this notice, the names of the authors or their
    institutions shall not be used in advertising or otherwise to promote the
    sale, use or other dealings in this Software without prior written
    authorization from the authors.

    Copyright © 2006 Ian Osgood

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
    ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    Except as contained in this notice, the names of the authors or their
    institutions shall not be used in advertising or otherwise to promote the
    sale, use or other dealings in this Software without prior written
    authorization from the authors.

xcb-util-wm License & Copyright:
  .. code-block:: none
 
    Copyright © 2008-2011 Arnaud Fontaine <arnau@debian.org>
    Copyright © 2008-2011 Arnaud Fontaine <arnau@debian.org>
    Copyright © 2007-2008 Vincent Torri <vtorri@univ-evry.fr>
    
    Permission  is  hereby  granted,  free  of charge,  to  any  person
    obtaining  a copy  of  this software  and associated  documentation
    files   (the  "Software"),   to  deal   in  the   Software  without
    restriction, including without limitation  the rights to use, copy,
    modify, merge, publish,  distribute, sublicense, and/or sell copies
    of  the Software, and  to permit  persons to  whom the  Software is
    furnished to do so, subject to the following conditions:
    
    The  above copyright  notice and  this permission  notice  shall be
    included in all copies or substantial portions of the Software.
    
    THE SOFTWARE  IS PROVIDED  "AS IS", WITHOUT  WARRANTY OF  ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT  NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY,   FITNESS    FOR   A   PARTICULAR    PURPOSE   AND
    NONINFRINGEMENT. IN  NO EVENT SHALL  THE AUTHORS BE LIABLE  FOR ANY
    CLAIM,  DAMAGES  OR  OTHER  LIABILITY,  WHETHER  IN  AN  ACTION  OF
    CONTRACT, TORT OR OTHERWISE, ARISING  FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    
    Except as  contained in  this notice, the  names of the  authors or
    their institutions shall not be used in advertising or otherwise to
    promote the  sale, use or  other dealings in this  Software without
    prior written authorization from the authors.

 