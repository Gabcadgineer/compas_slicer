import logging
from copy import deepcopy

logger = logging.getLogger('logger')

__all__ = ['smooth_printpoint_attribute',
           'smooth_printpoints_up_vectors',
           'smooth_printpoints_layer_heights']


def smooth_printpoint_attribute(print_organizer, iterations, strength, get_attr_value, set_attr_value):
    """
    Iterative smoothing of the printpoints attribute.
    The attribute is accessed using the function get_attr_value(ppt), and is
    set using the function set_attr_value(ppt, v).
    All attributes are smoothened continuously (i.e. as if their printpoints belong into one long uninterrupted path)
    For examples of how to use this function look at 'smooth_printpoints_layer_heights' and
    'smooth_printpoints_up_vectors' below.
    TODO: add interrupted smoothing, where the ppt.extrusion_toggle is taken into consideration.

    Parameters
    ----------
    print_organizer: :class: 'compas_slicer.print_organization.BasePrintOrganizer', or other class inheriting from it.
    iterations: int, smoothing iterations
    strength: float
    get_attr_value: function that returns an attribute of a printpoint, get_attr_value(ppt)
    set_attr_value: function that sets an attribute of a printpoint, set_attr_value(ppt, new_value)
    """

    # first smoothen the values
    attrs = []
    for ppt in print_organizer.printpoints_iterator():
        assert get_attr_value(ppt), 'The attribute you are trying to smooth has not been assigned a value'

    for iteration in range(iterations):
        attrs = [get_attr_value(ppt) for ppt in print_organizer.printpoints_iterator()]
        new_values = deepcopy(attrs)

        for i, ppt in enumerate(print_organizer.printpoints_iterator()):
            if 0 < i < len(attrs) - 1:  # ignore first and last element
                mid = (attrs[i - 1] + attrs[i + 1]) * 0.5
                new_values[i] = mid * strength + attrs[i] * (1 - strength)
        attrs = new_values

        # in the end assign the new (smoothened) values to the printpoints
        if iteration == iterations-1:
            for i, ppt in enumerate(print_organizer.printpoints_iterator()):
                set_attr_value(ppt, attrs[i])


def smooth_printpoints_layer_heights(print_organizer, iterations, strength):
    """ This function is an example for how the 'smooth_printpoint_attribute' function can be used. """
    def get_ppt_layer_height(ppt): return ppt.layer_height
    def set_ppt_layer_height(ppt, v): ppt.layer_height = v
    smooth_printpoint_attribute(print_organizer, iterations, strength, get_ppt_layer_height, set_ppt_layer_height)


def smooth_printpoints_up_vectors(print_organizer, iterations, strength):
    """ This function is an example for how the 'smooth_printpoint_attribute' function can be used. """
    def get_ppt_up_vec(ppt): return ppt.up_vector
    def set_ppt_up_vec(ppt, v): ppt.up_vector = v
    smooth_printpoint_attribute(print_organizer, iterations, strength, get_ppt_up_vec, set_ppt_up_vec)
