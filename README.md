<p align="center">
  <img src="https://github.com/sebas119/AirBnB_clone/blob/master/utils/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">ALX School BnB</h1>
<p align="center">An AirBnB clone - The Console.</p>

<hr>

## Description :house:

AirBnB Clone is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Classes :cl:

AirBnB utilizes the following classes:

* BaseModel
* FileStorage
* User
* State
* City
* Amenity
* Place
* Review


## Storage :baggage_claim:

The storage engine is defined in the FileStorage class and will add, save and reload objects into the private class attribute "__objects".

We made an instance for this class that is named "storage" and then immediately the method reload() is called, this will open the file.json if exists and charge all the objects in json format that are saved there in the private class attribute "__objects".

## Console :computer:

The command line interpreter is an interface that we build to have interaction with the backend functions in the ALX project. Is an easy tool to test and manage a loot of functionalities.

It use the cmd.Cmd framework from python that has several built-in methods to deal with interactive and non-interactive mode.

### How to use it

Our shell work like this in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

In order to use the HBNB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HBNB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and 
the instance is saved to the file `file.json`.

```
$ ./console.py
(hbnb) create User
3702fbb0-97be-4b24-9cb8-bd62943abf97
(hbnb) EOF
$ cat file.json ; echo ""
{"User.3702fbb0-97be-4b24-9cb8-bd62943abf97": {"created_at": "2022-11-20T01:44:01.693073", "id": "3702fbb0-97be-4b24-9cb8-bd62943abf97", "updated_at": "2020-02-20T01:44:01.693097", "__class__": "User"}}

```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
3702fbb0-97be-4b24-9cb8-bd62943abf97
(hbnb)
(hbnb) show User 3702fbb0-97be-4b24-9cb8-bd62943abf97
[User] (3702fbb0-97be-4b24-9cb8-bd62943abf97) {'id': '3702fbb0-97be-4b24-9cb8-bd62943abf97', 'updated_at': datetime.datetime(2022, 11, 24, 1, 44, 1, 693097), 'created_at': datetime.datetime(2020, 2, 20, 1, 44, 1, 693073)}
(hbnb)
(hbnb) User.show(3702fbb0-97be-4b24-9cb8-bd62943abf97)
[User] (3702fbb0-97be-4b24-9cb8-bd62943abf97) {'id': '3702fbb0-97be-4b24-9cb8-bd62943abf97', 'updated_at': datetime.datetime(2022, 11, 24, 1, 44, 1, 693097), 'created_at': datetime.datetime(2022, 11, 24, 1, 44, 1, 693073)}
(hbnb)
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id.

