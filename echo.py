import argparse
import sys

def upper(text):
    uppercase = text.upper()
    return uppercase

def lower(text):
    lowercase = text.lower()
    return lowercase

def title(text):
    title = text.title()
    return title

def parser_create():
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument('-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument('-t', '--title', help='convert text to titlecase', action='store_true')
    return parser

def main():
    args = parser_create().parse_args()
    if args.title == True and args.upper == True and args.lower == True:
        uppercase = upper(args.text)
        lowercase = lower(uppercase)
        word = title(lowercase)
        print word
        return word
    elif args.upper == True:
        upper(args.text)
    elif args.lower == True:
        lower(args.text)
    elif args.title == True:
        title(args.text)


if __name__ == '__main__':
    main()