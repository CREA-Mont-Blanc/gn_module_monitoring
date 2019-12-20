import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent


def gnmodule_install_app(gn_db, gn_app):
    """
        Fonction principale permettant de réaliser les opérations d'installation du module
    """
    with gn_app.app_context():
        # To run a SQL script use the gn_db parameter
        #gn_db.session.execute(open(str(ROOT_DIR / "data/data.sql"), "r").read())
        #gn_db.session.commit()
        # Install frontend
        gn_db.session.execute(open(str(ROOT_DIR / "data/schema_suivi_generique.sql"), "r").read())
        gn_db.session.commit()

        subprocess.call(["npm install"], cwd=str(ROOT_DIR / "frontend"), shell=True)
