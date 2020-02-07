import re
import vim

def visual_select():
    '''
    This function needs to be called from within Vim. It returns the contents of
    the last visual selection.

    Parameters:
        None

    Returns:
        selection               (string)            Contents of the last visual selection
    '''
    vim.command("let b:vve_reg_backup = [getreg('0'), getregtype('0')]")
    vim.command("normal! gvy")
    selection = vim.eval("getreg('0')")
    vim.command("call setreg('0', b:vve_reg_backup[0], b:vve_reg_backup[1])")
    return selection


def visual_paste(string, visual_mode):
    '''
    This function needs to be called from within Vim. Overrides the contents of the last
    visual selection with the contents of {string}.

    Parameters:
        string                  (string)            Contents used for the replacement
        visual_mode             (string)            Register mode of {string} (v,V,^V)

    Returns:
        None
    '''
    vim.command("let b:vve_reg_backup = [getreg('0'), getregtype('0')]")
    buf = vim.current.buffer
    buf.vars['vve_replace_value'] = string
    vim.command("call setreg('0', b:vve_replace_value, '" + visual_mode + "')")
    vim.command('normal! gv"0p')
    vim.command("call setreg('0', b:vve_reg_backup[0], b:vve_reg_backup[1])")


def visual_apply(funcref, visual_mode):
    '''
    This function needs to be called from within Vim. It applies the specified
    {funcref} on the contents of the last visual selection and replaces the last
    visual selection with the result.

    Parameters:
        funcref                 (funcref)           Function reference to apply
        visual_mode             (string)            Register mode of last selection (v,V,^V)

    Returns:
        None
    '''
    selection = visual_select()
    if visual_mode == 'v':
        applied = funcref(selection)
    elif re.match('V|\\', visual_mode):
        lines = selection.split('\n')
        lines = list(map(lambda x: funcref(x), lines))
        applied = "\n".join(lines)
    else:
        print("[Error] - This function has to be called from visualmode", end="")
        return 1
    visual_paste(applied, visual_mode)
