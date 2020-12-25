function! vve#utils#GetVisualMode(type)
    if a:type == 'char'
        execute "normal! `[v`]\<ESC>"
        return 'v'

    elseif a:type == 'line'
        execute "normal! `[V`]\<ESC>"
        return 'V'

    elseif a:type =~ '^\(v\|V\|\)$'
        return a:type

    else
        return "Nope"
    endif
endfunction


