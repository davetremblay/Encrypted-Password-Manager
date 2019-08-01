# Encrypted Password Manager

EPM is a code that lets you create, edit, delete, search, and view passwords and their related information (website, nickname).
The information is encrypted in a file on your hard drive and you must use a meta-password to access them. That's the only password
you'll need to remember. If you forget it, your file will be unusable. The unprotected text file is cleared and deleted automatically.
That's the only password you'll need to remember. If you don't
have a password manager, this is a good option. If you already do, make sure you trust the company owning it.

## Getting Started

Clone the project and run it using Python.

### Prerequisites

You need to install ast and pyAesCrypt.

```
pip install ast

pip install pyAesCrypt
```

### Example Scenarios

1: You want to add a new entry with a randomly generated password.

```
$ python epm.py
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: a
Enter password manually? (y/n): n
Identifier (unique value): example_1
Website name or url: website.com
Nickname / Email address: nick@name.com
Desired password length: 7
Strength
1: Uppercase
2: 1 + lowercase
3: 2 + numbers
4: 3 + special characters

Desired password strength (1-4): 4
Entry created!
Identifier (unique value): example_1
Website name or url: website.com
Nickname or email address: nick@name.com
Password: Rn4R4;I
Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): ******
Enter new main password again: ******
Clearing and deleting password_list.txt...
password_list.txt cleared and deleted.
```

1.5: You want to add a new entry with a manual password.

```
$ python epm.py
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: a
Decrypting file...
Enter main password to access encrypted passwords: ******
Enter password manually? (y/n): y
Identifier (unique value): example_2
Website name or url: internet.com
Nickname / Email address: nick@name.com
Enter password manually: password1234
Entry created!
Identifier (unique value): example_2
Website name or url: internet.com
Nickname or email address: nick@name.com
Password: password1234
Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): ******
Enter new main password again: ******
Clearing and deleting password_list.txt...
password_list.txt cleared and deleted.
```

2: You want to edit an entry.

```
$ python epm.py
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: e
What do you want to edit?
(W)ebsite name or url
(N)ickname or Email address
(P)assword

Edit: p
Decrypting file...
Enter main password to access encrypted passwords: ******
Enter password manually? (y/n): n
Identifier of what you want to edit: example_2
Desired new password length: 7
Strength
1: Uppercase
2: 1 + lowercase
3: 2 + numbers
4: 3 + special characters

Desired new password strength (1-4): 4
Password edited!
Identifier (unique value): example_2
Website name or url: internet.com
Nickname or email address: nick@name.com
Password: BiN@GH)
Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): ******
Enter new main password again: ******
Clearing and deleting password_list.txt...
password_list.txt cleared and deleted.
```

3: You want to search for an entry.

```
$ python epm.py
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: s
Decrypting file...
Enter main password to access encrypted passwords: ******
Identifier of what you want to search: example_2
Website name or url: internet.com
Nickname or email address: nick@name.com
Password: BiN@GH)
Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): ******
Enter new main password again: ******
Clearing and deleting password_list.txt...
password_list.txt cleared and deleted.
```

4: You want to view all entries.

```
$ python epm.py
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: v
Decrypting file...
Enter main password to access encrypted passwords: ******

'Identifier': ['Website', 'Nickname', 'Password']

'example_1': ['website.com', 'nick@name.com', 'Rn4R4;I']
'example_2': ['internet.com', 'nick@name.com', 'BiN@GH)']


Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): ******
Enter new main password again: ******
Clearing and deleting password_list.txt...
password_list.txt cleared and deleted.
```

5. You want to delete an entry.

```
$ python epm.py
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: d
Decrypting file...
Enter main password to access encrypted passwords: ******
Identifier of what you want to delete: example_1
Entry deleted!
Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): ******
Enter new main password again: ******
Clearing and deleting password_list.txt...
password_list.txt cleared and deleted.
```

## Author

* **Dave Trembay** - *Initial work* - [davetremblay](https://github.com/davetremblay)

## License

This project is licensed under the MIT License, see the [LICENSE.MD](LICENSE.MD) file for details.

## Acknowledgements

* Thanks to all those who report bugs and issues and help improve this project.
