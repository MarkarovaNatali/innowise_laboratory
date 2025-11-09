from colorama import init, Fore, Back, Style

def main():
    # Initialize colorama with autoreset to avoid manual resets in each print
    init(autoreset=True)

    print(f"{Fore.RED}{Back.YELLOW}Hello World!")
    print(f"{Fore.BLUE}Hello World!")
    print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue!")
    print(f"{Fore.MAGENTA}{Back.CYAN}{Style.DIM}Hello World with Magenta text and Cyan background!")

if __name__ == "__main__":
    main()