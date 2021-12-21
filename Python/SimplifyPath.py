# https://codefights.com/interview/wqveBLtNtfByaEnfW
# TODO: Not complete
import re


def simplifyPath(path):
    '''
    Here is how this path was simplified:
    * /./ means "move to the current directory" and can be replaced with a single /;
    * /x/../ means "move into directory x and then return back to the parent directory", so it can replaced with a single /;
    * // means "move to the current directory" and can be replaced with a single /.
    '''
    if (path == '/'):
        return path

    if (path[0] != '/'):
        path = '/' + path

    while '.' in path:
        path = path.replace('/./', '/')
        path = path.replace('//', '/')
        path = re.sub(r'\/[a-z]*\/\.\.\/', '/', path)
        path = re.sub(r'\/[a-z]*\/\.\.', '/', path)
        path = re.sub(r'\/\.\.\/', '/', path)

    print(path)
    if (path == '/'):
        return path

    if (path[len(path) - 1] is '/'):
        path = path[:-1]

    print(path)
    return path


# simplifyPath("/a/b/c/../..")
# simplifyPath("home/a/./x/../b//c/")
# simplifyPath("/../")
simplifyPath("a/b/../c/d/../../e/../../")
