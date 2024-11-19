
class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        st = []
        for c in S:
            if c >= '0' and c <= '9':
                st.append(int(c))
                
            elif c == '*':
                num1 = st.pop()
                num2 = st.pop()
                res = num2 * num1
                st.append(res)
                
            elif c == '/':
                num1 = st.pop()
                num2 = st.pop()
                res = num2 / num1
                st.append(int(res))
                
            elif c == '+':
                num1 = st.pop()
                num2 = st.pop()
                res = num2 + num1
                st.append(res)
                
            else:
                num1 = st.pop()
                num2 = st.pop()
                res = num2 - num1
                st.append(res)
                
        return st[-1]
