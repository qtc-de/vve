import sys


class VimDummy:
    '''
    The unit tests require a 'vim' module, which is normally only avaibale when running
    from inside vim. In the following, we use this class as a dummy module and implement
    the only required function 'command' as a dummy function.
    '''

    def command(self, cmd):
        '''
        Dummy function that does nothing.
        '''


sys.modules['vim'] = VimDummy()
