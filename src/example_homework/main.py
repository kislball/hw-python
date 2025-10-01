from abc import ABC, abstractmethod

# Класс GreetingProvider является интерфейсом для различных провайдеров строк приветствия.
# Чаще всего используется для поддержки мультиязычности, различных уровней вежиловсти и т.д.
class GreetingProvider(ABC):
    @abstractmethod
    # get_greeting возвращает приветствие для имени name.
    def get_greeting(self, name):
        pass

# Реализация GreetingProvider для русского языка
class RussianGreetingProvider(GreetingProvider):
    def get_greeting(self, name):
        return f"Привет, {name}!"

# Реализация GreetingProvider для английского языка
class EnglishGreetingProvider(GreetingProvider):
    def get_greeting(self, name):
        return f"Hello, {name}!"

# Интерфейс для различных исполнителей приветствий. Например ConsoleGreetingExecutor.
# Также возможна реализация иных каналов связи, например голосовой(условный VoiceGreetingExecutor) и пр.
class GreetingExecutor(ABC):
    @abstractmethod
    # Исполняет приветствия, предоставляемое GreetingProvider.
    def greet_using_provider(self, provider, name):
        pass

# Реализация GreetingExecutor для stdio.
class ConsoleGreetingExecutor(GreetingExecutor):
    def greet_using_provider(self, provider, name):
        print(provider.get_greeting(name))

provider = EnglishGreetingProvider()
executor = ConsoleGreetingExecutor()

executor.greet_using_provider(provider, "world")
