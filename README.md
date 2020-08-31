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
Usage: Need cache for whole app. Heavy/costly operations of creation objects.
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

## Behavioural