import re

def read_template():
    file = open("assets/content_game.txt",'r')
    content = file.read()
    return content  
#########################################
def parse_template(content):
  arr =[]
  curly =re.findall(r'\{.*?\}', content)
  for i in curly:
        arr.append(i.strip("{ }"))   
  return arr
#########################################
def merge(content , words):  
    return (re.sub(r'{[^}]*}','{}',content)).format(*words) 
#########################################
def copyFile_content(finalResult):
    print(finalResult)
    file = open('assets/result-game.txt','w')
    file.write(finalResult)
#########################################
if __name__ == "__main__":
   
    print("Welcome to Madlib Game :\nwe will asked you to input some words to play this game!")
    content = read_template()
    arr = parse_template(content)
    words=[]
    for i in range(len(arr)):
        words.append(input("Enter a {} ".format(arr[i])))
    finalResult = merge(content, words)
    copyFile_content(finalResult)
