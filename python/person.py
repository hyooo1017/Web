# 설계도 개념 -> 이 설계도를 바탕으로 사람을 만들 수 있음
class Person():                 # 클래스 (집단)
    name = '사람의 고유한 속성'   # 멤버 변수 (속성)
    age = '출생 이후부터 현재까지의 기간'

    def greeting(self):         # 멤버 메서드 (행동)
        print(f'{self.name}가 인사합니다. 안녕하세요.')

    def eating(self):
        print(f'{self.name}은(는) 밥을 먹고 있습니다.')

hyo = Person()                  # 인스턴스

print(hyo.name)                 # 인스턴스 생성 후 name 등 class의 멤버 변수는 인스턴스 변수라고도 불림
print(hyo.age)

hyo.name = 'hyo'
hyo.age = '27'

print(hyo.name)
print(hyo.age)

hyo.greeting()                  # 인스턴스 생성 후 greeting 등 class의 멤버 메서드는 인스턴스 메서드라고도 불림
