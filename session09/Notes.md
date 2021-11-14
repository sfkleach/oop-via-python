# Notes on Bonus Session 09

I thought it might be interesting to review SOLID. Here's a nice
article on SOLID that is a wall to bounce off:

https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/

1. Single responsibility principle - it is inherently confusing because some 
class somewhere has to integrate responsibilities, right? The key is the concept
of class/object boundaries and saying that _within the boundary_ of a class
there is only 1 responsibility. What this really means is to prefer 
composition (actually aggregation) as a means of joining functionality. But
this is a dubious principle, since extension and composition are duals.

2. Open-Closed Principle - this is generally misinterpreted in the form of
a language anti-pattern. "This is part of the design of languages like Java—you 
can create classes and extend them (by creating a subclass), but you can’t 
modify the original class." No, this is not the right explanation. Java closes 
classes with regard to extension - you have to create new classes. It is 
probably better to see the Open-Closed Principle as a form of monotonic 
extension where you do not undo existing properties but only ever add new 
properties.

3. Liskov Substitution Principle - is actually a genuine principle. It states
that should be able to substitute a sub-type wherever the parent type works. 
This is monotonicity applied to sub-types. Why is it a genuine principle? 
Because it applies to the modelling process in the problem domain.

4. Interface Segregation Principle - is really advice for how to use explicit
type assertions. It's not a principle for OOP. It boils down to the idea that
we should not add type assertions that invalidate working programs i.e. type
assertions should be as weak as possible. It is a corollary of the Dollin
Principle.

5. Dependency Inversion Principle - is exactly the same principle as the 
Interface Segregation Principle. Use the weakest type assertions.
