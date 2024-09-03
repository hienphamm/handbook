from __future__ import annotations
from abc import ABC, abstractmethod


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
