from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class RlsaRecipe(CompiledComponentsPythonRecipe):
    """This is a two-in-one recipe:
      - build labraru `libprotobuf.so`
      - build and install python binding for protobuf_cpp
    """
    name = 'rlsa'
    version = '0.0.2'
    url = 'https://github.com/ssppkenny/rlsa/archive/refs/tags/{version}.tar.gz'
    call_hostpython_via_targetpython = False
    depends = ['numpy', 'setuptools']
    site_packages_name = 'rlsa'

recipe = RlsaRecipe()
