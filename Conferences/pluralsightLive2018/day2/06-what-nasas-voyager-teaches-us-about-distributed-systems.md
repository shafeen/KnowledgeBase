# What NASA's Voyager mission teaches us about building distributed systems

### Understand the mission

Take a "grand tour".

Build to last and expand our knowledge.

Leave our mark with the golden record.

Redundancy: 2 ships, 2 paths and duplicted systems.

#### Embrace redundancy

- Redundancy at each layer (infrastructure, networking, software, databases)
- May be active or passive
- Cloud platforms offer via configuration AND architecture
- Multi-cloud offers new redundancy options

#### Lesson: be creative with your what-if analysis 

You can have thorough testing but still be surprised.

- In distributed systems, you need to consider more failure points.
- Identify SPOF, and either mitigate or document.
- Consider using the chaos engineering approach.

#### Lesson: Reuse whenever possible

- Reuse architecture patterns 
- Reuse aspect-oriented concerns like indentity, logging monitoring, and configuration.
- Leverage existing application platforms and common (operational) abstractions.

#### Lesson: Bake in the flexibility you'll need

-  Decompose systems into individually updateable components.
- Use Dependency Injection where it makes sense.
- Externalize configuration and environment-specific behavior (from your code).
- Use things like feature flags to achieve "progressive delivery" (good idea to bake into self rolled framework).

#### Lesson: Solve problems with what's available

- Accept that constraints can be freeing (too many options can be paralyzing)
- Use existing people and technology where possible
- Don't create new "platforms" when current ones are sufficient.
- Introduce new components after careful consideration.

#### Lesson: Have respect for earlier decisions

- Don't immediately dismiss prior choices (notice that we are the next generation's idiots)
- Review documentation and context
- Recognize the simplicity of original design
- Be sure to understand the impact of "upgrading"

#### Lesson: Don't skimp on instrumentation

- Make subsystems and services observable 
  - your system should be able to tell you that it's healthy
- Use configurations to turn instrumentation on and off
- Get the big picture through distributed tracing and correlation (be able to monitor stuff like latency in your applications)
- Use this data to power your automation, and decision making.

#### Lesson: Take advantage of Expert Advice

- Solicit feedback on your design, early and often.
- Use conferences and meetups to discuss assumptions.
- Leverage SREs (System Reliability Engineers) to explore your system reliability.

#### Lesson: Documentation matters

- Write for the later audience (developers, operators), not your current self.
- Call out assumptions and constraints.
- Be specific about functionality and parameters
- Document expected errors and how they are handled.
- Keep it up to date.

#### Lesson: Leadership Matters

- Need leaders who can build consensus 
- Want leaders that empower others
- Look for passion, but also calm under pressure

---

#### Connect the Dots

We need to know that as software engineers the only reason we are building something is to make something that adds some kind of customer value. It can be easy to get caught in the tech, but try to look back at your system periodically to stop yourself from overly geeking out on the tech and balance that with actually adding customer value.

 







