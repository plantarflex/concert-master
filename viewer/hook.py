import time

def hook():
    while True:
        time.sleep(3)
        print('this container is online')


if __name__ == '__main__':
    hook()
