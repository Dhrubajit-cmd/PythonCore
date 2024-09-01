# In this class we shall learn about Hybrid and Hierarchial Inheritance in Python .
# Isi technique of inheritance ko hybrid kaha jata hain , jaha ek se zyada inheritance ke techniques ko use kiya jata hain.
class BaseClass :
    pass
class Derived1(BaseClass) :
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived1,Derived2):
    pass

# Hierarchial Inheritance :
# Bahut sari sub classes ek single base class se :
class Base :
    pass
class Heirarchy1(Base):
    pass
class Heirarchy2(Base):
    pass
# Yahan ek Parent class hain , usi se aur alag class derive kiye gaye hain joki as a subclass act karte hain base class ke.


# Implementation yahi hain, abh baki methods and all , normal same hi hain.
# Yeh bas terms hain jinhe yaad rakhna imp hain.