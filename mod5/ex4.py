import sys
import traceback


class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        if self.stdout is not None:
            sys.stdout, self.stdout = self.stdout, sys.stdout
        if self.stderr is not None:
            sys.stderr, self.stderr = self.stderr, sys.stderr
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr.write(traceback.format_exc())
        if self.stderr is not None:
            sys.stderr, self.stderr = self.stderr, sys.stderr
            self.stderr.close()
        if self.stdout is not None:
            sys.stdout, self.stdout = self.stdout, sys.stdout
            self.stdout.close()
        return True
