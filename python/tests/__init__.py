# Pythons 'vim' module is normally only available when called from within vim. With this little
# hack, the module import works. As we only want to test the encoding and decoding functions,
# this should be sufficient
import sys
sys.modules['vim'] = "dummy"
