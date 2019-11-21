import os


class Config:
    SECRET_KEY = 'my_secret_key'
    DEBUG = True


class TestConfig(Config):
    SECRET_KEY = 'test_secret_key'
    DEBUG = True


class ProdConfig(Config):
    SECRET_KEY = 'prod_secret_key'
    DEBUG = False


def run_config():
    env = os.environ.get("ENV")
    dict_config = {"TEST": TestConfig,
                   "PROD": ProdConfig,
                   "": Config}
    return dict_config.get(env)

