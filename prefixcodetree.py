import binascii

class Tree (object):
    def _init_(this, codeword = '' , symbol = None):
        this.codeword = codeword
        this.symbol = symbol

class PrefixCodeTree:
    def _init_(self):
        this.tree = {}

        def insert(this, codeword, symbol):
            index = 0
            for i in range(len(codeword)):
                index = index * 2 + codeword[i] + 1
                
            this.tree[str(index)] = Tree(codeword,symbol)    