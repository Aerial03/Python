# 상속
# 공통요소를 부모클래스에 한번만 정의할 수 있음
# 코드의 중복을 줄일 수 있음
# 함수 재지정(overriding) - 다형성
class Super(object): #상속 사용 문법
    # def __init__(self):
    #     pass
    def super_function(self):
        print('부모의 소유함수 - super_function')

    def sayEcho(self, name):
        return name+"님, 즐거운 코딩해요"

class Sub(Super):
    # def __init__(self):
    #     pass
    def sub_function(self):
        print('본인 소유함수 - sub_function')
    def sayEcho(self, name):
        return name+"님, 즐거운 코딩!!"

# 인스턴스 생성구문
child = Sub()
child.super_function()
child.sub_function()
print('print - ', child.sayEcho('jslim')) #자식 클래스에 없으면 부모, 부모에 없으면 object로 올라감

parent = Super()
parent.super_function()
# parent.sub_function() - 부모타입으로 자식 소유의 구성요소에 접근 불가
print()

#self(인스턴스 소유), super(부모 지칭)
class Unit(object):
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.__damage = damage
        self.__life = life
    def status(self):
        return '타입: {}\t공격력: {}\t생명력: {}'.format(self.utype, self.__damage, self.__life)
    def attack(self):
        pass
    #set, get
    def setDamage(self, damage):
        self.__damage = damage
    def setLife(self, life):
        self.__life = life
    def getDamage(self):
        return self.__damage
    def getLife(self):
        return self.__life

class Marine(Unit):
    def __init__(self, damage, life, offenseUp, defenseUp):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.offenseUp = offenseUp
        self.defenseUp = defenseUp
    def status(self):
        return super().status()+'\t공격력 업: {}\t방어력 업: {}'.format(self.offenseUp, self.defenseUp)
    def attack(self):
        print('마린이 공격을 시작합니다.')
    def stimPack(self):
        if self.getLife() > 40:
            print('stimPack을 사용합니다.')
            super().setDamage(super().getDamage() * 1.5)
            super().setLife(super().getLife() - 10)
        else:
            print('체력이 낮아서 stimPack을 사용할 수 없습니다.')

class Medic(Unit):
    def __init__(self, damage, life, defenseUp):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.defenseUp = defenseUp
    def status(self):
        return super().status()+'\t방어력 업:{}'.format(self.defenseUp)
    def attack(self):
        print('메딕이 마린을 치료합니다.')

unit = Unit(100, 100)
print('info - ', unit.status())
marine = Marine(100, 100, 50, 50)
print('marine info - ', marine.status())
marine.attack()
marine.stimPack()
print('marine info - ', marine.status())
print()
medic = Medic(0, 100, 0)
print('medic info - ', medic.status())
print()

unit_lst = [marine, medic]
for u in unit_lst:
    print(u.utype)
    print('unit info - ',u.status())
print()

print('[marine과 medic을 이동시키는 수송기 Unit 설계]')
class DropShip(Unit):
    def __init__(self,damage,life):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.unitlst = []
    def board(self, crew):
        self.unitlst.append(crew)
    # isinstance(): 타입체크가 가능하다.
    def drop(self):
        for u in self.unitlst:
            if isinstance(u, Marine):
                u.stimPack()
            else:
                u.attack()
    def move(self):
        print('병력을 이동시킵니다.')

print('DropShip 생성')
ship = DropShip(0, 100)
print('info - ', ship.status())
print('부대원 이동을 위해서 DropShip에 승선시킨다.')
ship.board(marine)
ship.board(medic)
ship.move()
print('부대원을 타겟지점에 낙하시킨다.')
ship.drop()
print('전투종료 후 상태확인')
print('info - ', marine.status())
print('info - ', medic.status())

# 다중 상속 및 추상클래스
# 추상화 - 클래스가 추상함수를 가질 수 있도록 하여
# 자식에서 반드시 오버라이딩하도록 하는 방법

from abc import *
class Animal(object, metaclass=ABCMeta): #추상클래스
    @abstractmethod                      #추상클래스
    def cry(self):
        pass
    def nonAbstractMethod(self):
        print('추상클래스에 정의된 일반 메서드입니다.')
class Tiger:
    def cry(self):
        print('어흥')
class Lion:
    def cry(self):
        print('어허흥')
class Liger(Lion, Tiger):
    pass

# liger = Liger()
# liger.cry()

# animal = Animal()
tiger = Tiger()