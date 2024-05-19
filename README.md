# AirBnB Clone

## Overview
Welcome to the AirBnB Clone project! This is the first step in building a full web application, and it lays the foundation for subsequent projects. The primary goals of this project include creating a parent class (BaseModel) for initialization, serialization, and deserialization. Additionally, you will establish a simple flow for serialization/deserialization, create classes for AirBnB entities (User, State, City, Place, etc.), and implement a file storage engine.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SalahMSwefy/AirBnB_clone
    cd AirBnB_clone
    ```
2. Run the console application:
    ```bash
    ./console.py
    ```

## Examples
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Usage
1. Start the console in interactive mode:
    ```bash
    $ ./console.py
    (hbnb)
    ```
2. Use help to see the available commands:
    ```bash
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)
    ```
3. Quit the console:
    ```bash
    (hbnb) quit
    ```

## Commands
The commands are displayed in the following format: `Command / Usage / Example with Output`

### Create
Creates a new instance of a given class. The class' ID is printed, and the instance is saved to the file `file.json`.
```bash
create <class>
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

### Show
Displays information about an instance of a given class with a specific ID.
```bash
show <class> <id>
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

### Destroy
Deletes an instance of a given class with a given ID.
```bash
destroy <class> <id>
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```

### All
Prints all string representations of all instances of a given class or all classes.
```bash
all [class]
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode
```

### Update
Updates an instance based on the class name, ID, and key-value pairs passed.
```bash
update <class> <id> <attribute> <value>
(hbnb) create User
1afa163d-486e-467a-8d38-3040afeaa1a1
(hbnb) update User 1afa163d-486e-467a-8d38-3040afeaa1a1 email "aysuarex@gmail.com"
(hbnb) show User 1afa163d-486e-467a-8d38-3040afeaa1a1
[User] (s) [User] (1afa163d-486e-467a-8d38-3040afeaa1a1) {'id': '1afa163d-486e-467a-8d38-3040afeaa1a1', 'created_at': datetime.datetime(2021, 11, 14, 23, 42, 10, 502157), 'updated_at': datetime.datetime(2021, 11, 14, 23, 42, 10, 502186), 'email': 'aysuarex@gmail.com'}
(hbnb)
```
