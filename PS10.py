#!/usr/bin/env python
# coding: utf-8

# In[3]:


class MoonLight :
    def main( args):
        # Open the input and output files
        file1 = open("inputPS10.txt","r") 
        file2 = open("outputPS10.txt","w") 
        # Getting the number of Test cases from the input file
        t = int(file1.readline())

        for i in range(t):
            
            counts = file1.readline()
            counts_split = counts.split()

            # Getting the number of boys from the input file
            m = int(counts_split[0])
            # Getting the number of girls from the input file
            n = int(counts_split[1])
            
            boys = [0] * (m)
            girls = [0] * (n)

            # Getting the individual height for boys and converting the same into a list of integers
            m_values = file1.readline()
            m_values_split = m_values.split()
            for j in range(m):
                boys[j] = int(m_values_split[j])

            # Getting the individual height for boys and converting the same into a list of integers
            n_values = file1.readline()
            n_values_split = n_values.split()
            for k in range(n):
                girls[k] = int(n_values_split[k])
            
            # Write NO into the output file when the number of girls is less than boys
            if (n < m) :
                print("NO")
                file2.write("NO \n")
            # Else check if each boy has a matching girl such that height of the girl is less than boy
            else :
                # Get the heights in sorted fashion
                boys = MoonLight.sortHeight(boys, 200)
                girls = MoonLight.sortHeight(girls, 200)
                
                girlForEachBoy = True
                
                # Check the height of individual boy to that of the girl
                for l in range(m):
                    if boys[l] <= girls[l]:
                        girlForEachBoy = False
                    
                if (girlForEachBoy) :
                    print("YES")
                    file2.write("YES \n")
                    
                else :
                    print("NO")
                    file2.write("NO \n")
                    
        file1.close()
        file2.close()

    # Fucntion to sort the height based on input and the maximum number of values that can be considered
    def sortHeight(input, maxValue):
        freq = [0] * (maxValue + 1)

        i = 0
        while (i < len(input)):
            freq[input[i]] += 1
            i += 1

        totalCount = 0
        i = 0
        while (i <= maxValue):
            oldCount = freq[i]
            freq[i] = totalCount

            totalCount += oldCount
            i += 1

        output = [0] * (len(input))
        i = 0
        while (i < len(input)):
            output[freq[input[i]]] = input[i]
            freq[input[i]] += 1
            i += 1

        return output
    

if __name__=="__main__":
    MoonLight.main([])


# In[ ]:




