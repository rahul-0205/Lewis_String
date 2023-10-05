# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
st,i,rev=[],0,''
while i<len(s):
  if not st:
    st.append(s[i])
  elif st and s[i]==')':
    while st[-1]!='(':
      rev+=st.pop()
      #print(st)
    st.pop()
    c=len(rev)
    for j in rev:
      st.append(j)
      
    rev=''
  else:
    st.append(s[i])
  i+=1
print(''.join(st))
