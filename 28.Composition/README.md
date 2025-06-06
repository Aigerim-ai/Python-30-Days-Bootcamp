## 🧱 What Is Composition? (In Simple Terms)

**Composition** means that one class contains objects of other classes as part of its own structure — to use their behavior or data.  
Instead of _inheriting_ features, it _uses_ them by including them.

> ✅ Think: "A car **has** an engine" (NOT "A car **is** an engine").

---

## 📌 Step-by-Step Breakdown with Examples

---

### ✅ Step 1: Think About Responsibilities

Break your system into small components, each responsible for one thing.

**Example:**  
We want to model a **Car**.  
A car has:

- an **Engine** (to drive)
- a **MusicPlayer** (to play music)

These are **components** of a car.

---

### ✅ Step 2: Create Component Classes

Let’s write the individual components as separate classes.

```python
class Engine:
    def start(self):
        return "Engine started"

class MusicPlayer:
    def play(self):
        return "Playing music"
```

These classes do **one thing each**:

- `Engine.start()` starts the engine.
- `MusicPlayer.play()` plays music.

---

### ✅ Step 3: Compose Them in Another Class

Now we create the `Car` class. It will **have** an `Engine` and a `MusicPlayer`.

```python
class Car:
    def __init__(self):
        self.engine = Engine()
        self.player = MusicPlayer()

    def start_car(self):
        return self.engine.start()

    def play_music(self):
        return self.player.play()
```

Now `Car` is **composed** of two classes:

- `Engine`
- `MusicPlayer`

---

### ✅ Step 4: Use the Composed Object

```python
my_car = Car()

print(my_car.start_car())    # Output: Engine started
print(my_car.play_music())   # Output: Playing music
```

The `Car` class did not inherit anything from `Engine` or `MusicPlayer`.  
It just **uses** them — that’s Composition.

---

## 🤔 Why Use Composition Instead of Inheritance?

### ✅ More Flexibility

Let’s say you want a **SportsCar** with a better music system:

```python
class PremiumMusicPlayer:
    def play(self):
        return "Playing premium sound"

class SportsCar:
    def __init__(self):
        self.engine = Engine()
        self.player = PremiumMusicPlayer()

    def start_car(self):
        return self.engine.start()

    def play_music(self):
        return self.player.play()
```

You swapped in a different component without needing to rewrite or inherit anything — just plug and play.

---

## 🎯 Summary

| Feature      | Composition                                      |
| ------------ | ------------------------------------------------ |
| Definition   | A class has one or more objects of other classes |
| Purpose      | Combine behaviors instead of inheriting          |
| Relationship | "Has-a" (e.g. a Car has an Engine)               |
| Flexibility  | High (you can swap components easily)            |
| Example      | `Car` uses `Engine` and `MusicPlayer`            |

---

# Composition in Object-Oriented Programming

Composition is a fundamental concept that models a "has-a" relationship between classes, where one class (the composite) contains one or more objects of another class (the component) as part of its structure.

## Key Characteristics of Composition

- **"Has-a" Relationship**: Expresses that one object contains or is composed of other objects
- **Code Reuse**: Achieved by combining simple objects into more complex ones
- **Flexibility**: Components can be changed at runtime
- **Encapsulation**: The composite controls access to its components

## UML Representation

```
    ┌─────────────┐        ┌─────────────┐
    │  Composite  │<>─────>│  Component  │
    └─────────────┘        └─────────────┘
```

- The diamond on the composite side indicates composition
- The arrow points to the component class
- Cardinality is shown near the component (default is 1 if not specified)

## Cardinality Notation

| Notation | Meaning                          |
| -------- | -------------------------------- |
| 1        | Exactly one component            |
| \*       | Zero or more components          |
| 1..\*    | One or more components           |
| 0..1     | Optional (zero or one) component |
| 1..4     | Between one and four components  |

## Example

```python
class Tail:
    def wag(self):
        print("Tail wagging")

class Horse:
    def __init__(self):
        self.tail = Tail()  # Horse "has-a" Tail

    def show_happiness(self):
        self.tail.wag()

class Dog:
    def __init__(self):
        self.tail = Tail()  # Dog also "has-a" Tail

    def express_joy(self):
        self.tail.wag()
```

## Advantages of Composition

1. **Greater Flexibility**: Components can be swapped at runtime
2. **Better Encapsulation**: Internal implementation details are hidden
3. **Avoids Inheritance Limitations**: No fragile base class problem
4. **Promotes Loose Coupling**: Components can be developed independently
5. **Supports Single Responsibility**: Each class focuses on one thing

## Composition vs. Inheritance

While inheritance represents "is-a" relationships (Horse is an Animal), composition represents "has-a" relationships (Horse has a Tail). Composition is generally preferred when:

- The relationship is more about capabilities than identity
- You need to change behavior at runtime
- You want to share functionality between unrelated classes
- You want to avoid deep inheritance hierarchies

## Practical Use Cases

- A `Car` has an `Engine`
- A `Computer` has a `CPU`, `RAM`, and `Storage`
- A `House` has `Room` objects
- A `Playlist` has `Song` objects
