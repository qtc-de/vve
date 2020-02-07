python3 << EOF
from vve.numbers import numbers_apply
EOF

function! vve#numbers#Dispatch(function_name, type)

    if a:type == 'char'
        execute "normal! `[v`]\<esc>"
        execute "python3 numbers_apply('" . a:function_name . "', 'v')"

    elseif a:type == 'line'
        execute "normal! `[V`]\<esc>"
        execute "python3 numbers_apply('" . a:function_name . "', 'V')"

    else
        execute "python3 numbers_apply('" . a:function_name . "', '" . a:type . "')"

    endif
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

function! vve#numbers#VisualFromHexString(type)
    call vve#numbers#Dispatch('from_hex_string', a:type)
endfunction
