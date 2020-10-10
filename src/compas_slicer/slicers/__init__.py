"""
********************************************************************************
compas_slicer.slicers
********************************************************************************

Classes
=======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    BaseSlicer


BaseSlicer
----------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    PlanarSlicer
    CurvedSlicer
    
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import compas

from .base_slicer import *  # noqa: F401 E402 F403
from .planar_slicer import *
if not compas.IPY:
    from .curved_slicer import *
    from compas_slicer.slicers.planar_slice_functions.planar_slicing_meshcut import *  # noqa: F401 E402 F403
    from compas_slicer.slicers.planar_slice_functions.planar_slicing_numpy import *  # noqa: F401 E402 F403
    from compas_slicer.slicers.planar_slice_functions.planar_slicing_cgal import *  # noqa: F401 E402 F403
    from compas_slicer.slicers.planar_slice_functions.planar_slicing import *  # noqa: F401 E402 F403
    from compas_slicer.fabrication.print_process_utilities.generate_z_hop import *  # noqa: F401 E402 F403

__all__ = [name for name in dir() if not name.startswith('_')]
