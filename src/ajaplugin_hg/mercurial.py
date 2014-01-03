import logging
import subprocess
import shlex

from aja.vcs.base import VcsBase


class Mercurial(VcsBase):
    """Aja Mercurial support."""

    def pull(self, repository_uri):
        logging.info("Pulling repository {uri}.".format(uri=repository_uri))
        cmd = "hg clone {uri}".format(uri=repository_uri)
        self.run(cmd)

    def update(self):
        logging.info("Updating repository {path}".format(path=repository))
        cmd = "hg pull; hg update"
        self.run(cmd)

    def run(self, cmd):
        try:
            subprocess.check_call(shlex.split(cmd))
        except subprocess.CalledProcessError as e:
            logging.error(str(e))
