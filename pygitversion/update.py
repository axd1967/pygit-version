import argparse
import os
from subprocess import check_output


def update_file(filename, gitinfo):

    file_obj = open(filename, 'w')
    file_obj.write("""
# idea: https://packaging.python.org/guides/single-sourcing-package-version/
# note: this file is typically generated from script, and often versioned as template and to be ignored by Git

__version__ = "{}"
__branch__ = "{}" """.format(gitinfo.version, gitinfo.branch)
                   )

    file_obj.close()


class GitInfo:
    version = 'git describe --tags --dirty'
    branch = 'git rev-parse --abbrev-ref HEAD'

    def __init__(self):
        self.version = self._get_git_version()
        self.branch = self._get_branch_name()

    def _get_git_version(self):
        describe = check_output(self.version.split()).decode('utf-8').strip()
        return describe
        # self._extract_version_components(describe)

    def _get_branch_name(self):
        branchname = check_output(self.branch.split()).decode('utf-8').strip()
        return branchname

    def _extract_version_components(self, git_describe_string):
        """Split the output of ``git describe`` into elementary segments"""
        tag_dir = os.path.dirname(git_describe_string)  # XXX non-PEP-440
        full_tag = os.path.basename(git_describe_string)

        # split on '-': before=tag, after=steps-sha1-dirty etc
        full_tag += '-'*3    # in case segments are absent, to avoid array out of indexes
        segments = full_tag.split('-')

        tag = segments[0]
        steps = segments[1]
        sha1 = segments[2]
        dirty = segments[3]

        return tag_dir, tag, steps, sha1, dirty


def main():

    parser = argparse.ArgumentParser(
        description="Create/overwrite a file with version info.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('fname', metavar='filename', type=str, help='filename to pepper')

    args = parser.parse_args()

    gitinfo = GitInfo()
    update_file(args.fname, gitinfo)
