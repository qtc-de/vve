python3 << EOF
from vve.encode import encode_apply, change_encoding
EOF

let s:encode_dict = {
    \ "ascii" : "encode_ascii",
    \ "base64" : "encode_base64",
    \ "binary" : "encode_binary",
    \ "hex" : "encode_hex",
    \ "hexstring" : "encode_hex_string",
    \ "url" : "encode_url",
    \ "url_full" : "encode_url_full"
    \ }

let s:decode_dict = {
    \ "ascii" : "decode_ascii",
    \ "base64" : "decode_base64",
    \ "binary" : "decode_binary",
    \ "hex" : "decode_hex",
    \ "hexstring" : "decode_hex_string",
    \ "url" : "decode_url",
    \ "url_full" : "decode_url"
    \ }


function! vve#encode#ListEncodings(A, L, P)
    let l:options = "ascii \n"
    let l:options .= "base64 \n"
    let l:options .= "binary \n"
    let l:options .= "hex \n"
    let l:options .= "hexstring \n"
    let l:options .= "url \n"
    let l:options .= "urlfull "
    return l:options
endfunction

function! vve#encode#Dispatch(function_name, type)
    if a:type == 'char'
        execute "normal! `[v`]\<ESC>"
        execute "python3 encode_apply('" . a:function_name . "', 'v')"

    elseif a:type == 'line'
        execute "normal! `[V`]\<ESC>"
        execute "python3 encode_apply('" . a:function_name . "', 'V')"

    elseif a:type =~ '^\(v\|V\|\)$'
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

function! vve#encode#VisualChangeEncoding(from, to)

    if !has_key(s:decode_dict, a:from)
        echom "[-] Unknown encoding: " . a:from
        return

    elseif !has_key(s:encode_dict, a:to)
        echom "[-] Unknown encoding: " . a:to
        return

    elseif visualmode() == ""
        echom "[-] ChangeEncoding has to be called after or from a visual selection."
        return
    endif

    let l:from_function = s:decode_dict[a:from]
    let l:to_function = s:encode_dict[a:to]

    execute "python3 change_encoding('" . l:from_function . "', '" . l:to_function . "', '" . visualmode() . "')"

endfunction
