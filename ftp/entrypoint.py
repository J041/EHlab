import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

root = "/srv/ftp"
user = os.getenv("FTP_USER", "student")
password = os.getenv("FTP_PASS", "training-only")

authorizer = DummyAuthorizer()
authorizer.add_anonymous(root, perm="elr")
authorizer.add_user(user, password, root, perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "Training FTP Service"
handler.passive_ports = range(30000, 30010)

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
