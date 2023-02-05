import hydra

@hydra.main(config_path="conf", config_name='config_instantiate', version_base=None)
def my_app(cfg) -> None:
    print(hydra.utils.instantiate(cfg.model1))
    print(hydra.utils.instantiate(cfg.model2))
    print(hydra.utils.instantiate(cfg.model3))
    print(hydra.utils.call(cfg.scorer))

my_app()