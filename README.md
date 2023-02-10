# Welcome to AI-Album Notebooks

## Dependencies

Initialise all the submodules.

```bash
$ git submodule init
```

Install the python dependencies.

```bash
$ pip install "fastapi[all]"
$ pip install pymongo
$ pip install pydantic-mongo
$ pip install jsons
$ pip ninstall pyyaml
$ pip install networkx
$ mamba install pytorch torchvision cudnn torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
$ pip install cryptography==38.0.4
```

### Building DLIB library

```bash
./build.sh
```