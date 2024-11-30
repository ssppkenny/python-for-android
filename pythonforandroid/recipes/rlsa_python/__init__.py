
from pythonforandroid.recipe import PythonRecipe


class RlsaPythonRecipe(PythonRecipe):
    version = '0.0.1'
    url = 'https://github.com/ssppkenny/rlsa_python/archive/refs/tags/{version}.tar.gz'

    depends = ['setuptools', 'numpy']

    call_hostpython_via_targetpython = False


recipe = RlsaPythonRecipe()
