import multiprocessing

def proc (name):
    for i in range (1000000):
        print (name, i)



if __name__ == "__main__":
    p1 = multiprocessing.Process(target=proc, args=("A",))
    p1.start()

if __name__ == "__main__":
    p2 = multiprocessing.Process(target=proc, args=("B",))
    p2.start()