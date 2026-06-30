class Circle:
    radius = 0

    def get_area(self, radius):
        number_pi = 3.14
        radius_squared = radius ** 2

        circle_area = number_pi * radius_squared
        return print(circle_area)


my_circle = Circle()
my_circle.radius = float(input("Enter the radius: "))
my_circle.get_area(float(my_circle.radius))
