python3 << EOF
from vve.strings import strings_apply, strings_invoke
EOF

function! vve#strings#Dispatch(function_name, type)

    if a:type == 'char'
        execute "normal! `[v`]\<esc>"
        execute "python3 strings_apply('" . a:function_name . "', 'v')"

    elseif a:type == 'line'
        execute "normal! `[V`]\<esc>"
        execute "python3 strings_apply('" . a:function_name . "', 'V')"

    else
        execute "python3 strings_apply('" . a:function_name . "', '" . a:type . "')"

    endif
endfunction

function! vve#strings#DispatchInvoke(function_name, type)

    if a:type == 'char'
        execute "normal! `[v`]\<esc>"
        execute "python3 strings_invoke('" . a:function_name . "')"

    elseif a:type == 'line'
        execute "normal! `[V`]\<esc>"
        execute "python3 strings_invoke('" . a:function_name . "')"

    else
        execute "python3 strings_invoke('" . a:function_name . "')"

    endif
endfunction

function! vve#strings#VisualSwapEndian(type)
    call vve#strings#Dispatch('swap_endian', a:type)
endfunction

function! vve#strings#VisualLength(type)
    call vve#strings#DispatchInvoke('string_length', a:type)
endfunction

function! vve#strings#VisualLengthHexString(type)
    call vve#strings#DispatchInvoke('string_length_hs', a:type)
endfunction

function! vve#strings#VisualUpper(type)
    call vve#strings#Dispatch('string_upper', a:type)
endfunction

function! vve#strings#VisualLower(type)
    call vve#strings#Dispatch('string_lower', a:type)
endfunction

function! vve#strings#VisualMarkdownHeadline(type)
    call vve#strings#Dispatch('string_markdown_headline', a:type)
endfunction

function! vve#strings#VisualSnakeCase(type)
    call vve#strings#Dispatch('string_snake_case', a:type)
endfunction

function! vve#strings#VisualCamelCase(type)
    call vve#strings#Dispatch('string_camel_case', a:type)
endfunction
