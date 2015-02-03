# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:45:15 2015

@author: Alec
"""

def tokenizeString(inputString, size, tokenStream):
    i = 0    
    while i < (size - 1):
        currentChar = inputString[i];
        if(currentChar == '~'):
            tokenStream.append("NOT")
            
        elif(currentChar == '&'):
            tokenStream.append("AND")
            
        elif(currentChar == '|'):
            tokenStream.append("OR")
            
        elif(currentChar == '='):
            tokenStream.append("CONDITIONAL")
            i += 2
            
        elif(currentChar == '<'): 
            tokenStream.append("BICONDITIONAL")
            i += 3
            
        elif(currentChar == '('):
            tokenStream.append("LPAREN")
            
        elif(currentChar == ')'):
            tokenStream.append("RPAREN") 
       
        elif(currentChar == 't'):
            tokenStream.append("TRUE") 
            i += 4
        
        elif(currentChar == 'f'):
            tokenStream.append("FALSE") 
            i += 5
            
        elif(currentChar == ' '):
            i = i
        
        else:
            tokenStream.append("INVALID")
        
        i += 1             
        
def removeInvalids(tokenStream):  
    temp = []
    for item in tokenStream:
        if item != 'INVALID':
            temp.append(item)
    return temp
          
def main():
    TextParse = open('TextParse.txt')
    for line in TextParse:
        tokenStream = []
        size = len(line)
        tokenizeString(line, size, tokenStream)
        #tokenStream = removeInvalids(tokenStream)
        print tokenStream
    
    
if __name__ == "__main__":
    main()
   
    