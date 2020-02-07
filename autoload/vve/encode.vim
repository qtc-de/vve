python3 << EOF
from vve.encode import encode_apply
EOF

function! vve#encode#Dispatch(function_name, type)
    if a:type == 'char'
        execute "normal! `[v`]\<ESC>"
        execute "python3 encode_apply('" . a:function_name . "', 'v')"

    elseif a:type == 'line'
        execute "normal! `[V`]\<ESC>"
        execute "python3 encode_apply('" . a:function_name . "', 'V')"

    else
        execute "python3 encode_apply('" . a:function_name . "', '" . a:type . "')"

    endif
endfunction

function! vve#encode#VisualEncodeBase64(type)
    call vve#encode#Dispatch('encode_base64', a:type)
endfunction

function! vve#encode#VisualDecodeBase64(type)
    call vve#encode#Dispatch('decode_base64', a:type)
endfunction

function! vve#encode#VisualEncodeBinary(type)
    call vve#encode#Dispatch('encode_binary', a:type)
endfunction

function! vve#encode#VisualDecodeBinary(type)
    call vve#encode#Dispatch('decode_binary', a:type)
endfunction

function! vve#encode#VisualEncodeHexString(type)
    call vve#encode#Dispatch('encode_hex_string', a:type)
endfunction

function! vve#encode#VisualDecodeHexString(type)
    call vve#encode#Dispatch('decode_hex_string', a:type)
endfunction

function! vve#encode#VisualEncodeHex(type)
    call vve#encode#Dispatch('encode_hex', a:type)
endfunction

function! vve#encode#VisualDecodeHex(type)
    call vve#encode#Dispatch('decode_hex', a:type)
endfunction

function! vve#encode#VisualEncodeURL(type)
    call vve#encode#Dispatch('encode_url', a:type)
endfunction

function! vve#encode#VisualDecodeURL(type)
    call vve#encode#Dispatch('decode_url', a:type)
endfunction

function! vve#encode#VisualEncodeURLFull(type)
    call vve#encode#Dispatch('encode_url_full', a:type)
endfunction

function! vve#encode#VisualEncodeHtmlFull(type)
    call vve#encode#Dispatch('encode_html_full', a:type)
endfunction

function! vve#encode#VisualEncodeXml(type)
    call vve#encode#Dispatch('encode_xml', a:type)
endfunction

function! vve#encode#VisualDecodeXml(type)
    call vve#encode#Dispatch('decode_xml', a:type)
endfunction 

function! vve#encode#VisualEncodeHtml(type)
    call vve#encode#Dispatch('encode_html', a:type)
endfunction

function! vve#encode#VisualDecodeHtml(type)
    call vve#encode#Dispatch('decode_html', a:type)
endfunction 
