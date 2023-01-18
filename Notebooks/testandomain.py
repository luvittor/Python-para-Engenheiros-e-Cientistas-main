# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:46:11 2023

@author: luvit
"""
   
def funcao2():
    print('funcao2')
    print(__name__)
        
    if __name__== "__main__":
        print("este codigo esta sendo executado diretamente")
    else:
        print("este codigo esta sendo chamado como modulo")
        print(__name__)


funcao2()