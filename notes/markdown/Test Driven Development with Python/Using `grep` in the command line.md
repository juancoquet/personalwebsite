Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch14 p243

---
# Using `grep` in the command line
The `grep` command can be used to search for text in a file. It uses the syntax `grep <search query> <path to file(s)>`.
```bash
$ grep 'search for this' in/this/file.txt
```

It can be combined with other common bash commands, such as the `*` wildcard.
```bash
$ grep 'search for this' in/this/*.txt
```

The above command will search for the query in all `.txt` files contained in the `this` directory.

To search recursively, i.e. to search through all files under a directory and its sub-directories, use the `-r` option:
```bash
$ grep -r 'search for this' in/
```

Use the `-i` option to ignore case:
```bash
$ grep -r -i 'SeArCh FoR tHiS' in/
```