from abc import ABC, abstractmethod

class GreetingProvider(ABC):
    @abstractmethod
    def get_greeting(self, name):
        pass

class RussianGreetingProvider(GreetingProvider):
    def get_greeting(self, name):
        return f"Привет, {name}!"

class EnglishGreetingProvider(GreetingProvider):
    def get_greeting(self, name):
        return f"Hello, {name}!"

class GreetingExecutor(ABC):
    @abstractmethod
    def greet_using_provider(self, provider):
        pass

class ConsoleGreetingExecutor(GreetingExecutor):
    def greet_using_provider(self, provider, name):
        print(provider.get_greeting(name))

provider = EnglishGreetingProvider()
executor = ConsoleGreetingExecutor()

executor.greet_using_provider(provider, "world")
