# Encrypted Password Manager

EPM is a code that lets you create, edit, delete, search, and view passwords and their related information (website, nickname).
The information is encrypted in a file on your hard drive and you must use a meta-password to access them. That's the only password
you'll need to remember. If you forget it, your file will be unusable. The unprotected text file is sent to trash automatically, but 
for better security you need to delete it manually, or empty your trash. That's the only password you'll need to remember. If you don't 
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

1: You want to add a new entry.

```
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: a

Identifier (unique value): identifier

Website name or url: website.com

Nickname / Email address: nick@name.com

Desired password length: 8

Strength
1: Uppercase
2: 1 + lowercase
3: 2 + numbers
4: 3 + special characters

Desired password strength (1-4): 4
Entry created!
Identifier (unique value): identifier
Website name or url: website.com
Nickname or email address: nick@name.com
Password: m%+Pk6^h

Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): mainpass
password_list.txt moved to Trash / Recycling bin.
Delete it and close this window for full protection.
```

2: You want to edit a new entry.

```
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
Enter main password to access encrypted passwords: mainpass

Identifier of what you want to edit: identifier

Desired new password length: 16

Strength
1: Uppercase
2: 1 + lowercase
3: 2 + numbers
4: 3 + special characters

Desired new password strength (1-4): 4
Password edited!
Identifier (unique value): identifier
Website name or url: website.com
Nickname or email address: nick@name.com
Password: 6xm@o8U5tz>K1jL[

Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): mainpass
password_list.txt moved to Trash / Recycling bin.
Delete it and close this window for full protection.
```

3: You want to search for an entry.

```
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: s

Decrypting file...
Enter main password to access encrypted passwords: mainpass

Identifier of what you want to search: identifier
Website name or url: website.com
Nickname or email address: nick@name.com
Password: 6xm@o8U5tz>K1jL[

Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): mainpass
password_list.txt moved to Trash / Recycling bin.
Delete it and close this window for full protection.
```
4: You want to view all entries.

```
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: v

Decrypting file...
Enter main password to access encrypted passwords: mainpass

'Identifier': ['Website', 'Nickname', 'Password']

'identifier': ['website.com', 'nick@name.com', '6xm@o8U5tz>K1jL[']]



Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): mainpass
password_list.txt moved to Trash / Recycling bin.
Delete it and close this window for full protection.
```

5. You want to delete an entry.

```
What do you want to do?
(A)dd an entry
(E)dit an entry
(D)elete an entry
(S)earch an entry
(V)iew all entries
(Q)uit

Enter command: d

Decrypting file...
Enter main password to access encrypted passwords: mainpass

Identifier of what you want to delete: identifier
Entry deleted!

Encrypting file...
Enter new main password (!!!DON'T FORGET IT!!!): mainpass
password_list.txt moved to Trash / Recycling bin.
Delete it and close this window for full protection.
```

## Author

* **Dave Trembay** - *Initial work* - [davetremblay](https://github.com/davetremblay)

## License

This project is licensed under the MIT License, see the [LICENSE.MD](LICENSE.MD) file for details.

## Acknowledgements

* Thanks to all those who report bugs and issues and help improve this project.

