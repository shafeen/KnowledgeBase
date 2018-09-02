# Understanding Modern Cloud Architecture

The Plan for this talk: 

- Evolution of distributed applications and role in the cloud
- Building up to where we are today
- I'll explain the technologies involved along the way

---

### Evolution of distributed applications and role in the cloud

#### The Monolith

Benefits:

- Easy to deploy
- Well known and easy to comprehend (especially for a junior team of developers)
- No calls over the wire
- IDE friendly

Cons:

- Failures can be harder to debug
- Might not be scalable (enough), scale out or scale up.
- The team: Teams may have to wait for one another to be done to start working on something
- The bigger, the harder to maintain due to difficulty decoupling subcomponent of the applications
- Tends to get bigger 
- One stack.

Distributing components might be able to alleviate some of these problems. These components may be web apis, or an entire sub-application (like an angular front-end application).

---

#### SOA (Service Oriented Applications)

This may be a way to solve a few of the monolith's problems.

Commonly used SOA techniques:

##### Remote Procedure Call: Call a function over the wire

We don't tend to use this technique in modern applications.

Has high Platform, Behavioral and Temporal Coupling.

##### SOAP: Simple Object Access Protocol - Call function using standardized ZXML

Somewhat solves Platform coupling (low), but still has high Behavioral and Temporal Coupling.

##### REST:

Low Platform and Behavioral coupling, but still has high temporal coupling.

##### Microservices: 

Small Autonomous Components which communicate with each other using messages.

Miscroservices process queues of messages when they are up, those messages simply wait in their respective mailboxes if the microservice is not up. This is how microservices solve the temporal problem.

Microservices can also use their own stack and technologies.

Has low Platform, Behavioral and Temporal Coupling.

Downsides:

- Complex in nature, hard to maintain without the right team or set of skills available
- Hard to monitor status.

Could be the holy grail of decoupling, but not for all teams. The key thing is to get monitoring right.

---

#### Serverless Functions

Cloud only architecture. Create a function to the cloud. Uses a FaaS hosting model and scale on demand.

Negligible Platform and Behavioral coupling but the amount of Temporal Coupling depends of the type of triggers used.

Examples of triggers:

- File upload
- Record updated in batabase
- Timer elapsed
- HTTP request (web hook)
- Service bus message

----

#### The Role of the Cloud:

Evolution of Cloud Hosting : On Premises -> IaaS -> PaaS -> FaaS.

Examples of Cloud Services:

- Caching 
- Storage
- Security
- Service Bus
- AI
- IoT

A modern cloud architecture is a composition of cloud services.

---

Personal Questions: 

1. What is a Service Bus?



