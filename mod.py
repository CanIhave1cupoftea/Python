#May 13, 2023
#Making a color function

def purple(arg):
    return f"\033[95m{arg}\033[0m"

def cyan(arg):
    return f"\033[96m{arg}\033[0m"

def darkcyan(arg):
    return f"\033[36m{arg}\033[0m"

def blue(arg):
    return f"\033[94m{arg}\033[0m"

def green(arg):
    return f"\033[92m{arg}\033[0m"

def red(arg):
    return f"\033[91m{arg}\033[0m"

def bold(arg):
    return f"\033[1m{arg}\033[0m"

def underline(arg):
    return f"\033[4m{arg}\033[0m"
