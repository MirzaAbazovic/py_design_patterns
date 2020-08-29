# Desing patterns

## Intro

Pattern context consist of:

- Participants
- Quality attributes
- Forces
- Consequences

Participants are classes with roles (dispatcher, consumer etc).

Quality attributes are nonfunctional attributes like: Usability, modifiability, reliability, performace ,..
Effect on the entire software (architecture)

Forces are factors or trade-ffs to consider and are manifested in quality attributes.
If not considered might lead to unintended consequences (worst performance with better security)

Pattern language:

- Name (meaningful and memorable)
- Context (Scenario in which patter can be used. Provides insights for pro et contra for pattern)
- Problem (Design chalenge pattern is addressing)
- Solution (Specifies pattern with structure/relations and behaviour/interactions)
- Related patterns (list of other similar pattens with differences)


## Creational

### Factory

Encapsulates objects creation.

Useful when:

- not sure what kind of object you will need (uncertainties in type of objects)
- decisions must be made in runtime what class to use


### Abstract factory

Useful when user (clent) expects multiple related objects (family) but does not know which family until run time
Example:

Abstract factory -> Pet factory
Concrete factorise -> Cat factory, Dog factory

Abstract factory -> Abstract product
Concrete factorise -> Cat food, Dog food

## Structural

## Behavoural