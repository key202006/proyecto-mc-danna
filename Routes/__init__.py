from .aprendiz_bp import apr_bp
from .curso_bp import cur_bp
from .evaluacion_bp import eva_bp
from .imparte_bp import imp_bp
from .instructor_bp import inst_bp
from .matricula_bp import mat_bp
from .mat_eva_bp import mateva_bp
from .persona_bp import per_bp
from .documentacion import documentacion_bp


def loadRouters(app):
    app.register_blueprint(apr_bp, url_prefix='/aprendices')
    app.register_blueprint(cur_bp, url_prefix='/cursos')
    app.register_blueprint(eva_bp, url_prefix='/evaluaciones')
    app.register_blueprint(imp_bp, url_prefix='/impartes')
    app.register_blueprint(inst_bp, url_prefix='/instructores')
    app.register_blueprint(mat_bp, url_prefix='/matriculas')
    app.register_blueprint(mateva_bp, url_prefix='/mat_evas')
    app.register_blueprint(per_bp, url_prefix='/personas')
    app.register_blueprint(documentacion_bp,url_prefix='/documentacion')