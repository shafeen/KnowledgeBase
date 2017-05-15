A journey into feature toggles:
-------------------------------

Check out [martin fowlers blog](http://martinfowler.com/articles/feature-toggles.html) on this topic. 

Feature switches decouple deployment from release. It lets you release code not yet introduced to your users.

It lets you work with the master branch while keeping working code safe.

It's a way to choose code paths at runtime.

Treat different use cases of FT(feature toggles)s differently.
    - Release toggles
    - Permission toggles (differentiate premium vs basic users, admins vs users)
    - Ops toggles (kill switch)
    - Experimental toggles

---

##### Release Toggles:
- Around for DAYS.
- vary per deployment
- owned by devs

##### Permission Toggles:
- Around for YEARS.
- Owned by product

##### Experimental toggles:
- vary per request
- Owned by product

##### Ops toggles:
- owned by ops

---

#### Toggle Longevity

- Don't leave "if(featureEnabled())-else" in your code base if you don't need to coz it does affect your code base and you should give it te respect it needs. Consider replacing it with polymorphism or the strategy pattern.


#### Toggle Configuration

static                                                                dynamic 
<----------------------------------------------------------------------------->
hard coded | config baked into deployment | param config | config in app db | 

dynamic
 -------------------------->
distributed config

#### Advice: 
have the toggle configuration as static as possible.
- reason: devs like to make them super complicated 
Make the toggle configuration observable (api endpoint or ui).
Allow overriding configuration for testing.

#### Warning: 
Be aware that toggles aren't free.
Testing toggled code isn't easy.

Ultimately feature toggles help you write code easier.

One way to prevent long lived feature switches is to put in a "time bomb" such that the app will not start out if the feature switch is older than X.



















