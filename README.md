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

## Setup CARAFE
Requirements:

CUDA >= 9.0, Pytorch >= 1.3

Use CARAFE in your own project.

Git clone this repo.
```shell
git clone https://github.com/myownskyW7/CARAFE
```

Setup CARAFE in your own project.
```shell
cp -r ./CARAFE $Your_Project_Path$
cd $Your_Project_Path$/CARAFE
python setup.py develop
# or "pip install -v -e ."
```
Run gradient check to make sure the operator is successfully compiled
```
python grad_check.py
```

## Applications
Other projects contain CARAFE operators

[mmcv](https://github.com/open-mmlab/mmcv)

[mmediting](https://github.com/open-mmlab/mmediting)

[mmdetection](https://github.com/open-mmlab/mmdetection)
