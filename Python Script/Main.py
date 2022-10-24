import os

os.system('cls')

program_list = ['Pembayaran.py']

for program in program_list:
    exec(open(program).read())