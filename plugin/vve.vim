if !has('python3')
    echo "[-] vim seems not to be compiled with python3 support"
    finish
endif

if exists('g:vve_loaded')
    finish
endif

let s:vve_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys, vim, os
vve_root_dir = vim.eval('s:vve_root_dir')
py_root_dir = os.path.normpath(os.path.join(vve_root_dir, '..', 'python'))
sys.path.insert(0, py_root_dir)
EOF

" encoding functions
nnoremap <leader>ea :set operatorfunc=vve#encode#VisualEncodeAscii<CR>g@
nnoremap <leader>eb :set operatorfunc=vve#encode#VisualEncodeBinary<CR>g@
nnoremap <leader>eB :set operatorfunc=vve#encode#VisualEncodeBase64<CR>g@
nnoremap <leader>ee :set operatorfunc=vve#encode#VisualEncodeHtml<CR>g@
nnoremap <leader>eE :set operatorfunc=vve#encode#VisualEncodeHtmlFull<CR>g@
nnoremap <leader>eh :set operatorfunc=vve#encode#VisualEncodeHex<CR>g@
nnoremap <leader>eH :set operatorfunc=vve#encode#VisualEncodeHexString<CR>g@
nnoremap <leader>eu :set operatorfunc=vve#encode#VisualEncodeURL<CR>g@
nnoremap <leader>eU :set operatorfunc=vve#encode#VisualEncodeURLFull<CR>g@
nnoremap <leader>ex :set operatorfunc=vve#encode#VisualEncodeXml<CR>g@
nnoremap <leader>eX :set operatorfunc=vve#encode#VisualEncodeXml<CR>g@

nnoremap <leader>da :set operatorfunc=vve#encode#VisualDecodeAscii<CR>g@
nnoremap <leader>db :set operatorfunc=vve#encode#VisualDecodeBinary<CR>g@
nnoremap <leader>dB :set operatorfunc=vve#encode#VisualDecodeBase64<CR>g@
nnoremap <leader>dh :set operatorfunc=vve#encode#VisualDecodeHex<CR>g@
nnoremap <leader>dH :set operatorfunc=vve#encode#VisualDecodeHexString<CR>g@
nnoremap <leader>du :set operatorfunc=vve#encode#VisualDecodeURL<CR>g@
nnoremap <leader>dU :set operatorfunc=vve#encode#VisualDecodeURLFull<CR>g@
nnoremap <leader>de :set operatorfunc=vve#encode#VisualDecodeHtml<CR>g@
nnoremap <leader>dE :set operatorfunc=vve#encode#VisualDecodeHtmlFull<CR>g@
nnoremap <leader>dx :set operatorfunc=vve#encode#VisualDecodeXml<CR>g@
nnoremap <leader>dX :set operatorfunc=vve#encode#VisualDecodeHtmlFull<CR>g@

nnoremap <leader>Eb :set operatorfunc=vve#encode#VisualEncodeBinaryFromAscii<CR>g@
nnoremap <leader>EB :set operatorfunc=vve#encode#VisualEncodeBase64FromAscii<CR>g@
nnoremap <leader>Eh :set operatorfunc=vve#encode#VisualEncodeHexFromAscii<CR>g@
nnoremap <leader>EH :set operatorfunc=vve#encode#VisualEncodeHexStringFromAscii<CR>g@
nnoremap <leader>Ee :set operatorfunc=vve#encode#VisualEncodeHtmlFullFromAscii<CR>g@
nnoremap <leader>EE :set operatorfunc=vve#encode#VisualEncodeHtmlFullFromAscii<CR>g@
nnoremap <leader>Eu :set operatorfunc=vve#encode#VisualEncodeURLFromAscii<CR>g@
nnoremap <leader>EU :set operatorfunc=vve#encode#VisualEncodeURLFullFromAscii<CR>g@
nnoremap <leader>Ex :set operatorfunc=vve#encode#VisualEncodeXmlFullFromAscii<CR>g@
nnoremap <leader>EX :set operatorfunc=vve#encode#VisualEncodeXmlFullFromAscii<CR>g@

nnoremap <leader>Db :set operatorfunc=vve#encode#VisualDecodeBinaryToAscii<CR>g@
nnoremap <leader>DB :set operatorfunc=vve#encode#VisualDecodeBase64ToAscii<CR>g@
nnoremap <leader>Dh :set operatorfunc=vve#encode#VisualDecodeHexToAscii<CR>g@
nnoremap <leader>DH :set operatorfunc=vve#encode#VisualDecodeHexStringToAscii<CR>g@
nnoremap <leader>Du :set operatorfunc=vve#encode#VisualDecodeURLToAscii<CR>g@
nnoremap <leader>DU :set operatorfunc=vve#encode#VisualDecodeURLFullToAscii<CR>g@
nnoremap <leader>De :set operatorfunc=vve#encode#VisualDecodeHtmlFullToAscii<CR>g@
nnoremap <leader>DE :set operatorfunc=vve#encode#VisualDecodeHtmlFullToAscii<CR>g@
nnoremap <leader>Dx :set operatorfunc=vve#encode#VisualDecodeXmlFullToAscii<CR>g@
nnoremap <leader>DX :set operatorfunc=vve#encode#VisualDecodeXmlFullToAscii<CR>g@

