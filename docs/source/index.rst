.. akahu-py documentation master file, created by
   sphinx-quickstart on Sun May 25 00:54:54 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

akahu-py documentation
======================

**akahu-py** is an unofficial Python client for the `Akahu API <https://developers.akahu.nz>`_.


Github: `jason-s13r/akahu-py <https://github.com/jason-s13r/akahu-py>`_.


Command
--------

.. click:: akahu.command:cli
   :prog: akahu-py

See :ref:`cli` for a full usage information.

.. toctree::
   :maxdepth: 3
   :caption: Usage
   :hidden:

   /cli

Python Client
-------------

Example usage:

.. code-block:: python

   from datetime import datetime, timedelta
   from akahu.client import Client
   # Initialize the client with your API key
   config = Client.Config('your_app_token', 'your_user_token')
   client = Client(config)
   
   me = client.me.get()
   print(f"Akahu user email: {me.email}")

   end = datetime.now()
   start = end - timedelta(days=7)

   accounts = client.accounts.list()
   for account in accounts:
      print(f"{account.name} ({account.formatted_account}): {account.balance.current} {account.balance.currency}")
      page = client.accounts.transactions(account.id).list(start, end)
      for transaction in page.items:
         print(f"   {transaction.amount} ({transaction.description})")
      else:
         if not page.size:
            print("    No transactions found.")



.. toctree::
   :maxdepth: 3
   :caption: API Reference
   :hidden:

   /akahu/client
   /akahu/models/user
   /akahu/models/transaction
   /akahu/models/payment
   /akahu/models/account
   /akahu/api/endpoints/pending_transactions
   /akahu/api/endpoints/me
   /akahu/api/endpoints/payments
   /akahu/api/endpoints/transfers
   /akahu/api/endpoints/accounts
   /akahu/api/endpoints/transactions
   /akahu/api/endpoints/refresh
   /akahu/command
   /akahu/cli/me
   /akahu/cli/transactions
   /akahu/cli/tokens
   /akahu/cli/utils
   /akahu/cli/account
   /akahu/api/rest/client
   /akahu/api/rest/models/api_error
   /akahu/api/rest/models/paged_response
   /akahu/api/rest/endpoint/list
   /akahu/api/rest/endpoint/getbyid
   /akahu/api/rest/endpoint/defaults
   /akahu/api/rest/endpoint/get
   /akahu/api/rest/base