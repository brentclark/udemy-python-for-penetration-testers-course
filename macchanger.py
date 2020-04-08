import random
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='MD5 Cracker')
parser.add_argument('-i', dest='interface', help='interface', required=True)
parser_args = parser.parse_args()

def get_rand():
    return random.choice('abcdef0123456789')

def new_mac():
    new = ''
    for i in range(0,5):
        new += get_rand()+get_rand()+":"    
    new += get_rand()+get_rand()
    return new

def main():
    mac = open('/sys/class/net/'+parser_args.interface+'/address').readline().strip()
    print(f"mac is {mac}")

    subprocess.call(['sudo', 'ifconfig', parser_args.interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', parser_args.interface, 'hw', 'ether', new_mac()])
    subprocess.call(['sudo', 'ifconfig', parser_args.interface, 'up'])

    mac = open('/sys/class/net/'+parser_args.interface+'/address').readline().strip()
    print(f"mac is {mac}")

if __name__ == "__main__":
    main()