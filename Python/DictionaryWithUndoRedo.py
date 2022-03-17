# asked in outreach IO
# you have a dictionary object, with get, set and delete functionality
# you need to enhance its functionality with undo/redo capability
'''
example:
set("a", 1)
set("b", 2)
set("a", 3)

undo() --> should reset the state of dictionary to be {"a":1, "b":2}
undo() --> should make dictionary to be {"a":1}
redo() --> should add back "b" key => {"a":1, "b":2}
notice that we can only call redo if undo is called already
'''
class Solution():
    def __init__(self):
        self.dic = dict()
        # define 2 stacks
        self.undo = []
        self.redo = []
    
    def getx(self, key):
        if key in self.dic.keys():
            return self.dic[key]
        return None
    
    def setx(self, key, val):
        if key in self.dic.keys() and ("set", key, self.dic[key]) not in self.undo:
            self.undo.append(("set", key, self.dic[key]))
        
        self.dic[key] = val
        if ("set", key, val) not in self.undo: 
            self.undo.append(("set", key, val))
    
    def delete(self, key):
        if key not in self.dic.keys():
            return
        
        print(f"deleting item with key: {key}")

        if ("del", key, self.dic[key]) not in self.undo:
            self.undo.append(("del", key, self.dic[key]))
        
        val = self.dic[key]

        del self.dic[key]
        return key, val
    
    def _undo(self):
        if len(self.undo) <= 0:
            return

        print("performing undo...")
        op = self.undo.pop()
        # add this last operation to redo
        self.redo.append(op)
        if op[0] == "set":
            key = op[1]
            # find the last value corresponding to the key and set it in the dictionary
            val = None
            for o in self.undo:
                if o[0] == "set" and o[1] == key:
                    val = o[2]
            
            self.dic[key] = val

        elif op[0] == "del":
            self.setx(op[1], op[2])
        else:
            raise Error("not valid operation")
    
    def _redo(self):
        if len(self.redo) <= 0:
            return

        print("performing redo...")
        op = self.redo.pop()
        # add this last operation to undo
        self.undo.append(op)

        if op[0] == "set":
            key = op[1]
            val = op[2]
            self.dic[key] = val

        elif op[0] == "del":
            key = op[1]
            del self.dic[key]

        else:
            raise Error("not valid operation")

    def print(self):
        print()
        print("-" * 100)
        print(f"undo stack is {self.undo}")
        print(f"redo stack is {self.redo}")
        print("printing dictionary...")
        for k,v in self.dic.items():
            print(f"key is {k} and val is {v}")

s = Solution()

s.setx("a", 1)
s.setx("b", 10)
s.setx("a", 2)
s.setx("c", 100)
s.setx("a", 3)
s.setx("a", 3)
s.setx("d", 1000)
s.print()

s.delete("a")
s.print()

s._undo()
s.print()

s._redo()
s.print()

s._undo()
s.print()

s._redo()
s.print()

s._redo()
s.print()

s._undo()
s.print()

s._undo()
s.print()

s._undo()
s.print()

s._undo()
s.print()

s._undo()
s.print()

s._undo()
s.print()

s.setx("a", 3)
s.setx("a", 4)
# this causes a problem, need to figure this part out -- in the end the result for a should be 3, but it will show 4
# why? because 3 was already added before and we check in the setx function, if the tuple is already added - then we don't add it again
s.setx("a", 3) 
s.setx("a", 2)

s._undo()
s.print()
