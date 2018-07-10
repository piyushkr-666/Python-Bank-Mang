import pickle
file=open('MaxAccount.bin','rb')
try:
    while True:
        t=pickle.load(file)
        print('Max account no till now =',t)
except EOFError:
    pass
file.close()
