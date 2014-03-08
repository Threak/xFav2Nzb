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

def test_colors():
	print font_colors.HEADER + 'HEADER' + font_colors.ENDC
	print font_colors.OKBLUE + 'OKBLUE' + font_colors.ENDC
	print font_colors.OKGREEN + 'OKGREEN' + font_colors.ENDC
	print font_colors.WARNING + 'WARNING' + font_colors.ENDC
	print font_colors.FAIL + 'FAIL' + font_colors.ENDC

if __name__ == '__main__':
    test_colors()