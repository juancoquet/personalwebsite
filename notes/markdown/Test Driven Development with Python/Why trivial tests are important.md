Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch4 p39

---
# Why trivial tests are important
It may seem silly, and overkill at first, to test every minute detail in the early stages of a project—such as testing that your URL maps to the right *view* function, or testing that you receive a simple HTML response. However, these early tests are very important to set the foundation for your code as it grows and develops.

As the functions you are testing grow in complexity, they become increasingly difficult to test if you have not been testing them from the beginning. Setting up trivial tests at the start allows you to expand them as your application becomes more complex, which means you are never faced with a situation where you have to write a test from scratch for a complex function with many conditionals and advanced class structures.

The discipline of strict testing is like the discipline of learning a martial art—you must obey the rules and practice them intently for a long time before deciding if you want to break them. That means writing trivial tests.