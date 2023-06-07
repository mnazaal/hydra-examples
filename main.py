import hydra
from hydra.utils import call


def train_debug(cfg):
    print(f"environment seed is {cfg.environment.seed}")
    print(f"cfg.optimization.utility={cfg.optimization.utility_function}.")
    print(f"type(cfg.optimization.utility)={type(cfg.optimization.utility_function)}.")
    utility = call(cfg.optimization.utility_function)
    print(f"call(cfg.optimization.utility)={utility}.")
    print(
        f"type(call(cfg.optimization.utility))={type(call(cfg.optimization.utility_function))}."
    )


@hydra.main(config_path="config", config_name="main", version_base="1.2")
def run(cfg):
    train_debug(cfg)


if __name__ == "__main__":
    run()
