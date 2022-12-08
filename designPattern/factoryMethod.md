~~~mermaid
classDiagram
    class Factory {
        +get_shape() Shape
    }

    class Shape {
        <<interface>>
        +draw() void
    }

    class Ractangle{
        +draw() void
    }

    class Square{
        +draw() void
    }

    Shape <|-- Ractangle
    Shape <|-- Square   
    Factory --> Shape
~~~