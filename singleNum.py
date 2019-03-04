class Sol:
    def singleNum(self,arr):
        return 2*sum(set(arr))-sum(arr)
p1=Sol()
print(p1.singleNum([1,3,1]))
