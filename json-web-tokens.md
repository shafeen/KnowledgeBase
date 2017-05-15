TODO: organize and elaborate on the topics below

JWT topics worth talking about
------------------------------
- basic flow
- access/refresh tokens
- sliding sessions

### General reference material
- [The Ins and Outs of Token Based Authentication](https://scotch.io/tutorials/the-ins-and-outs-of-token-based-authentication)
- [The Anatomy of a JSON Web Token](https://scotch.io/tutorials/the-anatomy-of-a-json-web-token)
- [Blacklisting JSON Web Token API Keys](https://auth0.com/blog/blacklist-json-web-token-api-keys/)
- [Access/Refresh Tokens: When to Use Them and How They Interact with JWTs](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)  
 

### Basic flow of a system using JSON Web Tokens (or JWTs) (show a use case)  
*coming soon...*


### JWT based Access-token/Refresh-token scheme
#### What are access/refresh tokens?
*coming soon...*
#### what is the flow of a jwt system implementing a refresh-token/access-token scheme?
*coming soon...*
#### Where should we store access/refresh tokens? 
*coming soon...*
##### access tokens are short lived, but how long should we allow a refresh token to remain valid?
*coming soon...*

### Sliding sessions
#### What are sliding sessions?
Sliding sessions are sessions that are kept alive by user activity, vs sessions that have a static expiration time.  
If a user is inactive (has performed no action) for a certain predetermined period of time, a sliding session should log the user out. On the flipside, every time the user performs an action while logged in, his/her session should be extended (there may be an upper bound set for this after which time the user is forced to log in again).
- stackoverflow - [How to change the session timeout in PHP?](http://stackoverflow.com/questions/8311320/how-to-change-the-session-timeout-in-php)



#### How can we implement sliding sessions using jwts?
You should be able to implement "sliding session" functionality using a JWT access-token/refresh-token scheme.  
*coming soon...*


