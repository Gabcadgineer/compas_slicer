from compas.geometry import Point
from compas_slicer.geometry import PrintPoint

__all__ = ['generate_z_hop']

def generate_z_hop(printpoints_dict, z_hop=10):
    """Generates a z-hop between print paths.
    To generate the z-hop it creates a point above every start- and end-point of a path.

    Parameters
    ----------
    printpoints_dict : dictionary
        The PrintPoints as a dictionary.
    z_hop : float
        The value (in mm) to use for the z-hop generation.
    """
    
    for layer_key in printpoints_dict:
        for path_key in printpoints_dict[layer_key]:
            path_printpoints = printpoints_dict[layer_key][path_key]

            pt0 = path_printpoints[0].pt

            z_hop_printpoint = PrintPoint(pt=Point(pt0[0], pt0[1], pt0[2] + z_hop),
                                          layer_height=path_printpoints[0].layer_height)
            z_hop_printpoint.extruder_toggle = False

            # insert on list the new printpoint
            printpoints_dict[layer_key][path_key].insert(0, z_hop_printpoint)


if __name__ == "__main__":
    pass
