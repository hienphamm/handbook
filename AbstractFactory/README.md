# Factory Pattern

The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

## Key Concepts

1. **Factory Method**: This is a method in the creator class that returns new product objects. Subclasses usually override this method to change the resulting product's type.

2. **Product**: This is the common interface for all products. It declares the methods that all concrete products must implement.

3. **Concrete Products**: These are different implementations of the product interface.

4. **Creator**: This is a class that declares the factory method. The method returns new product objects. The creator may also provide a default implementation of the factory method.

5. **Concrete Creators**: These are classes that implement the factory method to create new products.

## Benefits

- It provides a simple way of creating objects without exposing the instantiation logic to the client.
- It provides a way to decouple the client code from concrete classes.
- It can provide a hook for subclasses to override object creation steps.

## Drawbacks

- The code may become more complicated since you need to introduce a lot of new subclasses which implement the factory method.

Remember, like any design pattern, the Factory Pattern should be used when it's beneficial and makes sense in the context of your project. It's not a one-size-fits-all solution.

[embedmd]:# (AbstractFactory/hello.go go)

