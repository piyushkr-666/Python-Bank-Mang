import pickle
file=open('MaxAccount.bin','wb')
while True:
    x='0'
    pickle.dump(x,file)
    break
file.close()


