from Circle import Circle
from Rectangle import Rectangle
from trinagle import trinagle

def main():
    s1=Circle(5)
    s2=Rectangle(3,4)
    s3=trinagle(8,10)

    s1.draw()
    s2.draw()
    s3.draw()

if __name__ =="__main__":
    main()