# Factory Pattern

{% hint style="info" %}
Source: [https://refactoring.guru/design-patterns/abstract-factory](abstractfactory.md#structure)
{% endhint %}

**Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### Structure <a href="#structure" id="structure"></a>

1. The **Abstract Factory** interface declares a set of methods for creating each of the abstract products.
2. **Concrete Factories** implement the creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.
3. **Abstract Products** declare interfaces for a set of distinct but related products that make up a product family.
4. **Concrete Products** are various implementations of abstract products, grouped by variants. Each abstract product (chair/sofa) must be implemented in all given variants (Victorian/Modern).
5. **Client:** Although concrete factories instantiate concrete products, signatures of their creation methods must return corresponding _abstract_ products. This way the client code that uses a factory doesn’t get coupled to the specific variant of the product it gets from a factory. The **Client** can work with any concrete factory/product variant, as long as it communicates with their objects via abstract interfaces.

### Code Example

```python
class GUIToolkitFactory(ABC):
    """
    The Abstract Factory interface for creating GUI elements.
    It declares methods for creating different types of GUI components.
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsGUIToolkitFactory(GUIToolkitFactory):
    """
    Concrete Factory for creating Windows-specific GUI components.
    Ensures that the created components are compatible with the Windows OS.
    """

    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSGUIToolkitFactory(GUIToolkitFactory):
    """
    Concrete Factory for creating MacOS-specific GUI components.
    Ensures that the created components are compatible with the macOS.
    """

    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


class Button(ABC):
    """
    Abstract Button interface for all button components.
    All button variants must implement this interface.
    """

    @abstractmethod
    def click(self) -> str:
        pass


"""
Concrete button implementations for Windows and MacOS.
"""


class WindowsButton(Button):
    def click(self) -> str:
        return "You have clicked a Windows button."


class MacOSButton(Button):
    def click(self) -> str:
        return "You have clicked a MacOS button."


class Checkbox(ABC):
    """
    Abstract Checkbox interface for all checkbox components.
    All checkbox variants must implement this interface.
    """

    @abstractmethod
    def check(self) -> str:
        pass

    @abstractmethod
    def toggle_with_button(self, button: Button) -> str:
        """
        Allows the checkbox to interact with a button.
        """
        pass


class WindowsCheckbox(Checkbox):
    def check(self) -> str:
        return "Windows checkbox is checked."

    def toggle_with_button(self, button: Button) -> str:
        result = button.click()
        return f"Windows checkbox toggled with ({result})"


class MacOSCheckbox(Checkbox):
    def check(self) -> str:
        return "MacOS checkbox is checked."

    def toggle_with_button(self, button: Button) -> str:
        result = button.click()
        return f"MacOS checkbox toggled with ({result})"


def client_code(factory: GUIToolkitFactory) -> None:
    """
    The client code works with factories and GUI components only through abstract types:
    GUIToolkitFactory, Button, and Checkbox. This allows any factory or product subclass
    to be passed to the client code without breaking it.
    """
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(f"{checkbox.check()}")
    print(f"{checkbox.toggle_with_button(button)}")


if __name__ == "__main__":
    print("Client: Testing client code with the Windows GUI toolkit:")
    client_code(WindowsGUIToolkitFactory())

    print("\n")

    print("Client: Testing the same client code with the MacOS GUI toolkit:")
    client_code(MacOSGUIToolkitFactory())
```

### Use cases

* Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.
* The Abstract Factory provides you with an interface for creating objects from each class of the product family. As long as your code creates objects via this interface, you don’t have to worry about creating the wrong variant of a product that doesn’t match the products already created by your app.

### &#x20;How to Implement <a href="#checklist" id="checklist"></a>

1. Map out a matrix of distinct product types versus variants of these products.
2. Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.
3. Declare the abstract factory interface with a set of creation methods for all abstract products.
4. Implement a set of concrete factory classes, one for each product variant.
5. Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.
6. Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.

### Pros and Cons <a href="#pros-cons" id="pros-cons"></a>

**Pros:**

1. You can be sure that the products you’re getting from a factory are compatible with each other.
2. You avoid tight coupling between concrete products and client code.
3. _**Single Responsibility Principle**_. You can extract the product creation code into one place, making the code easier to support.
4. _**Open/Closed Principle**_**.** You can introduce new variants of products without breaking existing client code.

**Cons:**  The code may become more complicated than it should be since a lot of new interfaces and classes are introduced along with the pattern.

