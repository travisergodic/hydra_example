from dataclasses import dataclass

@dataclass
class Dataset:
    name: str
    path: str

@dataclass
class Optim:
    name: str

@dataclass
class MyConfig:
    dataset: Dataset
    optim: Optim