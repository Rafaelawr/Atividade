from config import create_app
from controllers.atividade_controller import atividade_bp

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividade')

if __name__ == '_main_':
  app.run(host='localhost', port=5002) 