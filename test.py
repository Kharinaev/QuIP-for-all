from tqdm import tqdm
import time

if __name__ == '__main__':
    for i in tqdm(range(3)):
        time.sleep(1)
        print('lalalala')
        if i == 2:
            raise ValueError('some error')
    print('2500')