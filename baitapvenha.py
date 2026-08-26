from abc import ABC,abstractmethod
class Pet(ABC):
    def __init__(self,ten):
        self._ten=ten
    @abstractmethod
    def make_sound(self):
        pass
    @property
    def ten(self):
        return self._ten
    @ten.setter
    def ten(self,value):
        self._ten= value
class conCho(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con chó tên: ",self._ten,"kêu",self._sound)
class conMeo(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con mèo kêu",self._sound)
class conGa(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con gà kêu",self._sound)
class conTho(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sounda
    def make_sound(self):
        print("con thỏ kêu",self._sound)
class conRan(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con rắn kêukêu",self._sound)
class conKhi(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con khỉ kêukêu",self._sound)
class conBo(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con bò kêukêu",self._sound)
class conTacKe(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con tắc kèkè kêu",self._sound)
class conChuot(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con chuột kêu",self._sound)
class conCuu(Pet):
    def __init__(self,ten,sound):
        super().__init__(ten)
        self._sound=sound
    def make_sound(self):
        print("con cừu kêu",self._sound)
a=conCho("Nam","hè hè")
print(a.make_sound())