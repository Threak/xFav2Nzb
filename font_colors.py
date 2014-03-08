#!/usr/bin/env python2

class font_colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'

	BLOCK_OKGREEN = '\033[102m'
	BLOCK_WARNING = '\033[103m'
	BLOCK_FAIL = '\033[101m'

	ENDC = '\033[0m'

	# SPECIAL
	s_reset   = '\033[ 0m'
	s_bright  = '\033[ 1m'
	s_dim     = '\033[ 2m'
	s_normal  = '\033[22m'

	# FOREGROUND:
	f_black   = '\033[30m'
	f_red     = '\033[31m'
	f_green   = '\033[32m'
	f_yellow  = '\033[33m'
	f_blue    = '\033[34m'
	f_magenta = '\033[35m'
	f_cyan    = '\033[36m'
	f_white   = '\033[37m'
	f_reset  = '\033[39m'

	# BACKGROUND
	b_black   = '\033[40m'
	b_red     = '\033[41m'
	b_green   = '\033[42m'
	b_yellow  = '\033[43m'
	b_blue    = '\033[44m'
	b_magenta = '\033[45m'
	b_cyan    = '\033[46m'
	b_white   = '\033[47m'
	b_reset   = '\033[49m'

def test_colors():
	print font_colors.HEADER + 'HEADER' + font_colors.ENDC
	print font_colors.OKBLUE + 'OKBLUE' + font_colors.ENDC
	print font_colors.OKGREEN + 'OKGREEN' + font_colors.ENDC
	print font_colors.WARNING + 'WARNING' + font_colors.ENDC
	print font_colors.FAIL + 'FAIL' + font_colors.ENDC
	print ''
	print 'New Tests:'
	print '%sf_black  %s' % (font_colors.f_black  , font_colors.f_reset, )
	print '%sf_red    %s' % (font_colors.f_red    , font_colors.f_reset, )
	print '%sf_green  %s' % (font_colors.f_green  , font_colors.f_reset, )
	print '%sf_yellow %s' % (font_colors.f_yellow , font_colors.f_reset, )
	print '%sf_blue   %s' % (font_colors.f_blue   , font_colors.f_reset, )
	print '%sf_magenta%s' % (font_colors.f_magenta, font_colors.f_reset, )
	print '%sf_cyan   %s' % (font_colors.f_cyan   , font_colors.f_reset, )
	print '%sf_white  %s' % (font_colors.f_white  , font_colors.f_reset, )
	print '%sf_reset  %s' % (font_colors.f_reset  , font_colors.f_reset, )

if __name__ == '__main__':
	test_colors()