import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf, DictConfig
from conf.config import Optim

cs = ConfigStore.instance()
# Registering the Config class with the name `postgresql` with the config group `db`
cs.store(name="optim", group="optim", node=Optim)

@hydra.main(config_path="conf")
def my_app(cfg: DictConfig) -> None:
    print(cfg)


if __name__ == "__main__":
    my_app()