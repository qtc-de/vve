### Various Vim Encoders

----

![](https://github.com/qtc-de/vve/workflows/master%20Python%20CI/badge.svg?branch=master)
![](https://github.com/qtc-de/vve/workflows/develop%20Python%20CI/badge.svg?branch=develop)
[![](https://img.shields.io/badge/version-1.1.0-blue)](https://github.com/qtc-de/vve/releases)
![](https://img.shields.io/badge/python-9%2b-blue)
[![](https://img.shields.io/badge/license-GPL%20v3.0-blue)](https://github.com/qtc-de/vve/blob/master/LICENSE)

*Various Vim Encoders* is a small Vim plugin which adds encoding capabilities to the Vim editor.
It configures key mappings for the most commonly used encoding schemes and enables you to transform
text without leaving your editor. Some of its features include:

* Base64 encoding/decoding
* HTML encoding/decoding
* URL encoding/decoding
* HEX encoding/decoding
* Binary encoding/decoding
* [...]


![vve-example](https://tneitzel.eu/73201a92878c0aba7c3419b7403ab604/vve.gif)


The current version of *vve* does also support some features which are not really encoding related.
These features have proven to be useful, but may be removed in future versions. Some of these
features include:

* Number conversion
* In place arithmetic
* Endian Swapper
* Length Calculation
* [...]


### Installation 

----

*vve* is structured according to Vim's plugin specifications and can be consumed by Vim's native
package manager as well as by several other tools like *Vundle* or *Pathogen*. 

If you use Vim's native package manager, just clone the repository in either the ``start`` or ``opt``
folder of your Vim configuration folder. E.g.:

```console
$ cd ~/.vim/pack/plugins/start/
$ git clone https://github.com/qtc-de/vve
```

If you have chosen the ``start`` folder, *vve* will be available on each startup of Vim. If you decided
to use the ``opt`` folder, you have to call ``:packadd vve`` from within Vim to enable it. 

If you use an external package manager please read the corresponding manual on how to add additional
plugins.


### Usage

-----

*vve* makes extensive usage of Vim's Python3 integration and uses VimL functions as wrappers around the
actual python code. However, interfacing with the functions directly should not be required and only the
key mappings are of interest in this description.

*vve* defines key mappings with identical functionality for normal and visual mode. While the visual mode
mappings operate on the data that has been selected, the normal mode mappings switch to operator pending
mode and expect a motion to define the area of effect.

By default, most mappings expect the encoded input and decoded output to be represented in *UTF-8* format.
If *UTF-8* representation is not possible (e.g. when decoding stuff like ``//8=``), you should use the
*ASCII* version of the *vve operation*. *ASCII* in the context of *vve* means, that all *ASCII* characters
are displayed as normal, while all others are displayed as escape sequences (e.g. ``\xff``). Check the
[Unprintable Characters](#unprintable-characters) section for more details.

The following mappings are currently defined (notice that each key combination needs to be prefixed by your \<leader\> key):


**Visual Mode Only Mappings**

| Key       |Description                                                  |
|:---------:|-------------------------------------------------------------|
| ce        |Open ChangeEncoding menu                                     |


**Encoding Related Mappings Operating on UTF-8**

| Key       |Description                                                  |
|:---------:|-------------------------------------------------------------|
| ea        |Encode as ascii                                              |
| eb        |Encode as binary                                             |
| eB        |Encode as base64                                             |
| ee        |Encode HTML special characters (entities)                    |
| eE        |Encode all characters as HTML (entities)                     |
| eh        |Encode as hex                                                |
| eH        |Encode as hex string                                         |
| ej        |Encode as JSON string                                        |
| eJ        |Encode all characters as JSON                                |
| eu        |Encode URL special characters                                |
| eU        |Encode all characters as URL                                 |
| ex        |Encode XML special characters                                |
| eX        |Currently the same as ex                                     |
| da        |Decode ascii                                                 |
| db        |Decode binary                                                |
| dB        |Decode base64                                                |
| dh        |Decode hex                                                   |
| dH        |Decode hex string                                            |
| dj        |Decode JSON string                                           |
| dJ        |Decode JSON string                                           |
| du        |Decode URL                                                   |
| dU        |Decode URL Full                                              |
| de        |Decode HTML                                                  |
| dE        |Decode HTML Full                                             |
| dx        |Decode XML                                                   |
| dX        |Decode XML Full                                              |


**Encoding Related Mappings Operating on ASCII**

| Key       |Description                                                  |
|:---------:|-------------------------------------------------------------|
| Eb        |Encode as binary                                             |
| EB        |Encode as base64                                             |
| Ee        |Encode all characters as HTML (entities)                     |
| EE        |Encode all characters as HTML (entities)                     |
| Eh        |Encode as hex                                                |
| EH        |Encode as hex string                                         |
| Eu        |Encode URL special characters                                |
| EU        |Encode all characters as URL                                 |
| Ex        |Encode all characters as XML (entities)                      |
| EX        |Encode all characters as XML (entities)                      |
| Db        |Decode binary                                                |
| DB        |Decode base64                                                |
| Dh        |Decode hex                                                   |
| DH        |Decode hex string                                            |
| Du        |Decode URL                                                   |
| DU        |Decode URL Full                                              |
| De        |Decode HTML                                                  |
| DE        |Decode HTML Full                                             |
| Dx        |Decode XML                                                   |
| DX        |Decode XML Full                                              |


**Number Related Mappings**

| Key       |Description                                                  |
|:---------:|-------------------------------------------------------------|
| th        |To hex format                                                |
| tH        |To hex string format                                         |
| tb        |To binary format                                             |
| to        |To octal format                                              |
| td        |To decimal format                                            |
| ma        |In place addition                                            |
| ms        |In place subtraction                                         |
| mm        |In place multiplication                                      |
| md        |In place division                                            |


**String Related Mappings**

| Key       |Description                                                  |
|:---------:|-------------------------------------------------------------|
| se        |Swap endianess of hex strings                                |
| sc        |Echo string length                                           |
| sC        |Echo hex string length                                       |
| su        |Convert to upper                                             |
| sl        |Convert to lower                                             |
| sn        |Echo number of selected lines                                |
| fc        |Convert to camelCase (from snake_case)                       |
| fs        |Convert to snake_case (from camelCase)                       |
| fm        |Convert to markdown anchor                                   |
| fM        |Convert to markdown anchor reference                         |

Apart from the mappings, *vve* defines one encoding related *vim-command*: ``ChangeEncoding``.
While being in *visual mode*, you can either use ``<leader>ce`` or type ``:<c-u>ChangeEncoding``
to open the encoding menu. ``ChangeEncoding`` expects two arguments.

1. The encoding you are coming from.
2. The encoding you are going to.

E.g. after selecting some *base64* encoded text, you can use ``:ChangeEncoding base64 hex``
to convert the *base64* encoded text directly into *hex* format.


### Unprintable Characters

----

Decoding arbitrary portions of text inside of an editor has of course certain limitations.
If the decoded result contains non *UTF-8* conform character codes, the decoding operation
might fail. In these cases, *vve* will show an error like:

```
[Error] - Decoded result cannot be encoded as UTF-8.
```

However, in certain situations working with non *UTF-8* data is desired and *vve* supports
two workarounds to allow it:

1. For (almost) each operation, *vve* supports an *ascii* variant. In the context of *vve*
   *ascii* encoding means basically that *ascii* characters are displayed like usual,
   while all other characters are displayed as escape sequences.
   
   As an example, consider you want to decode the base64 encoded value ``SGVsbG8g/yBXb3JsZA==``.
   Using the ordinary ``<leader>dB`` command will fail, as the result contains non valid unicode
   characters. The *ascii* variant (``<leader>DB``), on the other hand, will decode this
   to ``Hello \xff World``.

2. A common scenario for dealing with non printable characters is when switching encoding.
   E.g. consider you want to switch from the hex encoded string ``aafefaeac3b1`` to its
   base64 variant. Decoding the value with ``<leader>dh`` and encoding it with ``<leader>eB``
   will not work, as the decoding operation results in non *UTF-8* characters.
   
   To allow such operations, *vve* supports the ``:ChangeEncoding`` command. Just visual select
   the hex string ``aafefaeac3b1`` and type ``:ChangeEncoding hex base64`` and the value
   should be encoded as ``qv766sOx`` (you can also type ``<leader>ce`` to open the ``ChangeEncoding``
   menu).


### Full Operations

----

*vve* defines several operations that have the term *Full* as part of their name. The meaning of *Full*
slightly differs depending whether the corresponding operation is an encoding or decoding operation.

* **For encoding operations**, *Full* does basically mean that all characters are converted. Using
  *URL encoding* as example, the string ``Hello World`` would normally be encoded as ``Hello+World``,
  as the space character is the only one that really needs to be encoded. The *Full* operation, on the
  other hand, will encode all characters no matter whether encoding is required.

* **For decoding operations**, *Full* operations are basically an alternative implementation. Lets take
  *URL encoding* again as an example. When using the ordinary *URL decode* operation (``<leader>du``),
  *vve* will just use a library function for decoding. This is fine for *90%* of the cases, but
  sometimes it causes unexpected results. E.g. when using the library function to decode ``%ff``
  to *ascii* representation (``<leader>Du``), you will get ``\xef\xbf\xbd``. This is because the library
  function tries to apply *UTF-8* encoding, but ``%ff`` is no valid *UTF-8* format.
  The *Full* (alternative) implementation (``<leader>DU``) will decode ``%ff`` to ``\xff`` which is probably
  what you expect.

In most situation, using the *non-Full* operations should be fine. However, when working with non-printable
characters, the *non-Full* operations can behave unexpected and using *Full* operations might fix that.


### Final Remark

----

To be honest, working with encodings is just a nightmare. There are plenty different possibilities how to
implement different encodings and taking these design decisions is just a mess. Don't expect *vve* to work
*100%* reliable. We invested some effort to make this tool working reliable for general usage, but there
are certainly some edge cases that are not covered yet.


*Copyright 2020, Tobias Neitzel and the vve contributors.*
