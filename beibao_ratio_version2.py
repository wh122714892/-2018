import math
import time
import copy
import random
def multi_knapsack_veersion2(vm_list,input_list):
    # cpu = int(input_lines[0].split( )[0])   
    # mem = int(input_lines[0].split( )[1])
    # input_list = []
    # input_list.append(cpu)
    # input_list.append(mem)
    # cpu_memory_choose = 0
    # if input_lines[-4].strip() = 'MEM':
    #     cpu_memory_choose = 1

    # input_list  = []

    # input_list.append([int(input_lines[3].split( )[1]),int(input_lines[3].split( )[2])])
    # input_list.append([int(input_lines[1].split( )[1]),int(input_lines[1].split( )[2])])
    # input_list.append([int(input_lines[2].split( )[1]),int(input_lines[2].split( )[2])]) 


    full_cpu11 = input_list[0][0]        #every High-Performance servel has the number of cpu
    full_memory11 = input_list[0][1]     #every High-Performance servel has the number of memory

    full_cpu21 = input_list[1][0]        #every normal servel has the number of cpu
    full_memory21 = input_list[1][1]     #every normal servel has the number of memory

    full_cpu41 = input_list[2][0]        #every Large-Memory servel has the number of cpu
    full_memory41 = input_list[2][1]     #every Large-Memory servel has the number of memory

    cpu_chanege11=[]    # the type of vmware memory/cpu =1:1
    memory_change11=[]
    cpu_chanege21=[]     # the type of vmware memory/cpu =2:1
    memory_change21=[]
    cpu_chanege41=[]      # the type of vmware memory/cpu =4:1
    memory_change41=[]
    value11 = []
    value21 = []
    value41 = []



    for i in range(0,len(vm_list),3):
        for j in range(vm_list[i]):
            cpu_chanege11.append(int(math.pow(2,i/3)))         # cpu_chanege11 stand for the High-Performance servel
            memory_change11.append(int(math.pow(2,i/3)))
            value11.append(int(2*math.pow(2,i/3)))

    for i in range(1,len(vm_list),3):
        for j in range(vm_list[i]):
            cpu_chanege21.append(int(math.pow(2,(i-1)/3)))         #cpu_chanege21 stand for the normal servel
            memory_change21.append(int(2*math.pow(2,(i-1)/3)))
            value21.append(int(3*math.pow(2,(i-1)/3)))

    for i in range(2,len(vm_list),3):
        for j in range(vm_list[i]):
            cpu_chanege41.append(int(math.pow(2,(i-2)/3)))        #cpu_chanege21 stand for the Large-Memory
            memory_change41.append(int(4*math.pow(2,(i-2)/3)))
            value41.append(int(5*math.pow(2,(i-2)/3)))
    
    
    cpu_chanege11.reverse()
    cpu_all11=sum(cpu_chanege11)
    memory_change11.reverse()
    mem_all11=sum(memory_change11)
    value11.reverse()

    cpu_chanege21.reverse()
    cpu_all21=sum(cpu_chanege21)
    memory_change21.reverse()
    mem_all21=sum(memory_change21)
    value21.reverse()

    cpu_chanege41.reverse()
    cpu_all41=sum(cpu_chanege41)
    memory_change41.reverse()
    mem_all41=sum(memory_change41)
    value41.reverse()

    # print("41=",cpu_chanege41)
    # print("gggggg",value41)
    ###################calc alll ratio of all mem/cpu
    #print("mem/cpu=",(mem_all11+mem_all21+mem_all41)/(cpu_all11+cpu_all21+cpu_all41))

    ################### vrey important (give data to 4:1 and 1:1 from 2:1  to make the ratio much more rational)
    nowpos=0
    while cpu_all41>0   and nowpos<len(cpu_chanege21) and len(cpu_chanege21)>0 and (mem_all41/(cpu_all41*1.0)) > (input_list[2][1]/(1.0*input_list[2][0])):
        if (mem_all41+memory_change41[nowpos])/(1.0*(cpu_all41+cpu_chanege41[nowpos])) < (input_list[2][1]/(1.0*input_list[2][0])):
            nowpos+=1
        else:
            mem_all41+=memory_change21[nowpos]
            cpu_all41+=cpu_chanege21[nowpos]
            memory_change41.append(memory_change21[nowpos])
            cpu_chanege41.append(cpu_chanege21[nowpos])
            value41.append(value21[nowpos])
            del memory_change21[nowpos]
            del cpu_chanege21[nowpos]
            del value21[nowpos]
    
    # for i1 in range(len(memory_change41)-1):
    #     for j1 in range(len(memory_change41)-1-i1):
    #         if cpu_chanege41[j1] < cpu_chanege41[j1+1]:
    #             cpu_chanege41[j1], cpu_chanege41[j1+1] = cpu_chanege41[j1+1], cpu_chanege41[j1] 
    #             memory_change41[j1], memory_change41[j1+1] = memory_change41[j1+1], memory_change41[j1]
    #             value41[j1], value41[j1+1] = value41[j1+1], value41[j1]
    # print(cpu_chanege41)
    # print(memory_change41)
    # print(value41)
    #print("mem41/cpu41=",(sum(memory_change41))/(sum(cpu_chanege41)))
    nowpos=0
    while  cpu_all11>0  and  nowpos<len(cpu_chanege21) and len(cpu_chanege21)>0 and (mem_all11/(cpu_all11*1.0)) < (input_list[0][1]/(1.0*input_list[0][0])):
        if (mem_all11+memory_change11[nowpos])/(1.0*(cpu_all11+cpu_chanege11[nowpos])) > (input_list[0][1]/(1.0*input_list[0][0])):
            nowpos+=1
        else:
            mem_all11+=memory_change21[nowpos]
            cpu_all11+=cpu_chanege21[nowpos]
            memory_change11.append(memory_change21[nowpos])
            cpu_chanege11.append(cpu_chanege21[nowpos])
            value11.append(value21[nowpos])
            del memory_change21[nowpos]
            del cpu_chanege21[nowpos]
            del value21[nowpos]
    ####################   add  the first 0  for the start from position 1 
    cpu_chanege11.insert(0,0)
    memory_change11.insert(0,0)
    value11.insert(0,0)

    cpu_chanege21.insert(0,0)
    memory_change21.insert(0,0)
    value21.insert(0,0)

    cpu_chanege41.insert(0,0)
    memory_change41.insert(0,0)
    value41.insert(0,0)
    # print(cpu_chanege)   
    # print("memchaneg=",memory_change)    
    # print("valuechage=",value)  
    servel=[]   # the all  servel
    servel11=[]  # the use of High-Performance servel、
    servel111=[]
    servel11.append("10")  #High-Performance servel
    servel21=[]  # the use of normal servel
    servel21.append("00")  #normal servel
    servel211=[]
    servel41=[]  # the use of Large-Memory servel
    servel41.append("01") #Large-Memory servel
    servel411=[]
    flavor11=[0 for i in range(18)]
    flavor21=[0 for i in range(18)]
    flavor41=[0 for i in range(18)]
    full_computer11=0  #the amount of used High-Performance servel
    full_computer21=0
    full_computer41=0
    temp_full_cpu11=full_cpu11     #located variable
    temp_full_memory11=full_memory11
    temp_full_cpu21=full_cpu21
    temp_full_memory21=full_memory21
    temp_full_cpu41=full_cpu41
    temp_full_memory41=full_memory41

    
    record11=[0 for k in range(len(cpu_chanege11))]
    record21=[0 for k in range(len(cpu_chanege21))]
    record41=[0 for k in range(len(cpu_chanege41))]
    fbest11 = [[[0 for col in range(input_list[0][1]+1)] for row in range(input_list[0][0]+1)] for i in range(len(cpu_chanege11))]  #inti the 2 array list
    fbest21 = [[[0 for col in range(input_list[1][1]+1)] for row in range(input_list[1][0]+1)] for i in range(len(cpu_chanege21))]
    fbest41 = [[[0 for col in range(input_list[2][1]+1)] for row in range(input_list[2][0]+1)] for i in range(len(cpu_chanege41))]
    
    servel_cpu_memory_remain11=[]
    servel_cpu_memory_remain111=[]
    servel_cpu_memory_remain11.append("10")   #cpu
    servel_cpu_memory_remain21=[]
    servel_cpu_memory_remain211=[]
    servel_cpu_memory_remain21.append("00")   #normal
    servel_cpu_memory_remain41=[]
    servel_cpu_memory_remain411=[]
    servel_cpu_memory_remain41.append("01")   #mem
    servel_cpu_memory_remain=[]
    reserve_cpu_mem=[]
    while(len(cpu_chanege11)>1):
        
        #start_time=time.time()
        for  i in range(1,len(cpu_chanege11),1):
            for j in range(1,full_cpu11+1,1):
                for k in range(1,full_memory11+1,1):

                    if cpu_chanege11[i]<=j and memory_change11[i]<=k:
                        fbest11[i][j][k] = max(fbest11[i-1][j][k] , fbest11[i-1][j-cpu_chanege11[i]][k-memory_change11[i]] + value11[i])
                    else: 
                        fbest11[i][j][k] = fbest11[i-1][j][k]   
        #end_time=time.time()
        #print('time: ',end_time-start_time)

            	

        #print("all=",fbest[len(cpu_chanege)-1][full_cpu1][full_memory1])

        for i in range(len(cpu_chanege11)-1,1,-1):
            
            if fbest11[i][temp_full_cpu11][temp_full_memory11]==fbest11[i-1][temp_full_cpu11][temp_full_memory11]:
                record11[i] =0;
            
            else:
          	    #print("222222222222")
          	    record11[i]=1;
          	    temp_full_cpu11 -= cpu_chanege11[i];
          	    temp_full_memory11 -= memory_change11[i];

          	
        if fbest11[1][temp_full_cpu11][temp_full_memory11]>0:
    	    record11[1]=1   
    	              
        # print(record)
        # print(cpu_chanege)
        #print(memory_change)
        single_servel_cpu=full_cpu11
        single_servel_mem=full_memory11
        for i in range(len(cpu_chanege11)):
            if record11[i]==1:

                if cpu_chanege11[i] ==1 and memory_change11[i]==1:
                    flavor11[0]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=1
                if cpu_chanege11[i] ==1 and memory_change11[i]==2:
                    flavor11[1]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=2
                if cpu_chanege11[i] ==1 and memory_change11[i]==4:
                    flavor11[2]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=4
                if cpu_chanege11[i] ==2 and memory_change11[i]==2:
                    flavor11[3]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=2
                if cpu_chanege11[i] ==2 and memory_change11[i]==4:
                    flavor11[4]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=4
                if cpu_chanege11[i] ==2 and memory_change11[i]==8:
                    flavor11[5]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=8
                if cpu_chanege11[i] ==4 and memory_change11[i]==4:
                    flavor11[6]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=4
                if cpu_chanege11[i] ==4 and memory_change11[i]==8:
                    flavor11[7]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=8
                if cpu_chanege11[i] ==4 and memory_change11[i]==16:
                    flavor11[8]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=16
                if cpu_chanege11[i] ==8 and memory_change11[i]==8:
                    flavor11[9]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=8
                if cpu_chanege11[i] ==8 and memory_change11[i]==16:
                    flavor11[10]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=16
                if cpu_chanege11[i] ==8 and memory_change11[i]==32:
                    flavor11[11]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=32
                if cpu_chanege11[i] ==16 and memory_change11[i]==16:
                    flavor11[12]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=16
                if cpu_chanege11[i] ==16 and memory_change11[i]==32:
                    flavor11[13]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=32
                if cpu_chanege11[i] ==16 and memory_change11[i]==64:
                    flavor11[14]+=1 
                    single_servel_cpu-=16
                    single_servel_mem-=64
                if cpu_chanege11[i] ==32 and memory_change11[i]==32:
                    flavor11[15]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=32
                if cpu_chanege11[i] ==32 and memory_change11[i]==64:
                    flavor11[16]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=64
                if cpu_chanege11[i] ==32 and memory_change11[i]==128:
                    flavor11[17]+=1 
                    single_servel_cpu-=32
                    single_servel_mem-=128                          

        # print("record=",record)
        # print("flavor11=",flavor11)
        # print("single_=",single_servel_cpu)
        # print("memme=",single_servel_mem)

        reserve_cpu_mem.append(single_servel_cpu)
        reserve_cpu_mem.append(single_servel_mem)
        servel_cpu_memory_remain111.append(copy.deepcopy(reserve_cpu_mem))
        # print("reswewww=",reserve_cpu_mem)
        del reserve_cpu_mem[0]
        del reserve_cpu_mem[0]
        
        nowpos=0
        #print("record==",record)
        while nowpos<len(cpu_chanege11):
            if record11[nowpos]==1:
                
                #print(nowpos)
                del cpu_chanege11[nowpos]
                del memory_change11[nowpos]
                del value11[nowpos]
                del record11[nowpos]

            else:
                nowpos+=1


        servel111.append(flavor11)
        full_computer11+=1
        
        flavor11=[0 for i in range(18)]
        record11=[0 for k in range(len(cpu_chanege11))]
        fbest11 = [[[0 for col in range(input_list[0][1]+1)] for row in range(input_list[0][0]+1)] for i in range(len(cpu_chanege11))]
        temp_full_cpu11=full_cpu11
        temp_full_memory11=full_memory11
        print("full_computer11=",full_computer11)
    servel_cpu_memory_remain11.append(servel_cpu_memory_remain111)
    servel_cpu_memory_remain.append(servel_cpu_memory_remain11)
    servel11.append(servel111)
    servel.append(servel11)
    
    

    #############  calc  the  flavor41

    while(len(cpu_chanege41)>1):
        
        #start_time=time.time()
        for  i in range(1,len(cpu_chanege41),1):
            for j in range(1,full_cpu41+1,1):
                for k in range(1,full_memory41+1,1):

                    if cpu_chanege41[i]<=j and memory_change41[i]<=k:
                        fbest41[i][j][k] = max(fbest41[i-1][j][k] , fbest41[i-1][j-cpu_chanege41[i]][k-memory_change41[i]] + value41[i])
                    else: 
                        fbest41[i][j][k] = fbest41[i-1][j][k]   

        for i in range(len(cpu_chanege41)-1,1,-1):
            
            if fbest41[i][temp_full_cpu41][temp_full_memory41]==fbest41[i-1][temp_full_cpu41][temp_full_memory41]:
                record41[i] =0;
            
            else:
                #print("222222222222")
                record41[i]=1;
                temp_full_cpu41 -= cpu_chanege41[i];
                temp_full_memory41 -= memory_change41[i];

            
        if fbest41[1][temp_full_cpu41][temp_full_memory41]>0:
            record41[1]=1   
                      
        # print(record)
        # print(cpu_chanege)
        #print(memory_change)
        single_servel_cpu=full_cpu41
        single_servel_mem=full_memory41
        for i in range(len(cpu_chanege41)):
            if record41[i]==1:

                if cpu_chanege41[i] ==1 and memory_change41[i]==1:
                    flavor41[0]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=1
                if cpu_chanege41[i] ==1 and memory_change41[i]==2:
                    flavor41[1]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=2
                if cpu_chanege41[i] ==1 and memory_change41[i]==4:
                    flavor41[2]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=4
                if cpu_chanege41[i] ==2 and memory_change41[i]==2:
                    flavor41[3]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=2
                if cpu_chanege41[i] ==2 and memory_change41[i]==4:
                    flavor41[4]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=4
                if cpu_chanege41[i] ==2 and memory_change41[i]==8:
                    flavor41[5]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=8
                if cpu_chanege41[i] ==4 and memory_change41[i]==4:
                    flavor41[6]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=4
                if cpu_chanege41[i] ==4 and memory_change41[i]==8:
                    flavor41[7]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=8
                if cpu_chanege41[i] ==4 and memory_change41[i]==16:
                    flavor41[8]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=16
                if cpu_chanege41[i] ==8 and memory_change41[i]==8:
                    flavor41[9]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=8
                if cpu_chanege41[i] ==8 and memory_change41[i]==16:
                    flavor41[10]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=16
                if cpu_chanege41[i] ==8 and memory_change41[i]==32:
                    flavor41[11]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=32
                if cpu_chanege41[i] ==16 and memory_change41[i]==16:
                    flavor41[12]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=16
                if cpu_chanege41[i] ==16 and memory_change41[i]==32:
                    flavor41[13]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=32
                if cpu_chanege41[i] ==16 and memory_change41[i]==64:
                    flavor41[14]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=64 
                if cpu_chanege41[i] ==32 and memory_change41[i]==32:
                    flavor41[15]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=32
                if cpu_chanege41[i] ==32 and memory_change41[i]==64:
                    flavor41[16]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=64
                if cpu_chanege41[i] ==32 and memory_change41[i]==128:
                    flavor41[17]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=128                          

        # print("record=",record)
        # print("flavor11=",flavor11)
        # print("single41_=",single_servel_cpu)
        # print("memme41=",single_servel_mem)
        reserve_cpu_mem.append(single_servel_cpu)
        reserve_cpu_mem.append(single_servel_mem)
        servel_cpu_memory_remain411.append(copy.deepcopy(reserve_cpu_mem))
        del reserve_cpu_mem[0]
        del reserve_cpu_mem[0]
        
        nowpos=0
        #print("record==",record)
        while nowpos<len(cpu_chanege41):
            if record41[nowpos]==1:
                
                #print(nowpos)
                del cpu_chanege41[nowpos]
                del memory_change41[nowpos]
                del value41[nowpos]
                del record41[nowpos]

            else:
                nowpos+=1

        servel411.append(flavor41)
        full_computer41+=1
        
        flavor41=[0 for i in range(18)]
        record41=[0 for k in range(len(cpu_chanege41))]
        fbest41 = [[[0 for col in range(input_list[2][1]+1)] for row in range(input_list[2][0]+1)] for i in range(len(cpu_chanege41))]
        temp_full_cpu41=full_cpu41
        temp_full_memory41=full_memory41
        print("full_computer41=",full_computer41)
    servel_cpu_memory_remain41.append(servel_cpu_memory_remain411)
    servel_cpu_memory_remain.append(servel_cpu_memory_remain41)
    servel41.append(servel411)
    servel.append(servel41)
     
    # print("servel=",servel)
    # print("servel_cpu_mem_remain=",servel_cpu_memory_remain)
    nowpos=1
    while nowpos<len(cpu_chanege21):
        for i in range(1,-1,-1):
            if  len(servel_cpu_memory_remain[i][1])>0:
                for j in range(len(servel_cpu_memory_remain[i][1])-1,-1,-1):
                    if nowpos<len(cpu_chanege21)  and servel_cpu_memory_remain[i][1][j][0]-cpu_chanege21[nowpos]>=0 and servel_cpu_memory_remain[i][1][j][1]-memory_change21[nowpos]>=0:
                        while nowpos<len(cpu_chanege21) and servel_cpu_memory_remain[i][1][j][0]-cpu_chanege21[nowpos]>=0 and servel_cpu_memory_remain[i][1][j][1]-memory_change21[nowpos]>=0:
                            #print("nowpos=",nowpos)
                            servel_cpu_memory_remain[i][1][j][0]-=cpu_chanege21[nowpos]
                            servel_cpu_memory_remain[i][1][j][1]-=memory_change21[nowpos]

                            if cpu_chanege21[nowpos] ==1 and memory_change21[nowpos]==1:
                                servel[i][1][j][0]+=1
                                
                            if cpu_chanege21[nowpos] ==1 and memory_change21[nowpos]==2:
                                servel[i][1][j][1]+=1
                                
                            if cpu_chanege21[nowpos] ==1 and memory_change21[nowpos]==4:
                                servel[i][1][j][2]+=1
                                
                            if cpu_chanege21[nowpos] ==2 and memory_change21[nowpos]==2:
                                servel[i][1][j][3]+=1
                                
                            if cpu_chanege21[nowpos] ==2 and memory_change21[nowpos]==4:
                                servel[i][1][j][4]+=1
                                
                            if cpu_chanege21[nowpos] ==2 and memory_change21[nowpos]==8:
                                servel[i][1][j][5]+=1
                                
                            if cpu_chanege21[nowpos] ==4 and memory_change21[nowpos]==4:
                                servel[i][1][j][6]+=1
                                
                            if cpu_chanege21[nowpos] ==4 and memory_change21[nowpos]==8:
                                servel[i][1][j][7]+=1
                                
                            if cpu_chanege21[nowpos] ==4 and memory_change21[nowpos]==16:
                                servel[i][1][j][8]+=1
                                
                            if cpu_chanege21[nowpos] ==8 and memory_change21[nowpos]==8:
                                servel[i][1][j][9]+=1
                                
                            if cpu_chanege21[nowpos] ==8 and memory_change21[nowpos]==16:
                                servel[i][1][j][10]+=1
                                
                            if cpu_chanege21[nowpos] ==8 and memory_change21[nowpos]==32:
                                servel[i][1][j][11]+=1
                                
                            if cpu_chanege21[nowpos] ==16 and memory_change21[nowpos]==16:
                                servel[i][1][j][12]+=1
                                
                            if cpu_chanege21[nowpos] ==16 and memory_change21[nowpos]==32:
                                servel[i][1][j][13]+=1
                                
                            if cpu_chanege21[nowpos] ==16 and memory_change21[nowpos]==64:
                                servel[i][1][j][14]+=1
                                 
                            if cpu_chanege21[nowpos] ==32 and memory_change21[nowpos]==32:
                                servel[i][1][j][15]+=1
                                
                            if cpu_chanege21[nowpos] ==32 and memory_change21[nowpos]==64:
                                servel[i][1][j][16]+=1
                                
                            if cpu_chanege21[nowpos] ==32 and memory_change21[nowpos]==128:
                                servel[i][1][j][17]+=1
                            
                            del cpu_chanege21[nowpos]
                            del memory_change21[nowpos]
                            del value21[nowpos]
                    else: 
                        nowpos+=1
    
    print(servel_cpu_memory_remain)
     ########################################  check the use ratio of the last servel of high cpu and high mem 
    signal_servel_cpu=0
    signal_servel_mem=0
    for j in range(1,-1,-1):
        if j == 1:
            signal_servel_cpu=full_cpu41
            signal_servel_mem=full_memory41
            #print("hahhhh=",len(servel_cpu_memory_remain[j][1]))
        else:
            signal_servel_cpu=full_cpu11
            signal_servel_mem=full_memory11
            

        if  len(servel_cpu_memory_remain[j][1])>0:
            if (servel_cpu_memory_remain[j][1][len(servel[j][1])-1][0]/(signal_servel_cpu*1.0)) >0.15 or (servel_cpu_memory_remain[j][1][len(servel[j][1])-1][1]/(signal_servel_mem*1.0)) >0.15:
            
                k=0
                for cpu_types in range(6):             # cal least servel
                    for memory_types in range(3):
                        for i in range(servel[j][1][len(servel_cpu_memory_remain[j][1])-1][k]):
                            
                            cpu_chanege21.append(int(math.pow(2,cpu_types)))
                            memory_change21.append(int(math.pow(2,cpu_types)*math.pow(2,memory_types)))
                            value21.append(int(math.pow(2,cpu_types)*(1+math.pow(2,memory_types))))
                        k+=1
                del servel[j][1][len(servel[j][1])-1]
                del servel_cpu_memory_remain[j][1][len(servel_cpu_memory_remain[j][1])-1]
                if j==1:
                    full_computer41-=1
                else:
                    full_computer11-=1



    #########################################  remain   cpu_change21
    record21=[0 for k in range(len(cpu_chanege21))]
    fbest21 = [[[0 for col in range(input_list[1][1]+1)] for row in range(input_list[1][0]+1)] for i in range(len(cpu_chanege21))]
    while(len(cpu_chanege21)>1):
        
        #start_time=time.time()
        for  i in range(1,len(cpu_chanege21),1):
            for j in range(1,full_cpu21+1,1):
                for k in range(1,full_memory21+1,1):

                    if cpu_chanege21[i]<=j and memory_change21[i]<=k:
                        fbest21[i][j][k] = max(fbest21[i-1][j][k] , fbest21[i-1][j-cpu_chanege21[i]][k-memory_change21[i]] + value21[i])
                    else: 
                        fbest21[i][j][k] = fbest21[i-1][j][k]   
        #end_time=time.time()
        #print('time: ',end_time-start_time)

                

        #print("all=",fbest[len(cpu_chanege)-1][full_cpu1][full_memory1])

        for i in range(len(cpu_chanege21)-1,1,-1):
            
            if fbest21[i][temp_full_cpu21][temp_full_memory21]==fbest21[i-1][temp_full_cpu21][temp_full_memory21]:
                record21[i] =0;
            
            else:
                #print("222222222222")
                record21[i]=1;
                temp_full_cpu21 -= cpu_chanege21[i];
                temp_full_memory21 -= memory_change21[i];

            
        if fbest21[1][temp_full_cpu21][temp_full_memory21]>0:
            record21[1]=1   
                      
        # print(record)
        # print(cpu_chanege)
        #print(memory_change)
        single_servel_cpu=full_cpu21
        single_servel_mem=full_memory21
        for i in range(len(cpu_chanege21)):
            if record21[i]==1:

                if cpu_chanege21[i] ==1 and memory_change21[i]==1:
                    flavor21[0]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=1
                if cpu_chanege21[i] ==1 and memory_change21[i]==2:
                    flavor21[1]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=2
                if cpu_chanege21[i] ==1 and memory_change21[i]==4:
                    flavor21[2]+=1
                    single_servel_cpu-=1
                    single_servel_mem-=4
                if cpu_chanege21[i] ==2 and memory_change21[i]==2:
                    flavor21[3]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=2
                if cpu_chanege21[i] ==2 and memory_change21[i]==4:
                    flavor21[4]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=4
                if cpu_chanege21[i] ==2 and memory_change21[i]==8:
                    flavor21[5]+=1
                    single_servel_cpu-=2
                    single_servel_mem-=8
                if cpu_chanege21[i] ==4 and memory_change21[i]==4:
                    flavor21[6]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=4
                if cpu_chanege21[i] ==4 and memory_change21[i]==8:
                    flavor21[7]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=8
                if cpu_chanege21[i] ==4 and memory_change21[i]==16:
                    flavor21[8]+=1
                    single_servel_cpu-=4
                    single_servel_mem-=16
                if cpu_chanege21[i] ==8 and memory_change21[i]==8:
                    flavor21[9]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=8
                if cpu_chanege21[i] ==8 and memory_change21[i]==16:
                    flavor21[10]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=16
                if cpu_chanege21[i] ==8 and memory_change21[i]==32:
                    flavor21[11]+=1
                    single_servel_cpu-=8
                    single_servel_mem-=32
                if cpu_chanege21[i] ==16 and memory_change21[i]==16:
                    flavor21[12]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=16
                if cpu_chanege21[i] ==16 and memory_change21[i]==32:
                    flavor21[13]+=1
                    single_servel_cpu-=16
                    single_servel_mem-=32
                if cpu_chanege21[i] ==16 and memory_change21[i]==64:
                    flavor21[14]+=1 
                    single_servel_cpu-=16
                    single_servel_mem-=64
                if cpu_chanege21[i] ==32 and memory_change21[i]==32:
                    flavor21[15]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=32
                if cpu_chanege21[i] ==32 and memory_change21[i]==64:
                    flavor21[16]+=1
                    single_servel_cpu-=32
                    single_servel_mem-=64
                if cpu_chanege21[i] ==32 and memory_change21[i]==128:
                    flavor21[17]+=1 
                    single_servel_cpu-=32
                    single_servel_mem-=128                          

        # print("record=",record)
        # print("flavor11=",flavor11)
        # print("single21_=",single_servel_cpu)
        # print("memme21=",single_servel_mem)

        reserve_cpu_mem.append(single_servel_cpu)
        reserve_cpu_mem.append(single_servel_mem)
        servel_cpu_memory_remain21.append(copy.deepcopy(reserve_cpu_mem))
        #print("reswewww=",reserve_cpu_mem)
        del reserve_cpu_mem[0]
        del reserve_cpu_mem[0]
        
        nowpos=0
        #print("record==",record)
        while nowpos<len(cpu_chanege21):
            if record21[nowpos]==1:
                
                #print(nowpos)
                del cpu_chanege21[nowpos]
                del memory_change21[nowpos]
                del value21[nowpos]
                del record21[nowpos]

            else:
                nowpos+=1

        servel211.append(flavor21)
        full_computer21+=1
        
        flavor21=[0 for i in range(18)]
        record21=[0 for k in range(len(cpu_chanege21))]
        fbest21 = [[[0 for col in range(input_list[1][1]+1)] for row in range(input_list[1][0]+1)] for i in range(len(cpu_chanege21))]
        temp_full_cpu21=full_cpu21
        temp_full_memory21=full_memory21
        print("full_computer21=",full_computer21)
    servel_cpu_memory_remain.append(servel_cpu_memory_remain21)
    servel21.append(servel211)
    servel.append(servel21)

    #print("cpu21_shanchu=",cpu_chanege21)
    print(servel_cpu_memory_remain)
    cpu_all=0
    memory_all=0
    full_cpu=0
    full_memory=0
    k=0
    for cpu_types in range(6):             # cal least servel
        for memory_types in range(3):
            cpu_all=cpu_all + math.pow(2,cpu_types)*vm_list[k]
            memory_all=memory_all + math.pow(2,cpu_types)*math.pow(2,memory_types)*vm_list[k]
            k+=1
    full_cpu=full_cpu11*full_computer11+full_cpu21*full_computer21+full_cpu41*full_computer41
    full_memory=full_memory11*full_computer11+full_memory21*full_computer21+full_memory41*full_computer41
    print("ratio_cpu=",cpu_all/full_cpu)
    print("ratio_mem=",memory_all/full_memory)
    return servel

a=multi_knapsack_veersion2([100,100,0,0,100,100,0,100,100,0,100,100,0,0,0,0,0,0],[[112,192],[56,128],[84,256]])  

print(a)

##########  125,88,0,0,75,31,0,112,33,0,31,32,0,0,0,0,0,0