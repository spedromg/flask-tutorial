import os
from flask import Flask

def create_app(test_config=None):
    # cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # carrega a instância config, se existir, quando não testar
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carrega o test do config se passar
        app.config.from_mapping(test_config)

    # verifique se a pasta da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # uma página simples que mostra hello
    @app.route("/hello")
    def hello():
        return 'Hello, World!'

    return app