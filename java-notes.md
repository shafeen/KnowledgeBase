## My miscellaneous Java notes
 
 
### I/O
 
#### `Scanner` vs `BufferedReader`
*coming soon*

#### Manually setting I/O streams when testing (JUnit)
*coming soon*

---

### Using Java 8 Lambdas & Streams

#### Lambdas
- format
- common use cases (Collections)  
*coming soon*


#### Using Java 8 Streams and common `map`/`reduce`/`filter` operations
- getting streams from collections and streams
*coming soon*
 
#### When should we *unbox* streaming values? 

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

*more coming soon*

--- 

### Exceptions

#### Checked vs Unchecked
*coming soon*

 