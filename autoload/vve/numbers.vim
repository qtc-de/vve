python3 << EOF
from vve.numbers import numbers_apply
EOF

function! vve#numbers#Dispatch(function_name, type)
    let l:type = vve#utils#GetVisualMode(a:type)

    if l:type == "Nope"
        echom "[-] Unknown motion / visual type: " . a:type
        return
    endif

    execute "python3 numbers_apply('" . a:function_name . "', '" . l:type . "')"
endfunction

function! vve#numbers#VisualToHex(type)
    call vve#numbers#Dispatch('to_hex', a:type)
endfunction

function! vve#numbers#VisualToBin(type)
    call vve#numbers#Dispatch('to_bin', a:type)
endfunction

function! vve#numbers#VisualToOct(type)
    call vve#numbers#Dispatch('to_oct', a:type)
endfunction

function! vve#numbers#VisualToDec(type)
    call vve#numbers#Dispatch('to_dec', a:type)
endfunction

function! vve#numbers#VisualInPlaceAdd(type)
    call vve#numbers#Dispatch('add', a:type)
endfunction

function! vve#numbers#VisualInPlaceSub(type)
    call vve#numbers#Dispatch('sub', a:type)
endfunction

function! vve#numbers#VisualInPlaceDiv(type)
    call vve#numbers#Dispatch('div', a:type)
endfunction

function! vve#numbers#VisualInPlaceMul(type)
    call vve#numbers#Dispatch('mul', a:type)
endfunction

function! vve#numbers#VisualToHexString(type)
    call vve#numbers#Dispatch('to_hex_string', a:type)
endfunction
