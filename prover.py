from mr import mr as generate_simple
from sugar import *
class Prover:
    def __init__(self):
       self.generate_params()

    def generate_b(self):
        phi=(self.__p-1)*(self.__q-1)
        while True:
            b=generate_simple()
            if gcd(b,phi):
                self.b=b
                return

    def generate_u(self):
        import random
        return random.randint(3,(self.__p*self.__q)-1)

    def generate_params(self):
        self.__p=generate_simple()
        self.__q=generate_simple()
        self.generate_b()
        self.__u=self.generate_u()
        self.n=self.__p*self.__q
        self.v=pow( inverse_of(self.__u,self.n), self.b, self.n)#v=u**(-1)**b(mod n)
        self.open_key={"n":self.n,"v":self.v,"b":self.b}
        
        self.e=None
        self.y=None
        self.r=None

    def to_witness(self):
      import random
      self.r=random.randint(2,self.__q*self.__p)
      return pow(self.r, self.b, self.n)
    
    def to_answer(self):
        self.y=(pow(self.__u,self.e,self.n)*self.r)%self.n#+1
        return self.y