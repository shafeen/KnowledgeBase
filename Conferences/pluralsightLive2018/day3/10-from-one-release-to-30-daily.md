# From one release per quarter to 30 times a day

Why 30? To unlock new ways of thinking.

Is duplicate code bad? It depends.

What we are really fighting as SDEs is the coupling. Coupling creates choke points in your software.

What don't we have enough of? Time.

Most organizations are optimized on *RESOURCES*.

We need to move from Resoruce Optimized to *TIME TO MARKET* optimized.

- Customer journey
- Organized on value stream (functional cohesive)
- Less hand-offs, higher quality and fewer highly skilled perople in the value stream.

We need to create **FLOW** (read Elyahu Goldratt - The Goal)

#### 1. Bottleneck - increase flow:

- make teams self sufficient

#### 2. Bottleneck - existing DC and intertia of IT ops / many rules on governance

- infrastructure as code, configuration as code
- implement the 4 eyes principle
- consider moving to the public cloud
- automate as much as you can

#### 3. Bottleneck - tooling / everything is still manual

- Automate EVERYTHING as much as you can
- needed for repeatable and reliable deployments to the cloud

#### Where are we?

- We have value stream based teams.
- We have a fully automated build.
- We have a fully automated deployment configuration in code

#### 4. Bottleneck - manual testing is slowing us down.

- Separate deployment from feature reveal.

Use of feature flags / toggles

- When you want to ship often, how do we cope with unfinished or untested code?
- Traditionally, you use feature branches to isolate
  - but what if you ship daily or weekly?
- Break up changes in independent parts that can be release separately
  - use feature toggles/flags to enable or disable features
  - give business control over who gets which feature

Note: that feature toggles need to be maintained, they need to be cleaned up over time (consider using a timestamp with your feature toggle).

Remember: the goal is to NEVER ROLL BACK!

#### 5. Bottleneck - branching strategy slows down releases.

Current: git-flow (works well for boxed products)

New: github-flow (uses pull requests when trying to deploy to production)

---

#### Blue / Green Deployments

Move traffic gradually fromt the blue to green node from 0 to 100% via a router. And then vice versa. Look at **canary** releases

---

#### What about the database when we deploy a new schema? 

Create binaries that are multi schema compatible.

Migrate data slowly to the new schema

Be careful with updating tables:

- don't take a lock on the table 
- always append on the table
- use nullable fields first

Update binaries to only use the new schema, clean up the old schema.

#### Measure and Learn

Have telemetry in place for your application:
- **U**sage
- **P**erformance
- **A**vailability
- **L**ogs

#### Release gates based on Telemetry

If gates succeed, deployment accepted, rejected otherwise. CI for example.



