# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:44:41 2020

@author: madhu
"""
#
#*******************************************************************************/
##include <stdio.h>
#int main(){
#    char array[]="aabbbdddaaaa";
#    char k[20]="a";
#    int a,j=0;
#    for(a=0;a<(sizeof(array)-1);a++)
#    {
#        
#        if(array[a]!=array[a+1])
#        {
#            k[j]=array[a];
#            j++;
#        }
#        else 
#        continue;
#        
#        
#    }
#    printf("%s",k);
#    return 0;
#}
#k=[]
# =============================================================================
# 
# =============================================================================
#def duplicity(array):
#    for a in array:
#        if a != a:
#            append.k(a)
#           
#        else:
#            continue;
#    print(k)
#     
#array=["adjasjsdjas"]
#k=array.split()
#print(k)
#duplicity(array)


string="Enter string:10938183"
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)