import random
import shutil
import sys, os
from math import ceil

sys.path.append(os.path.dirname(__file__) + os.sep + '../')

from utils.general import os, Path

root = Path(os.path.dirname(__file__))
dir = root / "../../datasets/VisDrone"
min_dir = root / "../../datasets/VisDrone-min"
min_dir.mkdir(parents=True, exist_ok=True)

data_list = ['VisDrone2019-DET-train', 'VisDrone2019-DET-val', 'VisDrone2019-DET-test-dev']
for x in data_list:
    (min_dir / x).mkdir(parents=True, exist_ok=True)
    (min_dir / x / "images").mkdir(parents=True, exist_ok=True)
    (min_dir / x / "labels").mkdir(parents=True, exist_ok=True)
    print(dir / x)
    file_list = []
    for file in os.listdir(dir / x / "labels"):
        file_list.append(file)
    count = ceil(len(file_list) / 10)
    random.shuffle(file_list)
    for f in file_list[0:count]:
        shutil.copyfile((dir / x / "labels" / f), (min_dir / x / "labels" / f))
        file_name, _ = os.path.splitext(f)
        file_name += ".jpg"
        shutil.copyfile((dir / x / "images" / file_name), (min_dir / x / "images" / file_name))
