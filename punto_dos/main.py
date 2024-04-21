import paquete.shape as shape

def main():

    try:
        is_regular_square = True
        vertices_square = [shape.Point(0,0), shape.Point(7,0), shape.Point(7,7), shape.Point(0,7)]
        edges_square = [shape.Line(shape.Point(0,0), shape.Point(7,0)), shape.Line(shape.Point(7,0), shape.Point(7,7)), shape.Line(shape.Point(7,0), shape.Point(0,7)), shape.Line(shape.Point(0,7), shape.Point(0,0))]
        square = shape.Square(is_regular_square, vertices_square, edges_square)
        print(square.compute_area())
        print(square.compute_perimeter())
        print(square.compute_inner_angles())

        is_regular_triangle = False
        vertices_triangle = [shape.Point(-1, 0), shape.Point(2,9), shape.Point(4,1)]
        edges_triangle = [shape.Line(shape.Point(-1, 0), shape.Point(4,1)), shape.Line(shape.Point(4,1), shape.Point(2,9)), shape.Line(shape.Point(2,9), shape.Point(-1,0))]
        triangle = shape.Scalene(is_regular_triangle, vertices_triangle, edges_triangle)
        print(triangle.compute_area())
        print(triangle.compute_perimeter())
        print(triangle.compute_inner_angles())
        
        is_regular_rectangle = False
        vertices_rectangle = [shape.Point(-3,-5), shape.Point(-3,-2), shape.Point(5,-2),shape.Point(5,-5)]
        edges_rectangle = [shape.Line(shape.Point(-3,-2), shape.Point(-3,-5)), shape.Line(shape.Point(-3,-5), shape.Point(5,-5)), shape.Line(shape.Point(5,-5), shape.Point(5,-2)), shape.Line(shape.Point(5,-2), shape.Point(-3,-2))]
        rectangle = shape.Rectangle(is_regular_rectangle, vertices_rectangle, edges_rectangle)
        print(rectangle.compute_area())
        print(rectangle.compute_perimeter())
        print(rectangle.compute_inner_angles())
    except TypeError as error:
        print("Error: " + str(error))
    except ValueError as error:
        print("Error: " + str(error))

if __name__=="__main__":
    main()