import hydra
from hydra.core.hydra_config import HydraConfig
from hydra.core.config_store import ConfigStore

from conf.config import MyConfig

cs = ConfigStore.instance()
cs.store(name='my_config', node=MyConfig)

@hydra.main(config_path="conf", config_name="config.yaml")
def main(cfg: MyConfig): 
    print(cfg)
    print(hydra.utils.get_original_cwd())
    print(cfg.model.path)


if __name__ == '__main__': 
    main()



