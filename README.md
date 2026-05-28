# PyMaxHeap

# PyMaxHeap: Custom Max Heap Implementation

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)

##  Introduction

This project is a custom implementation of a Max Heap data structure from scratch using Python. It does not rely on the built-in `heapq` module. Instead, it manually maintains heap properties through an underlying array, fully implementing the core sift-up and sift-down operations.

This project is ideal for algorithm learning, data structure simulation, and serving as a low-level component for more complex systems. It also provides a command-line interactive interface based on standard input and output.

##  Features

* **Clear low-level logic**: The internal array uses 1-based indexing, making the mathematical calculation of parent and child node indices like `left = 2 * i` and `right = 2 * i + 1` much more intuitive.
* **Core operations supported**:
  * `push k`: Inserts the element  into the heap and automatically maintains the max heap property.
  * `pop`: Removes and returns the maximum element at the top of the heap, then rebalances the tree.
  * `peek`: Retrieves the value of the maximum element at the top of the heap without removing it.
* **Edge case handling**: Gracefully handles operations on an empty heap by returning and printing .

##  Quick Start

You can run this script directly via the terminal and pass operation commands through standard input.

### 1. File Input Mode

Create an `input.txt` file containing your test cases:

```text
6
push 10
push 25
push 5
peek
pop
peek
