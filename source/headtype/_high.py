from headtype import _types
from headtype import _master


def create_type(type_, callback, *args, **kwargs):
    '''Creates type instance with associated callbacks.
    
    type_: Type
        Any type object like class.
    callback: Callable
        Callable accepting single argument being object to match against.
    fast_callaback: Callback
        Similar to callback but intended to be fast or approximation.
    object_types: Iterable[Type]
        Collection of object types supported by provided type.
    '''
    return _types.Type(type_, callback, **kwargs)

def create_types(types):
    '''Creates types instance from collection of type instances.
    
    types: Iterable[Type] | Types
        Collection of Type instances or Types instance'''
    return _types.Types(types)

def create_master(object_, types):
    '''Create master instance from object and types.
    
    object_: Any
        Any python object.
    types: Iterable[Type] | Types
        Collection of Type instances or Types instance.
    '''
    return _master.Master(object_, types)

def extract_types(types):
    '''Extracts underlying types/classes from types instance.'''
    return create_types(types).get_raw_types()

def extract_type(type_):
    '''Extracts underlying types/classes from type instance.'''
    return type_.get_type()


def find_matching_types(object_, types_, limit=None):
    '''Finds type matching provided object.'''
    master = create_master(object_, types_)
    types = master.get_matching_types(limit)
    return extract_types(types)

def find_matching_type(object_, types_):
    '''Finds type matching provided object.'''
    master = create_master(object_, types_)
    type = master.get_matching_type()
    if type: return extract_type(type)
