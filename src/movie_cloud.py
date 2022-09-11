import shutil
from os import path

import jieba
import pandas as pd
import stylecloud
from IPython.display import Image

from config.config_reader import cloudConfig


def generate_cloud_map(subject, icon):
    project_path = path.dirname(path.dirname(__file__))
    df = pd.read_csv(f"{project_path}/csv/comment-{subject}.csv", index_col=0)
    cts_list = df["comments"].values.tolist()
    cts_str = "".join([str(i).replace("\n", "").replace(" ", "") for i in cts_list])
    stop_words = []
    with open(f"{project_path}/static/stop_words.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    # jieba 分词
    word_list = jieba.cut(cts_str)
    words = []
    for word in word_list:
        if word not in stop_words:
            words.append(word)
    cts_str = "，".join(words)
    print(cts_str)

    # 如果icon_name找不到，报错：TypeError: 'NoneType' object is not subscriptable
    icon_name = f"fas fa-{icon}"
    file_name = f"{icon}-{subject}.png"
    file_path = f"{project_path}/picture/"
    stylecloud.gen_stylecloud(
        text=cts_str,
        max_words=300,
        collocations=False,
        font_path=f"{project_path}/static/SIMLI.TTF",
        # fa-arrow-circle-right,fa-user-graduate,fa-bone,fa-apple-alt
        icon_name=icon_name,
        size=800,
        output_name=file_name,
    )
    # 若dst是file_path+file_name则会覆盖，而file_path则不会覆盖
    shutil.move(src=file_name, dst=file_path + file_name)
    Image(filename=file_path + file_name)


if __name__ == "__main__":
    generate_cloud_map(subject=cloudConfig.subject, icon=cloudConfig.icon_name)
