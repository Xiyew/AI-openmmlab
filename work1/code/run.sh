#!/bin/bash
# 加载模块
module load anaconda/2021.05
module load cuda/11.1
module load gcc/7.3

# 激活环境
source activate mmclassification

# 刷新⽇志缓存
export PYTHONUNBUFFERED=1

# 训练模型
python tools/train.py \
       configs/resnet18/resnet18_b16_flower.py \
       --work-dir work/resnet18_b16_flower

