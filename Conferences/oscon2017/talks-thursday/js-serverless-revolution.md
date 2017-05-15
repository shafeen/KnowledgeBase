 The serverless revolution for JavaScript developers
 ---------------------------------------------------

What is serverless? (hint: THERE ARE servers!)
F(unctions)aaS and B(ackends)aaS; examples include AWS lambda.

- Container technology enabled FaaS.
- Friendly to providers for efficient use of infrastructure.
- Metering model costfriendly to consumers
- Reduces costs for consumers and providers

AWS lambda is a service that runs your code in response to EVENTS!

FaaS Pricing:
Cost = Invocations + Compute time

Compute time: measured in GB-second
What's a GB-second?
- a measure of compute time 
- 1 second of wall-clock time with 1 GB provisioned

AWS and GCF both have free tiers, GCF is more generous.

You can run both interpreted code OR upload binaries in FaaS.

Deployment Options:
- serverless framework
- apex
- zappa
- chalice
- claudiaJS
- shep
- (there are more!)

Ways to use serverless computing:
- serving apis
- mobile apps
- iot
- data analysis
- ops triggers

FaaS in production:
- Bustle
- Coca-Cola uses it for their vending machines
- MLB advanced media: captures and analyzes every play

What to check out next:
- the awesome-serverless-list
- try out a serverless function (possible)

Challenges of Serverless:
- State
- Orchestration
- Deployment
- Testing
- Debugging
- Networking
- Monitoring



























