# import Flask Script object
from flask_script import Manager, Server
import main
import models
import users
import articles

# Init manager object via app object
manager = Manager(main.app)

# Create some new commands
manager.add_command("server", Server())

models.db.create_all()

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app, db=models.db)

if __name__ == '__main__':
    manager.run()