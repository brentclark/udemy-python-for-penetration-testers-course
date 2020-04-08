import hashlib
import argparse

parser = argparse.ArgumentParser(description='MD5 Cracker')
parser.add_argument('-md5', dest='hash', help='md5 hash', required=True)
parser.add_argument('-w', dest='wordlist', help='wordlist', required=True)
parser_args = parser.parse_args()

def main():
    hash_cracked = None
    with open(parser_args.wordlist) as file:
        for line in file:
            line = line.strip()

            if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == parser_args.hash:
                hash_cracked = line
                print(f"Password Cracked: {hash_cracked}")
                exit
    
    if hash_cracked is None:
        print("Failed to crack password")

if __name__ == "__main__":
    main()