vnoremap <leader>ce :<c-u>ChangeEncoding 
vnoremap <leader>ea :<c-u>call vve#encode#VisualEncodeAscii(visualmode())<CR>
vnoremap <leader>eb :<c-u>call vve#encode#VisualEncodeBinary(visualmode())<CR>
vnoremap <leader>eB :<c-u>call vve#encode#VisualEncodeBase64(visualmode())<CR>
vnoremap <leader>ee :<c-u>call vve#encode#VisualEncodeHtml(visualmode())<CR>
vnoremap <leader>eE :<c-u>call vve#encode#VisualEncodeHtmlFull(visualmode())<CR>
vnoremap <leader>eh :<c-u>call vve#encode#VisualEncodeHex(visualmode())<CR>
vnoremap <leader>eH :<c-u>call vve#encode#VisualEncodeHexString(visualmode())<CR>
vnoremap <leader>eu :<c-u>call vve#encode#VisualEncodeURL(visualmode())<CR>
vnoremap <leader>eU :<c-u>call vve#encode#VisualEncodeURLFull(visualmode())<CR>
vnoremap <leader>ex :<c-u>call vve#encode#VisualEncodeXml(visualmode())<CR>
vnoremap <leader>eX :<c-u>call vve#encode#VisualEncodeXml(visualmode())<CR>

vnoremap <leader>da :<c-u>call vve#encode#VisualDecodeAscii(visualmode())<CR>
vnoremap <leader>db :<c-u>call vve#encode#VisualDecodeBinary(visualmode())<CR>
vnoremap <leader>dB :<c-u>call vve#encode#VisualDecodeBase64(visualmode())<CR>
vnoremap <leader>dh :<c-u>call vve#encode#VisualDecodeHex(visualmode())<CR>
vnoremap <leader>dH :<c-u>call vve#encode#VisualDecodeHexString(visualmode())<CR>
vnoremap <leader>du :<c-u>call vve#encode#VisualDecodeURL(visualmode())<CR>
vnoremap <leader>dU :<c-u>call vve#encode#VisualDecodeURLFull(visualmode())<CR>
vnoremap <leader>de :<c-u>call vve#encode#VisualDecodeHtml(visualmode())<CR>
vnoremap <leader>dE :<c-u>call vve#encode#VisualDecodeHtmlFull(visualmode())<CR>
vnoremap <leader>dx :<c-u>call vve#encode#VisualDecodeXml(visualmode())<CR>
vnoremap <leader>dX :<c-u>call vve#encode#VisualDecodeHtmlFull(visualmode())<CR>

vnoremap <leader>Eb :<c-u>call vve#encode#VisualEncodeBinaryFromAscii(visualmode())<CR>
vnoremap <leader>EB :<c-u>call vve#encode#VisualEncodeBase64FromAscii(visualmode())<CR>
vnoremap <leader>Eh :<c-u>call vve#encode#VisualEncodeHexFromAscii(visualmode())<CR>
vnoremap <leader>EH :<c-u>call vve#encode#VisualEncodeHexStringFromAscii(visualmode())<CR>
vnoremap <leader>Ee :<c-u>call vve#encode#VisualEncodeHtmlFullFromAscii(visualmode())<CR>
vnoremap <leader>EE :<c-u>call vve#encode#VisualEncodeHtmlFullFromAscii(visualmode())<CR>
vnoremap <leader>Eu :<c-u>call vve#encode#VisualEncodeURLFromAscii(visualmode())<CR>
vnoremap <leader>EU :<c-u>call vve#encode#VisualEncodeURLFullFromAscii(visualmode())<CR>
vnoremap <leader>Ex :<c-u>call vve#encode#VisualEncodeXmlFullFromAscii(visualmode())<CR>
vnoremap <leader>EX :<c-u>call vve#encode#VisualEncodeXmlFullFromAscii(visualmode())<CR>

vnoremap <leader>Db :<c-u>call vve#encode#VisualDecodeBinaryToAscii(visualmode())<CR>
vnoremap <leader>DB :<c-u>call vve#encode#VisualDecodeBase64ToAscii(visualmode())<CR>
vnoremap <leader>Dh :<c-u>call vve#encode#VisualDecodeHexToAscii(visualmode())<CR>
vnoremap <leader>DH :<c-u>call vve#encode#VisualDecodeHexStringToAscii(visualmode())<CR>
vnoremap <leader>Du :<c-u>call vve#encode#VisualDecodeURLToAscii(visualmode())<CR>
vnoremap <leader>DU :<c-u>call vve#encode#VisualDecodeURLFullToAscii(visualmode())<CR>
vnoremap <leader>De :<c-u>call vve#encode#VisualDecodeHtmlFullToAscii(visualmode())<CR>
vnoremap <leader>DE :<c-u>call vve#encode#VisualDecodeHtmlFullToAscii(visualmode())<CR>
vnoremap <leader>Dx :<c-u>call vve#encode#VisualDecodeXmlFullToAscii(visualmode())<CR>
vnoremap <leader>DX :<c-u>call vve#encode#VisualDecodeXmlFullToAscii(visualmode())<CR>


