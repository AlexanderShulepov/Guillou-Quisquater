

from prover import *
from verifier import *

def lab():
    P=Prover()

    V=Verifier(P.open_key)

    V.x=P.to_witness()

    P.e=V.to_challenge()

    V.y=P.to_answer()

    print(V.verify())

lab()



	