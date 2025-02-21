name="Nithin"
surName="Jukuri"
result=name+" "+surName
print(f"after conactinating: {result}")
print(f"length: {len(result)}")
print(f"UPPER CASE: {result.upper()}")
print(f"lower case: {result.lower()}")
print(result)
new_text=result.replace(" ","_" )
print("modified text: ",new_text)   
words=result.split()
print("words: ",words)
text="        it has space around it      "
print("stripped text: ",text.strip())
if "Ni" in result:
    print("substring is present")

arn="arn:aws:iam:1234567:user/john"
print("To get the user name: ",arn.split("/")[1])
print("power **: ",2**2)