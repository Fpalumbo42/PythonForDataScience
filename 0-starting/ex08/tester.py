from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(10000)):
    sleep(0.005)
for elem in tqdm(range(10000)):
    sleep(0.005)
print()