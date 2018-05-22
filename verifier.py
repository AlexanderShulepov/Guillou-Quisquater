class Verifier:
    def __init__(self,open_key):
       self.n=open_key["n"]
       self.b=open_key["b"]
       self.v=open_key["v"]
       self.y=None
       self.x=None
       self.e=None

    def to_challenge(self):
        import random
        self.e=random.randint(1,self.b-1)
        return self.e

    def verify(self):
        if self.x==(pow(self.y,self.b,self.n) * pow(self.v,self.e,self.n) )%self.n:
            return True
        else:
            return False