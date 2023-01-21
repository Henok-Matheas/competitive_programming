class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        this is a backtrack question definitely
        
        why because it is an enumeration question
        
        it wants us to enumerate the different ways we can split the string such that it's valid
        
        what makes it valid
        
        they can't have leading zeros meaning if you find a zero and it's the first then that bitch is the only thing in that part
        
        return the calid ip's
        
        
        one way do the dots by placing each part in a list of 4 lists
        
        and finally add a isvalid function to check if the thing is valid
        
        so how would this word?
        
        well the pointers tell us where the end is
        
        
        so we can have 4 loops
        
        for
            for
                for
                
                
        this makes it n cubed but the backtrack approach is??
        appending them into a stack
        """
        res = []
        
        def BT(i,address):
            
            if i==len(s):
                if len(address)==4:
                    res.append( '.'.join(map(str,address)) )
                return
            
            if address[-1]!=0 and address[-1]*10+int(s[i]) <= 255:
                lastItem = address[-1]
                address[-1] = lastItem*10+int(s[i])
                BT(i+1, address)
                address[-1] = lastItem
            
            if len(address)<4:
                BT(i+1,address + [int(s[i])])
        
        BT(1,[int(s[0])])
        return res