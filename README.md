# Design patterns

## Intro

Pattern context consist of:

- Participants
- Quality attributes
- Forces
- Consequences

Participants are classes with roles (dispatcher, consumer etc).

Quality attributes are nonfunctional attributes like: Usability, modifiability, reliability, performance ,..
Effect on the entire software (architecture)

Forces are factors or trade-ffs to consider and are manifested in quality attributes.
If not considered might lead to unintended consequences (worst performance with better security)

Pattern language:

- Name (meaningful and memorable)
- Context (Scenario in which patter can be used. Provides insights for pro et contra for pattern)
- Problem (Design challenge pattern is addressing)
- Solution (Specifies pattern with structure/relations and behaviour/interactions)
- Related patterns (list of other similar pattens with differences)

---

## Creational

### Factory

Encapsulates objects creation.

Useful when:

- not sure what kind of object you will need (uncertainties in type of objects)
- decisions must be made in runtime what class to use

- [code](src/main/creational/factory/factory.py)
- [test](src/test/creational/factory/test_factory.py)

### Abstract factory

Useful when user (clent) expects multiple related objects (family) but does not know which family until run time
Example:

Abstract factory -> Pet factory
Concrete factorise -> Cat factory, Dog factory

Abstract factory -> Abstract product
Concrete factorise -> Cat food, Dog food

- [code](src/main/creational/factory/abstract_factory.py)
- [test](src/test/creational/factory/test_abstract_factory.py)

### Singleton

OO way of providing global variables. 
Allows only one object to be instantiated
Usage: Need cache for whole app. 
Heavy aka costly aka expensive aka resource intensive operations of creation objects.
Sometimes also considered as anti-pattern.

- [code](src/main/creational/singleton/singleton.py)
- [test](src/test/creational/singleton/test_singleton.py)

### Builder

Solution for anti-pattern "telescoping constructor" (excessive number of constructors)

Roles:

- Director (in charge of building the product using the builder object)
- Abstract builder (interfaces)
- Concrete builder (implements interface of abstract builder)
- Product (object being build)

Doesn't rely on polymorphism (like factory and abstract factory), focuses to reduce complexity using divide-and-conquer strategy.

- [code](src/main/creational/builder/builder.py)
- [test](src/test/creational/builder/test_builder.py)

### Prototype

Use when creating many identical objects (cloning). 
Create prototype and then clone it (because maybe creating is expensive) when you need it.

Related with abstract factory.

- [code](src/main/creational/prototype/prototype.py)
- [test](src/test/creational/prototype/test_prototype.py)

---

## Structural

### Decorator

Add additional features to an existing object dynamically without using subclassing (inheritance)
Functions are objects in Python and we can add additional features to them.

Related with: adapter, composite and strategy. 

- [code](src/main/structural/decorator/decorator.py)
- [test](src/test/structural/decorator/test_decorator.py)

### Proxy

Proxy means ‘in place of’, representing’ or ‘in place of’ or ‘on behalf of’ 
are literal meanings of proxy and that directly explains Proxy Design Pattern.
Used for example when creating object that is resource intensive.
Controls and manage access to the object they are protecting, he is also substitute or placeholder for protected object. 
Allows you to perform something either before or after the request gets through to the original object (pre and post process hooks).


Roles:
- Producer (resource intensive creation)
- Artist (Proxy, placeholder to create object when necessary)
- Client (interacts with Artist-Proxy)

There are some types of proxies (by usage):

- Remote proxy (represent objects located remotely - over the wire, encapsulates (de)marshaling)
- Virtual proxy (produces default (dummy) results while proxied object is not ready)
- Protection proxy (uses impersonation to access object that app has no right to use)
- Smart proxy (adds additional layer of security, ex check is object locked)

Related patterns: Adapter and Decorator

- [code](src/main/structural/proxy/proxy.py)
- [test](src/test/structural/proxy/test_proxy.py)
    
### Adapter

Adapts (translates) incompatible interfaces between client and server ->
allows objects with incompatible interfaces to collaborate.

This pattern involves a single class which is responsible to join functionalities of independent or incompatible interfaces.

Solves problems like:
Reusing code that does not have an interface that a client requires.
Code with incompatible interfaces work together.

To use an adapter in our code:

1. Client should make a request to the adapter by calling a method on it using the target interface.
2. Using the Adaptee interface, the Adapter should translate that request on the adaptee.
3. Result of the call is received the client and he/she is unaware of the presence of the Adapter’s presence.

Related patterns: Bridge and Decorator

References:

- https://www.geeksforgeeks.org/adapter-method-python-design-patterns/

- [code](src/main/structural/adapter/adapter.py)
- [test](src/test/structural/adapter/test_adapter.py)
   

## Behavioural