" number conversion :<c-u>call and inplace arithmetic
nnoremap <leader>th :set operatorfunc=vve#numbers#VisualToHex<CR>g@
nnoremap <leader>tH :set operatorfunc=vve#numbers#VisualToHexString<CR>g@
nnoremap <leader>tb :set operatorfunc=vve#numbers#VisualToBin<CR>g@
nnoremap <leader>to :set operatorfunc=vve#numbers#VisualToOct<CR>g@
nnoremap <leader>td :set operatorfunc=vve#numbers#VisualToDec<CR>g@
nnoremap <leader>ma :set operatorfunc=vve#numbers#VisualInPlaceAdd<CR>g@
nnoremap <leader>ms :set operatorfunc=vve#numbers#VisualInPlaceSub<CR>g@
nnoremap <leader>mm :set operatorfunc=vve#numbers#VisualInPlaceMul<CR>g@
nnoremap <leader>md :set operatorfunc=vve#numbers#VisualInPlaceDiv<CR>g@

vnoremap <leader>th :<c-u>call vve#numbers#VisualToHex(visualmode())<CR>
vnoremap <leader>tH :<c-u>call vve#numbers#VisualToHexString(visualmode())<CR>
vnoremap <leader>tb :<c-u>call vve#numbers#VisualToBin(visualmode())<CR>
vnoremap <leader>to :<c-u>call vve#numbers#VisualToOct(visualmode())<CR>
vnoremap <leader>td :<c-u>call vve#numbers#VisualToDec(visualmode())<CR>
vnoremap <leader>ma :<c-u>call vve#numbers#VisualInPlaceAdd(visualmode())<CR>
vnoremap <leader>ms :<c-u>call vve#numbers#VisualInPlaceSub(visualmode())<CR>
vnoremap <leader>mm :<c-u>call vve#numbers#VisualInPlaceMul(visualmode())<CR>
vnoremap <leader>md :<c-u>call vve#numbers#VisualInPlaceDiv(visualmode())<CR>

" other util functions
nnoremap <leader>se :set operatorfunc=vve#strings#VisualSwapEndian<CR>g@
nnoremap <leader>sc :set operatorfunc=vve#strings#VisualLength<CR>g@
nnoremap <leader>sC :set operatorfunc=vve#strings#VisualLengthHexString<CR>g@
nnoremap <leader>su :set operatorfunc=vve#strings#VisualUpper<CR>g@
nnoremap <leader>sl :set operatorfunc=vve#strings#VisualLower<CR>g@
nnoremap <leader>fc :set operatorfunc=vve#strings#VisualCamelCase<CR>g@
nnoremap <leader>fs :set operatorfunc=vve#strings#VisualSnakeCase<CR>g@
nnoremap <leader>fm :set operatorfunc=vve#strings#VisualMarkdownAnchor<CR>g@
nnoremap <leader>fM :set operatorfunc=vve#strings#VisualMarkdownAnchorReference<CR>g@

vnoremap <leader>se :<c-u>call vve#strings#VisualSwapEndian(visualmode())<CR>
vnoremap <leader>sc :<c-u>call vve#strings#VisualLength(visualmode())<CR>
vnoremap <leader>sC :<c-u>call vve#strings#VisualLengthHexString(visualmode())<CR>
vnoremap <leader>su :<c-u>call vve#strings#VisualUpper(visualmode())<CR>
vnoremap <leader>sl :<c-u>call vve#strings#VisualLower(visualmode())<CR>
vnoremap <leader>fc :<c-u>call vve#strings#VisualCamelCase(visualmode())<CR>
vnoremap <leader>fs :<c-u>call vve#strings#VisualSnakeCase(visualmode())<CR>
vnoremap <leader>fm :<c-u>call vve#strings#VisualMarkdownAnchor(visualmode())<CR>
vnoremap <leader>fM :<c-u>call vve#strings#VisualMarkdownAnchorReference(visualmode())<CR>

" some util commands
command! -nargs=1 -complete=file InsertFile :exec "normal i" . fnamemodify(<q-args>, ":t") . "\<esc>"
command! -nargs=1 -complete=file AppendFile :exec "normal a" . fnamemodify(<q-args>, ":t") . "\<esc>"
command! -nargs=1 -complete=file InsertPath :exec "normal i" . <q-args> . "\<esc>"
command! -nargs=1 -complete=file AppendPath :exec "normal a" . <q-args> . "\<esc>"
command! -nargs=+ -complete=custom,vve#encode#ListEncodings ChangeEncoding :call vve#encode#VisualChangeEncoding(<f-args>, visualmode())

let g:vve_loaded = 1
