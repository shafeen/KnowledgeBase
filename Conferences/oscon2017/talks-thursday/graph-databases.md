Graph databases will change your freakin' life 
-----------------------------------------------

Lets talk about property graphs.
- neo4j <<---
- janusgraph
- orientdb
- (there are more)

Nodes have properties: keys/values.
Nodes have labels to tell you what type of thing it is.

Nodes are connected by relationships, relationships can have types. Relationships are one way only in neo4j!
In a graph db, relationships are first class objects.

When the meaning is in the relationships, graph dbs can be useful.
Direct relationships can be pretty easy to do with relational databases.
Sometimes we have indirect relationships, this is harder to do with relational databases.

Graph dbs are very good at answering questions you didn't expect (when you first designed the database). You can add more relationships as needed and still be performant.

Neo4j's query language is called "cypher".

Analogous to indexes? There are indexes in graphs as well.






