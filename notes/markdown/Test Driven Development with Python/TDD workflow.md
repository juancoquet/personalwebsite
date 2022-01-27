Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch3 p22

---
# TDD workflow
1. Start by writing a *functional test*, which describes the functionality form the user's point of view.
2. Start to think about what code needs to be written to get this test to pass. Now use *unit tests* to define how the code should behave.
3. Once you have a failing unit test, write the minimum necessary amount of production code to get the test to pass. You might iterate between steps 2 and 3 a few times until the functional test from step 1 progresses a little further.
4. Rerun the functional test(s) and gauge their performance. This may prompt you to write new unit tests, therefore more production code, and so on.

You can think of unit tests as being nested inside functional tests. First you write some functional tests and watch them fail. Then you write some unit tests to advance the functional tests and watch them fail. Now you can start writing production code, to advance the unit tests. As unit tests advance, you can once again check your functional tests, and keep adding functional tests and/or unit tests as needed.

![[Screenshot 2021-05-09 at 21.55.13.png]]

---
### See also:
- [[Unit Tests vs Functional Tests]]