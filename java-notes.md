## My miscellaneous Java notes
 
 
## Java I/O
 
### `Scanner` vs `BufferedReader`

Besides the obvious pattern matching and tokenizing functionality in `Scanner`, 
a major difference between the two is that `Scanner` has a smaller default 
buffer size (1024) which also not growable as opposed to `BufferedReader` which
has a larger buffer size (8192) **and** is growable as needed.  

**Sample usages demo-ing getting input from STDIN:**
```Java
// Scanner class
Scanner in = new Scanner(System.in);
System.out.println(in.nextLine());
```
```Java
// BufferedReader class
BufferedReader inputReader = new BufferedReader(new InputStreamReader(System.in));
System.out.println(inputReader.nextLine());

// If you really want the functionality that the Scanner offers,
// you can always create a Scanner object with the contents of the line
Scanner in = new Scanner(inputReader.nextLine);
System.out.println(in.nextInt());
```

### Manually setting I/O streams when testing (JUnit)
- Use of `System.setIn`/
- Use of `ByteArrayOutputStream` in conjunction with `System.setOut`/`setErr`  
*coming soon...*  

**Links:**
- [JUnit test for System.out.println()] (http://stackoverflow.com/questions/1119385/junit-test-for-system-out-println)

---

## Using Java 8 Lambdas & Streams

### Lambdas
- format
- common use cases (Collections)    
*coming soon...*

**Links:**
- [Java docs: Lambda Expressions] (https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Lambda Expressions in Java 8] (http://www.drdobbs.com/jvm/lambda-expressions-in-java-8/240166764)

### Using Java 8 Streams and common `map`/`reduce`/`filter` operations
- getting streams from collections and streams
*coming soon...*
 
### When should we *unbox* streaming values? 

**Example:**  
Compare the runtimes of these 2 similar snippets of code below
```Java
List<Integer> list = new LinkedList<>();
while (list.size() < 1000000) {
    list.add(list.size() + 1);
}

long start = System.currentTimeMillis();
System.out.println(list.stream().mapToInt(e -> e).map(v -> v-100).reduce(0, (p, v) -> p + v));
System.out.println(System.currentTimeMillis() - start);
```
```Java
List<Integer> list = new LinkedList<>();
while (list.size() < 1000000) {
    list.add(list.size() + 1);
}

long start = System.currentTimeMillis();
System.out.println(list.stream().map(v -> v-100).reduce(0, (p, v) -> p + v));
System.out.println(System.currentTimeMillis() - start);
```

The 1st code snippet with the unboxed values should have a noticably faster runtime.

*more coming soon...*

--- 

## Exceptions

### Checked vs Unchecked
*coming soon...*

 