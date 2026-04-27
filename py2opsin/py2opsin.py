import os
import subprocess
import sys
import warnings
from difflib import get_close_matches
from typing import Union

try:
    # python < 3.8
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

try:
    # python < 3.9
    from importlib.resources import files

    pkg_fopen = lambda fname: files("py2opsin") / fname
except ImportError:
    from pkg_resources import resource_filename

    pkg_fopen = lambda fname: resource_filename(__name__, fname)

# check if java is installed
try:
    result = subprocess.run(
        ["java", "-version"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
except Exception as e:
    warnings.warn(
        "Java may not be installed/accessible (java -version raised exception). "
        "Java 8 or newer is required to use py2opsin. Original Error:\n" + repr(e),
        category=RuntimeWarning,
    )


def py2opsin(
    chemical_name: Union[str, list],
    output_format: Literal[
        "SMILES",
        "ExtendedSMILES",
        "CML",
        "InChI",
        "StdInChI",
        "StdInChIKey",
    ] = "SMILES",
    allow_acid: bool = False,
    allow_radicals: bool = False,
    allow_bad_stereo: bool = False,
    wildcard_radicals: bool = False,
    jar_fpath: str = "default",
    tmp_fpath: str = "py2opsin_temp_input.txt",
) -> str:
    """Simple passthrough to opsin, returning results as Python strings.

    Args:
        chemical_name (str, list): IUPAC name of chemical as string, or list of strings.
        output_format (str, optional): One of "SMILES", "ExtendedSMILES", "CML", "InChI", "StdInChI", or "StdInChIKey".
                                        Defaults to "SMILES".
        allow_acid (bool, optional): Allow interpretation of acids. Defaults to False.
        allow_radicals (bool, optional): Enable radical interpretation. Defaults to False.
        allow_bad_stereo (bool, optional): Allow OPSIN to ignore uninterpreatable stereochem. Defaults to False.
        wildcard_radicals (bool, optional): Output radicals as wildcards. Defaults to False.
        jar_fpath (str, optional): Filepath to OPSIN jar file. Defaults to "default", which causes py2opsin to use its included jar.
        tmp_fpath (str, optional): Name for temporary file used for calling OPSIN. Defaults to "py2opsin_temp_input.txt".
                                   When multiprocessing, set this to a unique name for each process.

    Returns:
        str: Species in requested format, or False if not found or an error ocurred. List of strings if input is list.
    """
    # path to OPSIN jar
    pass
