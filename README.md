## Introduction

This Repo is the official CUDA implementation of ICCV 2019 Oral paper for [CARAFE: Content-Aware ReAssembly of FEatures](https://arxiv.org/abs/1905.02188).

```
@inproceedings{Wang_2019_ICCV,
    title = {CARAFE: Content-Aware ReAssembly of FEatures},
    author = {Wang, Jiaqi and Chen, Kai and Xu, Rui and Liu, Ziwei and Loy, Chen Change and Lin, Dahua},
    booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
    month = {October},
    year = {2019}
}
```

## Setup CARAFE Operator

There are two ways to setup CARAFE operator.


A. Install mmcv which contains CARAFE.

CARAFE is supported in mmcv.
You may install mmcv following the official guideline.
```
https://github.com/open-mmlab/mmcv
```



B. Install CARAFE directly from GitHub.

Requirements:

```
CUDA >= 9.0, Pytorch >= 1.3, Python >= 3.6
```

Install with `pip`
```shell
pip install git+https://github.com/myownskyW7/CARAFE.git@master
```

Run gradient check to make sure the operator is successfully compiled
```
$ python

>>> from carafe import grad_check
```

C. Compile CARAFE from source.

Requirements:

```
CUDA >= 9.0, Pytorch >= 1.3, Python >= 3.6
```

Git clone this repo.
```shell
git clone https://github.com/myownskyW7/CARAFE
```

Setup CARAFE op.
```shell
cd CARAFE
python setup.py develop
# or "pip install -v -e ."
```

Run gradient check to make sure the operator is successfully compiled
```
$ python

>>> from carafe import grad_check
```

## Usage

```python
import torch
from mmcv.ops.carafe import CARAFEPack
# or "from carafe import CARAFEPack"


x = torch.rand(2, 40, 50, 70)
model = CARAFEPack(channels=40, scale_factor=2)

model = model.cuda()
x = x.cuda()

out = model(x)

print('original shape: ', x.shape)
print('upscaled shape: ', out.shape)
```

## Applications
Projects with CARAFE operators

[mmcv](https://github.com/open-mmlab/mmcv)

[mmdetection](https://github.com/open-mmlab/mmdetection)

[mmediting](https://github.com/open-mmlab/mmediting)
