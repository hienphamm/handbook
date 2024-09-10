# Liskov substitution principle

{% hint style="info" %}
**Definition:** _Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program._
{% endhint %}

In simple terms, the Liskov Substitution Principle states:

"If you have a class `Parent`, and another class `Child` extends or inherits from `Parent`, you should be able to use an object of `Child` wherever you use an object of `Parent`, without breaking the functionality of your program."\


#### Breaking it Down

Let's look at this in simpler parts:

1. **Inheritance**: In object-oriented programming, a class (like `Child`) can inherit from another class (like `Parent`). This means `Child` will have all the methods and properties of `Parent`, plus any additional ones it defines.
2. **Replaceability**: LSP says that wherever you use a `Parent` object, you should be able to replace it with a `Child` object. If replacing `Parent` with `Child` breaks the program or makes it behave incorrectly, then the `Child` class is not following LSP.

#### An Example to Illustrate

Imagine a program that uses a `Bird` class:

```python
class Bird:
    def fly(self):
        print("I can fly!")

class Penguin(Bird):
    def fly(self):
        print("I can't fly!")

```

According to the Liskov Substitution Principle, you should be able to replace any `Bird` object with a `Penguin` object without causing issues. However, a `Penguin` doesn't behave like most `Birds` because it cannot fly. This breaks the Liskov Substitution Principle since the `Penguin` class changes the expected behavior of the `fly` method.\
\
**Code example:**

```python
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)

```
