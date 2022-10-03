# headtype
Headtype is a python library for finding types/classes associated with
object. Sometimes it may be worth it to know which object would work with
class or vice-verse. You wouldnt want to pass non url object into class
that expects url in string form.

Managing objects and classes could be a lot work especially having to do
repeately. This library takes that away and let you focus on how 
classes/types would be matched against objects.

### Install
Enter this into your command-line application.
```bash
pip install headtype
```

### Usage
The first thing is to import headtype library.
```python
import headtype
```

Now headtype is imported and ready to use, its time to specify types/classes
to be matched by objects. This will create `headtype.Type` instances that contain 
class/type along with how it will match objects.

But first we need to setup functions for matching objects before creating 
those `headtype.Type` instances.
```python
def names_func(object_):
    return object_ in {"marry", "john", "hope"}

def fruits_func(object_):
    return object_ in {"apple", "orange", "grapes"}

def numbers_func(object_):
    return object_ in {100, 500, 1000, 5000, 10000}
```

Since functions for matching are now setup, let setup types to be matched
with objects. We will also create fake classes for use with examples to 
make things clear.
```python
class names(): pass

class fruits(): pass

class numbers(): pass
```

Now everything is ready to actually create `headtype.Type` instances from 
those classes and functions.
```python
# Here headtype.Type instances get created and associated with functions.
names_type = headtype.create_type(names, names_func)
fruits_type = headtype.create_type(fruits, fruits_func)
numbers_type = headtype.create_type(numbers, numbers_func)
```

Type instances need to be grouped into collection of types either
in form of iterable or `headtype.Types`. 
```python 
# Creates list with headtype.Type instances
type_objects = [names_type, fruits_type, numbers_type]
# Creates headtype.Types instance from headtype.Type instances.
types_object = headtype.create_types(type_objects)
```

Let now check if object and type really match with each other based on
that function set type.
```python
# 1000 is number and is not in names.
headtype.object_matches_type(1000, names_type) # False
# 'John' is in names and get matched.
headtype.object_matches_type("john", names_type) # True
# 1000 is number and satisfies numbers_type
headtype.object_matches_type(1000, numbers_type) # True
```

What about finding types/classes that matches certain object?, thats also
possible. This is when order of items may become important especially if
aim is to get single type.
```python
# This gets first type matched(types order matters)
# Just as expected, nothing was matched.
headtype.find_matching_type(1000, type_objects) # None
# 'orange' is fruit according to fruits_type.
headtype.find_matching_type("orange", type_objects) 
# <class '__main__.fruits'>

# This gets multiple types but results is filter object.
matched_types = headtype.find_matching_types("orange", type_objects) 
list(matched_types) # [<class '__main__.fruits'>]
# Limit can be provided to limit items involved.
matched_types = headtype.find_matching_types(500, type_objects) 
list(matched_types) # [<class '__main__.numbers'>]
```

There is something very obvious about the `headtype.Type` instances in 
that they expect certain types of objects. Both `names_type` and 
`fruits_type` expects objects of `str` and `numbers_type` expects `int` 
object types.

It may be better to remove `headtype.Type` instances that does not 
correspond with object type. That is done by supplying object types
supported by `headtype.Type` instance.

Here are new `headtype.Type` instances with objects types/classes they
expected their objects to be. This may improve performance especially
if `headtype.Type` instances take long to match objects.
```python
# Much faster since objects types are provided.
names_type = headtype.create_type(names, names_func, object_types=[str])
fruits_type = headtype.create_type(names, fruits_func, object_types=[str])
numbers_type = headtype.create_type(names, names_func, object_types=[int])
```

### License
[MIT license](https://github.com/sekgobela-kevin/headtype/blob/main/LICENSE)