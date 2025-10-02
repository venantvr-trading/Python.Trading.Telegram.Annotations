# Python Trading Telegram Annotations

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern Python library for creating Telegram bots with an annotation and decorator-based command system.

## 🚀 Features

- ✅ Asynchronous message handling with threads
- ✅ Decorator-based command system
- ✅ Interactive menu support (inline keyboards)
- ✅ Multi-step prompt handling
- ✅ Extensible architecture with custom handlers
- ✅ Structured logging and robust error handling
- ✅ HTTP session with automatic retry
- ✅ Complete type hints for better DX

## 📦 Installation

### Standard Installation

```bash
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
pre-commit install
```

## 🛠️ Configuration

Create a `.env` file at the project root:

```env
BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
LOG_LEVEL=INFO  # Optional: DEBUG, INFO, WARNING, ERROR
```

## 🎯 Usage

### Simple Example

```python
from python_trading_telegram_annotations.bot import TelegramBot
from python_trading_telegram_annotations.handler import TelegramHandler
from python_trading_telegram_annotations.decorators import command


# noinspection PyUnresolvedReferences
class MySimpleHandler(TelegramHandler):
    @command(name="/menu", description="Display help menu", menu="/menu")
    def menu(self) -> dict:
        text_response = "Available commands:\n"
        for cmd_name, cmd_details in COMMAND_REGISTRY.items():
            description = cmd_details.get("description", "No description.")
            text_response += f"\n• `{cmd_name}` : {description}"
        return {"text": text_response, "parse_mode": "Markdown"}

    @command(
        name="/hello",
        description="Simple greeting without arguments",
        asks=[],
        kwargs_types={},
        menu="/menu"
    )
    def hello(self) -> dict:
        return {"text": "Hello! 👋"}

    @command(
        name="/greet",
        description="Personalized greeting with name and age",
        asks=[
            "What's your name?",
            "What's your age?"
        ],
        kwargs_types={
            "name": str,
            "age": int
        },
        menu="/menu"
    )
    def greet(self, name: str, age: int) -> dict:
        if age < 18:
            age_msg = "you're young!"
        else:
            age_msg = "you're an adult."
        return {"text": f"Hello, {name}! At {age} years old, {age_msg}"}


# Launch the bot
bot = TelegramBot(
    bot_token="YOUR_TOKEN",
    chat_id="YOUR_CHAT_ID",
    handlers=MySimpleHandler()
)
```

## 🧪 Tests

Run all tests:

```bash
make test
```

## 🔧 Development

### Useful Commands

```bash
make help        # Show all available commands
make format      # Format code with black and isort
make test        # Run tests
make check       # Run format and tests
make install     # Install dependencies
make update      # Update dependencies
make clean       # Clean up generated files
```

### Project Structure

```
.
├── src/
│   └── python_trading_telegram_annotations/
│       ├── __init__.py
│       ├── bot.py           # Main bot class
│       ├── handler.py       # Command handler
│       ├── decorators.py    # Command decorators
│       ├── config.py        # Configuration and logging
│       ├── protocols.py     # Protocol definitions
│       ├── classes/         # Types and enums
│       │   ├── __init__.py
│       │   ├── command.py
│       │   ├── menu.py
│       │   ├── types.py
│       │   └── enums.py
│       └── tools/           # Utility tools
│           └── logger.py    # Logging utilities
├── tests/                   # Unit tests
│   ├── test_bot.py
│   ├── test_handler.py
│   ├── main.py
│   └── handlers/           # Handler examples
│       ├── hello.py
│       └── bye.py
├── pyproject.toml          # Project configuration
├── Makefile                # Development commands
└── .pre-commit-config.yaml # Pre-commit hooks
```

## 📝 Code Conventions

- **Style**: Black (max line: 120 characters) + isort
- **Linting**: Ruff + Flake8 (in pre-commit)
- **Type checking**: Mypy with strict mode
- **Docstrings**: Google format
- **Tests**: Pytest
- **Pre-commit hooks**: Multiple quality checks including security (bandit), spell checking (codespell), and more

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Before Submitting

```bash
make check      # Run format and tests
pre-commit run --all-files  # Run all pre-commit hooks
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for inspiration
- The Telegram team for their excellent API

## 📮 Contact

- **Author**: venantvr
- **Email**: venantvr@gmail.com
- **GitHub**: [@venantvr](https://github.com/venantvr)