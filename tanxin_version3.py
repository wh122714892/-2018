import math

def knapsack_version3(Vm_list,input_lines,cpu_memory_choose): 
    
    # cpu = int(input_lines[0].split( )[0])   
    # mem = int(input_lines[0].split( )[1])
    # input_list = []
    # input_list.append(cpu)
    # input_list.append(mem)
    # cpu_memory_choose = 0
    # if input_lines[-4].strip() = 'MEM':
    #     cpu_memory_choose = 1

    #cpu_memory_choose 1 for memory optimizer ,else is cpu optimition 
    full_cpu1 = input_lines[0]       #every servel has the number of cpu
    full_memory1 = input_lines[1]   #every servel has the number of memory

    cpu_chanege11=[]    # the type of vmware memory/cpu =1:1
    memory_change11=[]
    cpu_chanege21=[]     # the type of vmware memory/cpu =2:1
    memory_change21=[]
    cpu_chanege41=[]      # the type of vmware memory/cpu =4:1
    memory_change41=[]
    
    servel=[]

####### for birth the 1:1 and 2:1 and 4:1 list

    for i in range(0,len(Vm_list),3):
        for j in range(Vm_list[i]):
            cpu_chanege11.append(int(math.pow(2,i/3)))        
            memory_change11.append(int(math.pow(2,i/3)))

    for i in range(1,len(Vm_list),3):
        for j in range(Vm_list[i]):
            cpu_chanege21.append(int(math.pow(2,(i-1)/3)))        
            memory_change21.append(int(2*math.pow(2,(i-1)/3)))

    for i in range(2,len(Vm_list),3):
        for j in range(Vm_list[i]):
            cpu_chanege41.append(int(math.pow(2,(i-2)/3)))        
            memory_change41.append(int(4*math.pow(2,(i-2)/3)))
    
    cpu_chanege11.reverse()
    memory_change11.reverse()
    cpu_chanege21.reverse()
    memory_change21.reverse()
    cpu_chanege41.reverse()
    memory_change41.reverse()
    # print(cpu_chanege11)
    # print(memory_change11)
    # print(cpu_chanege21)
    # print(memory_change21)
    # print(cpu_chanege41)
    # print(memory_change41)
   
 
    flavor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    full_computer=0
    full_cpu=full_cpu1
    full_memory=full_memory1
    nowpos=0
    nowpos21=0
    nowpos41=0
    flag=0 
    flag1=0 
    while (len(cpu_chanege11)+len(cpu_chanege21)+len(cpu_chanege41))>0:
        while (nowpos+nowpos21+nowpos41) < (len(cpu_chanege11)+len(cpu_chanege21)+len(cpu_chanege41)):      # nowpos present the now location 
            print("------------")
            print("cpu_chanege11=")
            print(len(cpu_chanege11))
            print("cpu_change21=")
            print(len(cpu_chanege21))
            print("cpu_change41=")
            print(len(cpu_chanege41))
            print("------------")
            print("cpu=%d",full_cpu)
            print("memory=%d",full_memory)
            
            if  full_cpu==0 or full_memory==0:
                break
            else:
                if  full_memory/(full_cpu*1.0)<1.5:       # use 1:1 then 2:1 then 4:1
                    print("111")
                    #decide weather the n can put into servel
                      
                    if len(cpu_chanege11)>0 and nowpos<len(cpu_chanege11) and 0<=(full_cpu - cpu_chanege11[nowpos]) and 0<=(full_memory-memory_change11[nowpos]):
                        full_cpu-=cpu_chanege11[nowpos]
                        full_memory-=memory_change11[nowpos]

                        if cpu_chanege11[nowpos] ==1 and memory_change11[nowpos]==1:
                            flavor[0]+=1;
                        
                        if cpu_chanege11[nowpos] ==2 and memory_change11[nowpos]==2:
                            flavor[3]+=1;
                       
                        if cpu_chanege11[nowpos] ==4 and memory_change11[nowpos]==4:
                            flavor[6]+=1;
                       
                        if cpu_chanege11[nowpos] ==8 and memory_change11[nowpos]==8:
                            flavor[9]+=1;
                       
                        if cpu_chanege11[nowpos] ==16 and memory_change11[nowpos]==16:
                            flavor[12]+=1;
                                   
                        
                        del cpu_chanege11[nowpos]
                        del memory_change11[nowpos]

                    else:
                        nowpos = nowpos +1 ;  

                    
                    if  nowpos>=len(cpu_chanege11) and len(cpu_chanege21)>0 and nowpos21<len(cpu_chanege21) and 0<=(full_cpu - cpu_chanege21[nowpos21]) and 0<=(full_memory-memory_change21[nowpos21]):
                        full_cpu-=cpu_chanege21[nowpos21]
                        full_memory-=memory_change21[nowpos21]

                        if cpu_chanege21[nowpos21] ==1 and memory_change21[nowpos21]==2:
                            flavor[1]+=1;
                        
                        if cpu_chanege21[nowpos21] ==2 and memory_change21[nowpos21]==4:
                            flavor[4]+=1;
                       
                        if cpu_chanege21[nowpos21] ==4 and memory_change21[nowpos21]==8:
                            flavor[7]+=1;
                       
                        if cpu_chanege21[nowpos21] ==8 and memory_change21[nowpos21]==16:
                            flavor[10]+=1;
                       
                        if cpu_chanege21[nowpos21] ==16 and memory_change21[nowpos21]==32:
                            flavor[13]+=1;
                                   
                        
                        del cpu_chanege21[nowpos21]
                        del memory_change21[nowpos21] 

                    else:
                        nowpos21 = nowpos21 + 1            
                                  
                    if  nowpos>=len(cpu_chanege11) and nowpos21 >= len(cpu_chanege21) and len(cpu_chanege41)>0  and nowpos41<len(cpu_chanege41) and 0<=(full_cpu - cpu_chanege41[nowpos41]) and 0<=(full_memory-memory_change41[nowpos41]):
                        full_cpu-=cpu_chanege41[nowpos41]
                        full_memory-=memory_change41[nowpos41]

                        if cpu_chanege41[nowpos41] ==1 and memory_change41[nowpos41]==4:
                            flavor[2]+=1;
                        
                        if cpu_chanege41[nowpos41] ==2 and memory_change41[nowpos41]==8:
                            flavor[5]+=1;
                       
                        if cpu_chanege41[nowpos41] ==4 and memory_change41[nowpos41]==16:
                            flavor[8]+=1;
                       
                        if cpu_chanege41[nowpos41] ==8 and memory_change41[nowpos41]==32:
                            flavor[11]+=1;
                       
                        if cpu_chanege41[nowpos41] ==16 and memory_change41[nowpos41]==64:
                            flavor[14]+=1;
                                   
                        
                        del  cpu_chanege41[nowpos41]
                        del  memory_change41[nowpos41]    

                    else:
                          
                          nowpos41 = nowpos41 +1 ;           #turn to the next position
     
      
      #########use 2:1 first ,then 1:1, then  4:1 
                elif  full_memory/(full_cpu*1.0)<2 and full_memory/(full_cpu*1.0)>=1.5:      
                    print("222")
                   #decide weather the n can put into servel
                    if len(cpu_chanege21)>0 and nowpos21<len(cpu_chanege21) and 0<=(full_cpu - cpu_chanege21[nowpos21]) and 0<=(full_memory-memory_change21[nowpos21]):
                        full_cpu-=cpu_chanege21[nowpos21]
                        full_memory-=memory_change21[nowpos21]

                        if cpu_chanege21[nowpos21] ==1 and memory_change21[nowpos21]==2:
                            flavor[1]+=1;
                        
                        if cpu_chanege21[nowpos21] ==2 and memory_change21[nowpos21]==4:
                            flavor[4]+=1;
                       
                        if cpu_chanege21[nowpos21] ==4 and memory_change21[nowpos21]==8:
                            flavor[7]+=1;
                       
                        if cpu_chanege21[nowpos21] ==8 and memory_change21[nowpos21]==16:
                            flavor[10]+=1;
                       
                        if cpu_chanege21[nowpos21] ==16 and memory_change21[nowpos21]==32:
                            flavor[13]+=1;
                                   
                        
                        del cpu_chanege21[nowpos21]
                        del memory_change21[nowpos21]

                    else:
                        nowpos21 = nowpos21 +1    


                    if  nowpos21>=len(cpu_chanege21) and len(cpu_chanege11)>0  and nowpos<len(cpu_chanege11) and 0<=(full_cpu - cpu_chanege11[nowpos-len(cpu_chanege21)]) and 0<=(full_memory-memory_change11[nowpos-len(cpu_chanege21)]):
                        full_cpu-=cpu_chanege11[nowpos-len(cpu_chanege21)]
                        full_memory-=memory_change11[nowpos-len(cpu_chanege21)]

                        if cpu_chanege11[nowpos-len(cpu_chanege21)] ==1 and memory_change11[nowpos-len(cpu_chanege21)]==1:
                            flavor[0]+=1;
                        
                        if cpu_chanege11[nowpos-len(cpu_chanege21)] ==2 and memory_change11[nowpos-len(cpu_chanege21)]==2:
                            flavor[3]+=1;
                       
                        if cpu_chanege11[nowpos-len(cpu_chanege21)] ==4 and memory_change11[nowpos-len(cpu_chanege21)]==4:
                            flavor[6]+=1;
                       
                        if cpu_chanege11[nowpos-len(cpu_chanege21)] ==8 and memory_change11[nowpos-len(cpu_chanege21)]==8:
                            flavor[9]+=1;
                       
                        if cpu_chanege11[nowpos-len(cpu_chanege21)] ==16 and memory_change11[nowpos-len(cpu_chanege21)]==16:
                            flavor[12]+=1;
                                   
                        
                        del cpu_chanege11[nowpos-len(cpu_chanege21)]
                        del memory_change11[nowpos-len(cpu_chanege21)]

                    else:
                        nowpos+=1
                    
                             
                                  
                    if  nowpos>=len(cpu_chanege11) and nowpos21>=len(cpu_chanege21) and len(cpu_chanege41)>0 and nowpos41<len(cpu_chanege41)  and 0<=(full_cpu - cpu_chanege41[nowpos41]) and 0<=(full_memory-memory_change41[nowpos41]):
                        full_cpu-=cpu_chanege41[nowpos41]
                        full_memory-=memory_change41[nowpos41]

                        if cpu_chanege41[nowpos41] ==1 and memory_change41[nowpos41]==4:
                            flavor[2]+=1;
                        
                        if cpu_chanege41[nowpos41] ==2 and memory_change41[nowpos41]==8:
                            flavor[5]+=1;
                       
                        if cpu_chanege41[nowpos41] ==4 and memory_change41[nowpos41]==16:
                            flavor[8]+=1;
                       
                        if cpu_chanege41[nowpos41] ==8 and memory_change41[nowpos41]==32:
                            flavor[11]+=1;
                       
                        if cpu_chanege41[nowpos41] ==16 and memory_change41[nowpos41]==64:
                            flavor[14]+=1;
                                   
                        
                        del cpu_chanege41[nowpos41]
                        del memory_change41[nowpos41]    

                    else:
                          
                          nowpos41 = nowpos41 +1 ;           #turn to the next position



        #########use 2:1 first ,then 4:1, then  1:1 
                elif  full_memory/(full_cpu*1.0)<3 and full_memory/(full_cpu*1.0)>=2:      
                    print("333")
                   #decide weather the n can put into servel
                    # print("------cpu_changeddddddd")
                    # print(cpu_chanege21)
                    # print("-------cpu_changeddddddd")
                    if  len(cpu_chanege21)>0 and nowpos21<len(cpu_chanege21) and 0<=(full_cpu - cpu_chanege21[nowpos21]) and 0<=(full_memory-memory_change21[nowpos21]):
                        full_cpu-=cpu_chanege21[nowpos21]
                        full_memory-=memory_change21[nowpos21]

                        if cpu_chanege21[nowpos21] ==1 and memory_change21[nowpos21]==2:
                            flavor[1]+=1;
                        
                        if cpu_chanege21[nowpos21] ==2 and memory_change21[nowpos21]==4:
                            flavor[4]+=1;
                       
                        if cpu_chanege21[nowpos21] ==4 and memory_change21[nowpos21]==8:
                            flavor[7]+=1;
                       
                        if cpu_chanege21[nowpos21] ==8 and memory_change21[nowpos21]==16:
                            flavor[10]+=1;
                       
                        if cpu_chanege21[nowpos21] ==16 and memory_change21[nowpos21]==32:
                            flavor[13]+=1;
                                   
                        
                        del cpu_chanege21[nowpos21]
                        del memory_change21[nowpos21]
                    else:
                        nowpos21+=1    

                  
                    if  nowpos21 >=len(cpu_chanege21) and len(cpu_chanege41)>0  and  nowpos41<len(cpu_chanege41) and  0<=(full_cpu - cpu_chanege41[nowpos41]) and 0<=(full_memory-memory_change41[nowpos41]):
                        full_cpu-=cpu_chanege41[nowpos41]
                        full_memory-=memory_change41[nowpos41]

                        if cpu_chanege41[nowpos41] ==1 and memory_change41[nowpos41]==4:
                            flavor[2]+=1;
                        
                        if cpu_chanege41[nowpos41] ==2 and memory_change41[nowpos41]==8:
                            flavor[5]+=1;
                       
                        if cpu_chanege41[nowpos41] ==4 and memory_change41[nowpos41]==16:
                            flavor[8]+=1;
                       
                        if cpu_chanege41[nowpos41] ==8 and memory_change41[nowpos41]==32:
                            flavor[11]+=1;
                       
                        if cpu_chanege41[nowpos41] ==16 and memory_change41[nowpos41]==64:
                            flavor[14]+=1;
                                   
                        
                        del cpu_chanege41[nowpos41]
                        del memory_change41[nowpos41] 
                    else:
                        nowpos41+=1   

                    if  nowpos21>=len(cpu_chanege21) and nowpos41>=len(cpu_chanege41) and len(cpu_chanege11)>0  and nowpos<len(cpu_chanege11) and 0<=(full_cpu - cpu_chanege11[nowpos]) and 0<=(full_memory-memory_change11[nowpos]):
                        full_cpu-=cpu_chanege11[nowpos-len(cpu_chanege41)-len(cpu_chanege21)]
                        full_memory-=memory_change11[nowpos-len(cpu_chanege41)-len(cpu_chanege21)]

                        if cpu_chanege11[nowpos] ==1 and memory_change11[nowpos]==1:
                            flavor[0]+=1;
                        
                        if cpu_chanege11[nowpos] ==2 and memory_change11[nowpos]==2:
                            flavor[3]+=1;
                       
                        if cpu_chanege11[nowpos] ==4 and memory_change11[nowpos]==4:
                            flavor[6]+=1;
                       
                        if cpu_chanege11[nowpos] ==8 and memory_change11[nowpos]==8:
                            flavor[9]+=1;
                       
                        if cpu_chanege11[nowpos] ==16 and memory_change11[nowpos]==16:
                            flavor[12]+=1;
                                   
                        
                        del cpu_chanege11[nowpos]
                        del memory_change11[nowpos]
                    

                    else:
                          
                          nowpos = nowpos +1 ;           #turn to the next position

            #########use 4:1 first ,then 2:1, then  1:1 
                elif  full_memory/(full_cpu*1.0)>=3 :      
                    print("444")
                   #decide weather the n can put into servel
                    if len(cpu_chanege41)>0 and nowpos41<len(cpu_chanege41) and 0<=(full_cpu - cpu_chanege41[nowpos41]) and 0<=(full_memory-memory_change41[nowpos41]):
                        full_cpu-=cpu_chanege41[nowpos41]
                        full_memory-=memory_change41[nowpos41]

                        if cpu_chanege41[nowpos41] ==1 and memory_change41[nowpos41]==4:
                            flavor[2]+=1;
                        
                        if cpu_chanege41[nowpos41] ==2 and memory_change41[nowpos41]==8:
                            flavor[5]+=1;
                       
                        if cpu_chanege41[nowpos41] ==4 and memory_change41[nowpos41]==16:
                            flavor[8]+=1;
                       
                        if cpu_chanege41[nowpos41] ==8 and memory_change41[nowpos41]==32:
                            flavor[11]+=1;
                       
                        if cpu_chanege41[nowpos41] ==16 and memory_change41[nowpos41]==64:
                            flavor[14]+=1;
                                   
                        
                        del cpu_chanege41[nowpos41]
                        del memory_change41[nowpos41]  
                    else:
                        nowpos41+=1  

                  
                    if  nowpos41>=len(cpu_chanege41) and len(cpu_chanege21)>0 and nowpos21<len(cpu_chanege21) and 0<=(full_cpu - cpu_chanege21[nowpos21]) and 0<=(full_memory-memory_change21[nowpos21]):
                        full_cpu-=cpu_chanege21[nowpos21]
                        full_memory-=memory_change21[nowpos21]

                        if cpu_chanege21[nowpos21] ==1 and memory_change21[nowpos21]==2:
                            flavor[1]+=1;
                        
                        if cpu_chanege21[nowpos21] ==2 and memory_change21[nowpos21]==4:
                            flavor[4]+=1;
                       
                        if cpu_chanege21[nowpos21] ==4 and memory_change21[nowpos21]==8:
                            flavor[7]+=1;
                       
                        if cpu_chanege21[nowpos21] ==8 and memory_change21[nowpos21]==16:
                            flavor[10]+=1;
                       
                        if cpu_chanege21[nowpos21] ==16 and memory_change21[nowpos21]==32:
                            flavor[13]+=1;
                                   
                        
                        del cpu_chanege21[nowpos21]
                        del memory_change21[nowpos21] 
                    else:
                        nowpos+=1   

                    if  nowpos21>=len(cpu_chanege21) and nowpos41>=len(cpu_chanege41) and len(cpu_chanege11)>0  and nowpos<len(cpu_chanege11)  and  0<=(full_cpu - cpu_chanege11[nowpos]) and 0<=(full_memory-memory_change11[nowpos]):
                        full_cpu-=cpu_chanege11[nowpo]
                        full_memory-=memory_change11[nowpos]

                        if cpu_chanege11[nowpos] ==1 and memory_change11[nowpos]==1:
                            flavor[0]+=1;
                        
                        if cpu_chanege11[nowpos] ==2 and memory_change11[nowpos]==2:
                            flavor[3]+=1;
                       
                        if cpu_chanege11[nowpos] ==4 and memory_change11[nowpos]==4:
                            flavor[6]+=1;
                       
                        if cpu_chanege11[nowpos] ==8 and memory_change11[nowpos]==8:
                            flavor[9]+=1;
                       
                        if cpu_chanege11[nowpos] ==16 and memory_change11[nowpos]==16:
                            flavor[12]+=1;
                                   
                        
                        del cpu_chanege11[nowpos]
                        del memory_change11[nowpos]
                    

                    else:
                        nowpos = nowpos +1 ;           #turn to the next position
                else:
                    break

        servel.append(flavor)
        full_computer=full_computer+1   
        print("第几台数")
        print(full_computer)
        print(servel)                       #one computer is over

        flavor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        full_cpu = full_cpu1
        full_memory = full_memory1
            
        nowpos = 0
        nowpos21 = 0
        nowpos41 = 0

    print(full_computer)
    return  servel



a=knapsack_version3([10,10,10,10,10,0,10,0,0,0,10,0,0,0,10],[56,128],1)
print(a)


