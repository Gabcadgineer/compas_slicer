import logging

from compas.geometry import Point

logger = logging.getLogger('logger')

__all__ = ['spiralize_contours']


def spiralize_contours(slicer):
    """Spiralizes contours. Only supports a constant layer height.
    Most useful for single contoured geometries (vases).

    Parameters
    ----------
    slicer : compas_slicer.slicers.PlanarSlicer
        An instance of the compas_slicer.slicers.PlanarSlicer class.
    layer_height : float
        Layer height used for slicing. 
    xx : xx
        xx
    """
    # retrieves layer height by subtracting z of first point of layer 1 from layer 0
    layer_height = slicer.layers[1].paths[0].points[0][2] - slicer.layers[0].paths[0].points[0][2]
    
    for layer in slicer.layers:
        if len(layer.paths) == 1:
            for path in layer.paths:
                for i, point in enumerate(path.points):
                    # get the number of points in a layer
                    no_of_points = len(path.points)
                    # calculates distance to move
                    distance_to_move = layer_height / no_of_points

                    path.points[i] = Point(point[0], point[1], point[2] + (i*distance_to_move))

        else:
            logger.warning("Spiralize contours only works for layers consisting out of a single path, contours were not changed, spiralize contour skipped")
            break
    

if __name__ == "__main__":
    pass
