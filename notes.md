### Notes

----

This file just contains some notes about the project. To be honest, working with encoding is a
pure nightmare. There are so many decisions that need to be made and it seems impossible to
cover all possible edge cases. This file contains some design decisions just for me and other
contributors to remember about :D


### Why no default encoders / decoders?

----

Some operations (e.g. the url decoding) are not done using library functions but
by some custom python code. This is usually done because the library functions have
certain limitations in their supported encoding.

As an example, imagine you want to url decode the following string:

```
Hello+World+%ff+:D
```

Pythons default url decoding modules try to convert the output to ``utf-8``, but ``\xff``
is no valid ``utf-8`` character. Therefore, the output of the function will contain the �
character instead.

If you intended to display the decoded output in *vim*, this is a reasonable choice, but
when converting to different formats it is annoying. Converting the above output to hex
it will look like:

```
48656c6c6f20576f726c6420efbfbd203a44
```

Which is probably not what you wanted. Instead, the custom url decoder will convert
the sequence ``%ff`` to the literal byte value ``ff``. This way, the ``utf-8`` decoding
will fail, but switching to other encodings should work fine.


### Why no ``.encode('utf-8')``?

----

In some locations a custom encoding function is used in favor of pythons default ``.encode('utf-8')``.
The reason is that the ``encode`` function will modify certain byte values during convertion. As an
example, consider you want to convert the following url encoded string to hex encoding:

```
•+This+is+%ff+a+Test+•
```

The ``encode`` function will convert the sequence ``%ff`` to ``\xc3\xbf``, which is probably not what you want.
The custom encoding function walks over each code point, checks whether it is in a range from ``0`` to ``255``
and converts it to the raw byte value in these cases. Only if this convertion fails, ``utf-8`` formatting is
used.

