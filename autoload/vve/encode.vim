python3 << EOF
from vve.encode import encode_apply, change_encoding
EOF


let s:encode_dict = {
    \ "ascii" : "encode_ascii",
    \ "base64" : "encode_base64",
    \ "binary" : "encode_binary",
    \ "hex" : "encode_hex",
    \ "hexstring" : "encode_hex_string",
    \ "htmlfull" : "encode_html_full",
    \ "json" : "encode_json",
    \ "jsonfull" : "encode_json_full",
    \ "url" : "encode_url",
    \ "urlfull" : "encode_url_full",
    \ "xmlfull" : "encode_xml_full",
    \ }


let s:decode_dict = {
    \ "ascii" : "decode_ascii",
    \ "base64" : "decode_base64",
    \ "binary" : "decode_binary",
    \ "hex" : "decode_hex",
    \ "hexstring" : "decode_hex_string",
    \ "htmlfull" : "decode_html_full",
    \ "json" : "decode_json",
    \ "url" : "decode_url",
    \ "urlfull" : "decode_url_full",
    \ "xmlfull" : "decode_xml_full",
    \ }


function! vve#encode#ListEncodings(A, L, P)
    let l:options = "ascii \n"
    let l:options .= "base64 \n"
    let l:options .= "binary \n"
    let l:options .= "hex \n"
    let l:options .= "hexstring \n"
    let l:options .= "htmlfull \n"
    let l:options .= "json \n"
    let l:options .= "jsonfull \n"
    let l:options .= "url \n"
    let l:options .= "urlfull \n"
    let l:options .= "xmlfull "
    return l:options
endfunction


function! vve#encode#Dispatch(function_name, type)
    let l:type = vve#utils#GetVisualMode(a:type)

    if l:type == "Nope"
        echom "[-] Unknown motion / visual type: " . a:type
        return
    endif

    execute "python3 encode_apply('" . a:function_name . "', '" . l:type . "')"
endfunction


function! vve#encode#VisualChangeEncoding(from, to, type)
    let l:type = vve#utils#GetVisualMode(a:type)

    if l:type == "Nope"
        echom "[-] Unknown motion / visual type: " . a:type
        return
    endif

    if !has_key(s:decode_dict, a:from)
        echom "[-] Unknown encoding: " . a:from
        return

    elseif !has_key(s:encode_dict, a:to)
        echom "[-] Unknown encoding: " . a:to
        return
    endif

    let l:from_function = s:decode_dict[a:from]
    let l:to_function = s:encode_dict[a:to]

    execute "python3 change_encoding('" . l:from_function . "', '" . l:to_function . "', '" . l:type . "')"
endfunction


function! vve#encode#VisualEncodeAscii(type)
    call vve#encode#Dispatch('encode_ascii', a:type)
endfunction


function! vve#encode#VisualDecodeAscii(type)
    call vve#encode#Dispatch('decode_ascii', a:type)
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


function! vve#encode#VisualEncodeJSON(type)
    call vve#encode#Dispatch('encode_json', a:type)
endfunction


function! vve#encode#VisualEncodeJSONFull(type)
    call vve#encode#Dispatch('encode_json_full', a:type)
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


function! vve#encode#VisualDecodeURLFull(type)
    call vve#encode#Dispatch('decode_url_full', a:type)
endfunction


function! vve#encode#VisualEncodeHtmlFull(type)
    call vve#encode#Dispatch('encode_html_full', a:type)
endfunction


function! vve#encode#VisualEncodeXml(type)
    call vve#encode#Dispatch('encode_xml', a:type)
endfunction


function! vve#encode#VisualEncodeXmlFull(type)
    call vve#encode#Dispatch('encode_xml_full', a:type)
endfunction


function! vve#encode#VisualDecodeXml(type)
    call vve#encode#Dispatch('decode_xml', a:type)
endfunction


function! vve#encode#VisualDecodeXmlFull(type)
    call vve#encode#Dispatch('decode_xml_full', a:type)
endfunction


function! vve#encode#VisualEncodeHtml(type)
    call vve#encode#Dispatch('encode_html', a:type)
endfunction


function! vve#encode#VisualDecodeHtml(type)
    call vve#encode#Dispatch('decode_html', a:type)
endfunction


function! vve#encode#VisualDecodeHtmlFull(type)
    call vve#encode#Dispatch('decode_html_full', a:type)
endfunction


function! vve#encode#VisualDecodeJSON(type)
    call vve#encode#Dispatch('decode_json', a:type)
endfunction


function! vve#encode#VisualEncodeBase64FromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'base64', a:type)
endfunction


function! vve#encode#VisualDecodeBase64ToAscii(type)
    call vve#encode#VisualChangeEncoding('base64', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeBinaryFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'binary', a:type)
endfunction


function! vve#encode#VisualDecodeBinaryToAscii(type)
    call vve#encode#VisualChangeEncoding('binary', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeHexStringFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'hexstring', a:type)
endfunction


function! vve#encode#VisualDecodeHexStringToAscii(type)
    call vve#encode#VisualChangeEncoding('hexstring', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeHexFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'hex', a:type)
endfunction


function! vve#encode#VisualDecodeHexToAscii(type)
    call vve#encode#VisualChangeEncoding('hex', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeURLFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'url', a:type)
endfunction


function! vve#encode#VisualDecodeURLToAscii(type)
    call vve#encode#VisualChangeEncoding('url', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeURLFullFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'urlfull', a:type)
endfunction


function! vve#encode#VisualDecodeURLFullToAscii(type)
    call vve#encode#VisualChangeEncoding('urlfull', 'ascii', a:type)
endfunction


function! vve#encode#VisualDecodeHtmlFullToAscii(type)
    call vve#encode#VisualChangeEncoding('htmlfull', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeHtmlFullFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'htmlfull', a:type)
endfunction


function! vve#encode#VisualDecodeXmlFullToAscii(type)
    call vve#encode#VisualChangeEncoding('xmlfull', 'ascii', a:type)
endfunction


function! vve#encode#VisualEncodeXmlFullFromAscii(type)
    call vve#encode#VisualChangeEncoding('ascii', 'xmlfull', a:type)
endfunction
