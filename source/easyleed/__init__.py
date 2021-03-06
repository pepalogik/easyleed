"""
The EasyLEED package is divided into several subpackages:

- base: Core functionality (fitting procedures, Tracker class, etc.)
- kalman: Implementation of Kalman filter classes
- io: Input/Output functionality (reading FITS, PIL, and IMG files)
- gui: Graphical User Interface

.. automodule:: easyleed.base
    :members:

.. automodule:: easyleed.kalman
    :members:

.. automodule:: easyleed.io
    :members:

.. automodule:: easyleed.gui
    :members:

"""

__version__ = "2.3.3"
__author__ = "Andreas Mayer, Hanna Salopaasi, Nicola Ferralis"

# import packages
# order of loading is important and should not be changed
import sys
sys.path.append('.')
try:
    import config
except:
    sys.path.append('..')
    try:
        import config
    except:
        from . import defaultconfig as config

import logging
logging.basicConfig(filename=config.loggingFilename, level=config.loggingLevel)
logger = logging.getLogger()

from . import kalman
from . import io
from . import base
from . import test
from . import qt
from . import gui
