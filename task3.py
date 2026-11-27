green = '\033[32m'
red = '\033[31m'
blue = '\033[34m'
yellow = '\033[33m'
reset = '\033[0m'

def print_color(text, color_code):
    print( color_code+text+reset)

print_color ("hello sabiha", green)
print_color("how are you?",blue)
print_color("how was your day?",red)
print_color("well!",yellow)