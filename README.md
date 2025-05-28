# akahu-py

**akahu-py** is an unofficial Python client for the [Akahu API](https://developers.akahu.nz).

## TODO

- a lot, probably.
- [ ] tests
- [ ] support more endpoints
- [ ] eg, make payments and transfers
- [ ] support full app tokens
- [ ] more cli commands
- [ ] pypi, homebrew, etc.
- [ ] loose interest in a week, probably.

## Installation

TODO.
Clone the project, then use `uv run akahu-py` to interact with the cli commands.

## Usage

### Command line

```
> uv run akahi-py
Usage: akahu-py [OPTIONS] COMMAND [ARGS]...

  Akahu CLI.

Options:
  --help  Show this message and exit.

Commands:
  account       Account commands.
  me            Get current user.
  tokens
  transactions  Transaction commands.
```

show current user info:
```
> $ uv run akahu-py me
╒══════════════════╤════════════════╤═════════════════════╤════════╤════════════╤═══════════╤════════════════════════════════╕
│ Email            │ Preferred Name │ Access Granted At   │ Mobile │ First Name │ Last Name │ ID                             │
╞══════════════════╪════════════════╪═════════════════════╪════════╪════════════╪═══════════╪════════════════════════════════╡
│ user@example.com │ User           │ 2025-05-21 03:29:31 │        │            │           │ user_xxxxxxxxxxxxxxxxxxxxxxxxx │
╘══════════════════╧════════════════╧═════════════════════╧════════╧════════════╧═══════════╧════════════════════════════════╛
```

list accounts, with filtered by currency:
```
> $ uv run akahu-py account list --currency AUD
╒══════════╤═══════════════════╤═════════╤════════════════╤══════════╤═════════╤═══════════╕
│ Provider │ Name              │ Type    │ Account Number │ Currency │ Current │ Available │
╞══════════╪═══════════════════╪═════════╪════════════════╪══════════╪═════════╪═══════════╡
│ Wise     │ User AUD Balance  │ FOREIGN │                │ AUD      │ 1000.00 │ 1000.00   │
├──────────┼───────────────────┼─────────┼────────────────┼──────────┼─────────┼───────────┤
│          │                   │         │ Total          │ AUD      │ 1000.00 │ 1000.00   │
╘══════════╧═══════════════════╧═════════╧════════════════╧══════════╧═════════╧═══════════╛
```

### Python

```python
from akahu.client import Client

config = Client.Config(app_token, user_token)
api = Client(config)
accounts = api.accounts.list()
for account in accounts:
    print(account.name, account.balance.current)
```

## Documentation

https://akahu-py.readthedocs.io/

## Contributing

Contributions are welcome! Please open issues or pull requests.

## License

Public domain, or unlicense, or CC0... I don't care.