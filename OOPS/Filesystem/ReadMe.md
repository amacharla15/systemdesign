# File System OOP Design

A simple object-oriented file system model built in Python.

This project models a small file system using classes for files, directories, and the overall file system. It supports creating files and directories, searching for items, deleting items, and listing directory contents.

## Features

- Create files
- Create directories
- Search for files and directories
- Delete files and directories
- List directory contents
- Recursive traversal for nested directories

## Project Structure

The system is built around three main classes:

### File
Represents a file in the system.

State:
- `file_name`
- `file_type`

Behavior:
- rename a file

### Directory
Represents a directory that can contain:
- files
- other directories

State:
- `dir_name`
- `dir_content`

Behavior:
- create files
- create subdirectories
- search recursively
- delete recursively
- list direct children

### FileSystem
Represents the overall file system.

State:
- `root` directory

Behavior:
- starts all operations from the root directory
- delegates create, search, delete, and list operations to the root

## Design Notes

This project uses composition as the main design idea.

- A `Directory` contains `File` objects and other `Directory` objects
- A `FileSystem` contains the root `Directory`

This creates a tree-like structure where directories can be nested inside other directories.

## Supported Operations

### Create File
Adds a new file to the current directory.

### Create Directory
Adds a new subdirectory to the current directory.

### Search
Searches recursively through nested directories.

Search supports:
- file name
- full file name such as `notes.txt`
- directory name

### Delete
Deletes matching files or directories recursively.

### List
Lists direct children of the current directory.

## Example

Example structure:

root/
- notes.txt
- docs/
- main.py

Possible operations:
- create `notes.txt`
- create `docs`
- search for `main.py`
- delete `notes.txt`
- list items inside root

## Example Usage

```python
fs = FileSystem()

fs.file_create("notes", "txt")
fs.file_create("main", "py")
fs.dir_create("docs")

print(fs.list())
print(fs.search("notes.txt"))
print(fs.delete("main.py"))
print(fs.list())