import click
click.clear()

class Stack:
    def __init__(self):
        self.stack = [None for i in range(27)]

    def push(self, val):
        if val == " ":
            self.stack[26] = val
        else:
            val = val.lower()
            self.stack[ord(val)-97] = val

    def pop(self):
        self.stack.remove(self.stack[self.length-1])

    def clear(self):
        self.__init__()

    def check(self, val):
        if val == " ":
            return(self.stack[26] == None)
        val = val.lower()
        return (self.stack[ord(val)-97] == None)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwwkew
        st = Stack()
        count = 0
        max = 0
        
        for i in s:
            if st.check(i):
                count += 1
                st.push(i)
                print(i)
                print(st.stack)
                print(count)
                print()
            else:
                if count>max:
                    max = count
                count = 0
                st.clear()
                count += 1
                st.push(i)
        
        return max if max>=count else count

if __name__ == '__main__':
    s = input("Enter: ") or "dvdf"
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))