```
$ ./console.py
(hbnb) create Place
d4f1ceff-dd29-4b09-a221-45addb80accc
(hbnb) 
(hbnb) create Amenity
171f546a-9fea-4fdb-b35f-bf510467500f
(hbnb) 
(hbnb) destroy Amenity 171f546a-9fea-4fdb-b35f-bf510467500f
(hbnb) Place.destroy("d4f1ceff-dd29-4b09-a221-45addb80accc")
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class.

```
$ ./console.py
(hbnb) create User
90b1e33d-7b5b-43c2-9596-a04a79ae327b
(hbnb) create User
8263962a-3415-4f54-9f8c-a79f16698f27
(hbnb) create Place
d16b4805-8826-4828-9fed-655ffb1c2b50
(hbnb) create BaseModel
5a16683d-2bf4-47e6-8082-0d12814e8572
(hbnb) 
(hbnb) all Place
["[Place] (d16b4805-8826-4828-9fed-655ffb1c2b50) {'id': 'd16b4805-8826-4828-9fed-655ffb1c2b50', 'created_at': datetime.datetime(2022, 11, 24, 1, 54, 1, 887235), 'updated_at': datetime.datetime(2022, 11, 24, 1, 54, 1, 887266)}"]
(hbnb) 
(hbnb) User.all()
["[User] (8263962a-3415-4f54-9f8c-a79f16698f27) {'id': '8263962a-3415-4f54-9f8c-a79f16698f27', 'created_at': datetime.datetime(2022, 11, 24, 1, 53, 57, 556946), 'updated_at': datetime.datetime(2022, 11, 24, 1, 53, 57, 556976)}", "[User] (90b1e33d-7b5b-43c2-9596-a04a79ae327b) {'id': '90b1e33d-7b5b-43c2-9596-a04a79ae327b', 'created_at': datetime.datetime(2022, 11, 24, 1, 53, 54, 246663), 'updated_at': datetime.datetime(2022, 11, 24, 1, 53, 54, 246687)}"]
(hbnb) 
(hbnb) all
["[User] (8263962a-3415-4f54-9f8c-a79f16698f27) {'id': '8263962a-3415-4f54-9f8c-a79f16698f27', 'created_at': datetime.datetime(2022, 11, 24, 1, 53, 57, 556946), 'updated_at': datetime.datetime(2022, 11, 24, 1, 53, 57, 556976)}", "[Place] (d16b4805-8826-4828-9fed-655ffb1c2b50) {'id': 'd16b4805-8826-4828-9fed-655ffb1c2b50', 'created_at': datetime.datetime(2022, 11, 24, 1, 54, 1, 887235), 'updated_at': datetime.datetime(2022, 11, 24, 1, 54, 1, 887266)}", "[User] (90b1e33d-7b5b-43c2-9596-a04a79ae327b) {'id': '90b1e33d-7b5b-43c2-9596-a04a79ae327b', 'created_at': datetime.datetime(2022, 11, 24, 1, 53, 54, 246663), 'updated_at': datetime.datetime(2022, 11, 24, 1, 53, 54, 246687)}", "[BaseModel] (5a16683d-2bf4-47e6-8082-0d12814e8572) {'id': '5a16683d-2bf4-47e6-8082-0d12814e8572', 'created_at': datetime.datetime(2022, 11, 24, 1, 54, 9, 979842), 'updated_at': datetime.datetime(2022, 11, 24, 1, 54, 9, 979873)}"]
(hbnb) 
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create City
8a24c74a-0f6f-47c4-a4a6-241b03ccaa25
(hbnb) create User
7f4dcd79-86ee-4238-833d-b5f632e921ab
(hbnb) create User
28d3e106-2543-446e-9432-8b64d22ccc0f
(hbnb) count User
2
(hbnb) City.count()
1
(hbnb) 
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. 
```
$ ./console.py
(hbnb) 
(hbnb) create City
d541356b-172d-4015-bd7c-4d4f73d93623
(hbnb) update City d541356b-172d-4015-bd7c-4d4f73d93623 name "Cali"
(hbnb) show City d541356b-172d-4015-bd7c-4d4f73d93623
[City] (d541356b-172d-4015-bd7c-4d4f73d93623) {'id': 'd541356b-172d-4015-bd7c-4d4f73d93623', 'name': 'Cali', 'updated_at': datetime.datetime(2022, 11, 24, 2, 1, 24, 442191), 'created_at': datetime.datetime(2022, 11, 24, 2, 0, 22, 500641)}
(hbnb) City.update("d541356b-172d-4015-bd7c-4d4f73d93623", "name", "Bogota")
(hbnb)
(hbnb) show City d541356b-172d-4015-bd7c-4d4f73d93623
[City] (d541356b-172d-4015-bd7c-4d4f73d93623) {'id': 'd541356b-172d-4015-bd7c-4d4f73d93623', 'name': 'Bogota', 'updated_at': datetime.datetime(2022, 11, 24, 2, 2, 31, 277387), 'created_at': datetime.datetime(2022, 11, 24, 2, 0, 22, 500641)}
(hbnb) 
```

## How to test :straight_ruler:

Unittests for the ALX project are defined in the [tests](./tests) 
folder. 

Run all test:
```
$ python3 unittest -m discover tests
```

Run a specific single test:
```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:
* **Raymond Lukwago** <[lukwagoraymond](https://github.com/lukwagoraymond)>
* **Sheriffdeen Yusuf** <[sheriffdean-yusuf](https://github.com/sheriffdean-yusuf)>
