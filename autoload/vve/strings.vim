python3 << EOF
from vve.strings import strings_apply, strings_invoke
EOF

function! vve#strings#Dispatch(function_name, type)
    let l:type = vve#utils#GetVisualMode(a:type)

    if l:type == "Nope"
        echom "[-] Unknown motion / visual type: " . a:type
        return
    endif

    execute "python3 strings_apply('" . a:function_name . "', '" . l:type . "')"
endfunction

function! vve#strings#DispatchInvoke(function_name, type)
    let l:type = vve#utils#GetVisualMode(a:type)

    if l:type == "Nope"
        echom "[-] Unknown motion / visual type: " . a:type
        return
    endif

    execute "python3 strings_invoke('" . a:function_name . "')"
endfunction

function! vve#strings#VisualSwapEndian(type)
    call vve#strings#Dispatch('swap_endian', a:type)
endfunction

function! vve#strings#VisualLength(type)
    call vve#strings#DispatchInvoke('string_length', a:type)
endfunction

function! vve#strings#VisualLengthHexString(type)
    call vve#strings#DispatchInvoke('string_length_hex', a:type)
endfunction

function! vve#strings#VisualLineLength(type)
    call vve#strings#DispatchInvoke('line_count', a:type)
endfunction

function! vve#strings#VisualUpper(type)
    call vve#strings#Dispatch('string_upper', a:type)
endfunction

function! vve#strings#VisualLower(type)
    call vve#strings#Dispatch('string_lower', a:type)
endfunction

function! vve#strings#VisualMarkdownAnchor(type)
    call vve#strings#Dispatch('string_markdown_anchor', a:type)
endfunction

function! vve#strings#VisualMarkdownAnchorReference(type)
    call vve#strings#Dispatch('string_markdown_anchor_reference', a:type)
endfunction

function! vve#strings#VisualSnakeCase(type)
    call vve#strings#Dispatch('string_snake_case', a:type)
endfunction

function! vve#strings#VisualCamelCase(type)
    call vve#strings#Dispatch('string_camel_case', a:type)
endfunction
