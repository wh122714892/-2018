import math
import time

def knapsack(Vm_list,input_list,cpu_memory_choose):    
    # cpu = int(input_lines[0].split( )[0])   
    # mem = int(input_lines[0].split( )[1])
    # input_list = []
    # input_list.append(cpu)
    # input_list.append(mem)
    # cpu_memory_choose = 0
    # if input_lines[-4].strip() = 'MEM':
    #     cpu_memory_choose = 1


    full_cpu1 = input_list[0]        #every servel has the number of cpu
    full_memory1 = input_list[1]     #every servel has the number of memory
    cpu_chanege=[]
    memory_change=[]
    value = []
    all_data=0
    for i in range(len(Vm_list)):
        all_data =all_data +Vm_list[i]
        for j in range(Vm_list[i]):
            if i == 0:  
                cpu_chanege.append(1)
                memory_change.append(1)
                value.append(2)
            if i == 1:
                cpu_chanege.append(1)
                memory_change.append(2)
                value.append(3)
            if i == 2:
                cpu_chanege.append(1)
                memory_change.append(4)
                value.append(5)
            if i == 3:
                cpu_chanege.append(2)
                memory_change.append(2)
                value.append(4)
            if i == 4:
                cpu_chanege.append(2)
                memory_change.append(4)
                value.append(6)
            if i == 5:
                cpu_chanege.append(2)
                memory_change.append(8)
                value.append(10)
            if i == 6:
                cpu_chanege.append(4)
                memory_change.append(4)
                value.append(8)
            if i == 7:
                cpu_chanege.append(4)
                memory_change.append(8)
                value.append(12)
            if i == 8:
                cpu_chanege.append(4)
                memory_change.append(16)
                value.append(20)
            if i == 9:
                cpu_chanege.append(8)
                memory_change.append(8)
                value.append(16)
            if i == 10:
                cpu_chanege.append(8)
                memory_change.append(16)
                value.append(24)
            if i == 11:
                cpu_chanege.append(8)
                memory_change.append(32)
                value.append(40)
            if i == 12:
                cpu_chanege.append(16)
                memory_change.append(16)
                value.append(32)
            if i == 13:
                cpu_chanege.append(16)
                memory_change.append(32)
                value.append(48)
            if i == 14:
                cpu_chanege.append(16)
                memory_change.append(64)
                value.append(80)


    cpu_chanege.reverse()
    memory_change.reverse()
    value.reverse()
    if(cpu_memory_choose==1):
        for i1 in range(len(memory_change)-1):
            for j1 in range(len(memory_change)-1-i1):
                if memory_change[j1] < memory_change[j1+1]:
                    memory_change[j1], memory_change[j1+1] = memory_change[j1+1], memory_change[j1] 
                    cpu_chanege[j1], cpu_chanege[j1+1] = cpu_chanege[j1+1], cpu_chanege[j1]
                    value[j1], value[j1+1] = value[j1+1],value[j1]

    cpu_chanege.insert(0,0)
    memory_change.insert(0,0)
    value.insert(0,0)
    # print(cpu_chanege)   
    # print("memchaneg=",memory_change)    
    # print("valuechage=",value)  
    servel=[]
    flavor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    full_computer=0
    full_cpu=full_cpu1
    full_memory=full_memory1

    b=1
    record=[0 for k in range(len(cpu_chanege))]
    fbest = [[[0 for col in range(input_list[1]+1)] for row in range(input_list[0]+1)] for i in range(len(cpu_chanege))]  #inti the 2 array list
    while(len(cpu_chanege)>1):
        
        start_time=time.time()
        for  i in range(1,len(cpu_chanege),1):
            for j in range(1,full_cpu+1,1):
                for k in range(1,full_memory+1,1):

                    if cpu_chanege[i]<=j and memory_change[i]<=k:
                        fbest[i][j][k] = max(fbest[i-1][j][k] , fbest[i-1][j-cpu_chanege[i]][k-memory_change[i]] + value[i])
                    else: 
                        fbest[i][j][k] = fbest[i-1][j][k]   
        end_time=time.time()
        #print('time: ',end_time-start_time)

            	

        #print("all=",fbest[len(cpu_chanege)-1][full_cpu1][full_memory1])

        for i in range(len(cpu_chanege)-1,1,-1):
            
            if fbest[i][full_cpu][full_memory]==fbest[i-1][full_cpu][full_memory]:
                record[i] =0;
            
            else:
          	    #print("222222222222")
          	    record[i]=1;
          	    full_cpu -= cpu_chanege[i];
          	    full_memory -= memory_change[i];

          	
        if fbest[1][full_cpu][full_memory]>0:
    	    record[1]=1   
    	              
        # print(record)
        # print(cpu_chanege)
        #print(memory_change)
        for i in range(len(cpu_chanege)):
            if record[i]==1:

                if cpu_chanege[i] ==1 and memory_change[i]==1:
                    flavor[0]+=1;
                if cpu_chanege[i] ==1 and memory_change[i]==2:
                    flavor[1]+=1;
                if cpu_chanege[i] ==1 and memory_change[i]==4:
                    flavor[2]+=1;
                if cpu_chanege[i] ==2 and memory_change[i]==2:
                    flavor[3]+=1;
                if cpu_chanege[i] ==2 and memory_change[i]==4:
                    flavor[4]+=1;
                if cpu_chanege[i] ==2 and memory_change[i]==8:
                    flavor[5]+=1;
                if cpu_chanege[i] ==4 and memory_change[i]==4:
                    flavor[6]+=1;
                if cpu_chanege[i] ==4 and memory_change[i]==8:
                    flavor[7]+=1;
                if cpu_chanege[i] ==4 and memory_change[i]==16:
                    flavor[8]+=1;
                if cpu_chanege[i] ==8 and memory_change[i]==8:
                    flavor[9]+=1;
                if cpu_chanege[i] ==8 and memory_change[i]==16:
                    flavor[10]+=1;
                if cpu_chanege[i] ==8 and memory_change[i]==32:
                    flavor[11]+=1;
                if cpu_chanege[i] ==16 and memory_change[i]==16:
                    flavor[12]+=1;
                if cpu_chanege[i] ==16 and memory_change[i]==32:
                    flavor[13]+=1;
                if cpu_chanege[i] ==16 and memory_change[i]==64:
                    flavor[14]+=1;                          

        # print("record=",record)
        # print("flavor=",flavor)
        nowpos=0
        #print("record==",record)
        while nowpos<len(cpu_chanege):
            if record[nowpos]==1:
                
                #print(nowpos)
                del cpu_chanege[nowpos]
                del memory_change[nowpos]
                del value[nowpos]
                del record[nowpos]

            else:
                nowpos+=1
        #start_time=time.time()
        k=0
        cpu_all=0
        memory_all=0
        for cpu_types in range(5):             # cal least servel
            for memory_types in range(3):
                cpu_all=cpu_all + math.pow(2,cpu_types)*flavor[k]
                memory_all=memory_all + math.pow(2,cpu_types)*math.pow(2,memory_types)*flavor[k]
                k+=1
        # print("flavor=",flavor)
        # print("use of cpu=",100*cpu_all/full_cpu1)
        # print("use of mem=",100*memory_all/full_memory1)   
        cpu_reserve = full_cpu1 - cpu_all
        memory_reserve = full_memory1 - memory_all
        
        if cpu_memory_choose==1 and cpu_reserve>0 and memory_reserve>0:      # cpu optimizer
            #rate = memory_reserve/cpu_reserve
            #if rate>=3:
                for i in range(14,2,-3):
                    while Vm_list[i]!=0 and  math.pow(2,(i-2)/3) <= cpu_reserve and  math.pow(2,(i-2)/3)*4 <= memory_reserve:
                        cpu_reserve = cpu_reserve - math.pow(2,(i-2)/3)
                        memory_reserve = memory_reserve - math.pow(2,(i-2)/3)*4
                        flavor[i]+=1
                for i in range(13,1,-3):
                    while Vm_list[i]!=0 and  math.pow(2,(i-1)/3) <= cpu_reserve and  math.pow(2,(i-1)/3)*2 <= memory_reserve:
                        cpu_reserve = cpu_reserve - math.pow(2,(i-1)/3)
                        memory_reserve = memory_reserve - math.pow(2,(i-1)/3)*2
                        flavor[i]+=1
                for i in range(12,0,-3):
                    while Vm_list[i]!=0 and  math.pow(2,i/3) <= cpu_reserve and  math.pow(2,i/3) <= memory_reserve:
                        cpu_reserve = cpu_reserve - math.pow(2,i/3)
                        memory_reserve = memory_reserve - math.pow(2,i/3)
                        flavor[i]+=1
           
        if cpu_memory_choose==0 and cpu_reserve>0 and memory_reserve>0:         
         
                for i in range(12,0,-3):
                    while Vm_list[i]!=0 and  math.pow(2,i/3) <= cpu_reserve and  math.pow(2,i/3) <= memory_reserve:
                        cpu_reserve = cpu_reserve - math.pow(2,i/3)
                        memory_reserve = memory_reserve - math.pow(2,i/3)
                        flavor[i]+=1

                while i in range(13,1,-3):
                    while Vm_list[i]!=0 and  math.pow(2,(i-1)/3) <= cpu_reserve and  math.pow(2,(i-1)/3)*2 <= memory_reserve:
                        cpu_reserve = cpu_reserve - math.pow(2,(i-1)/3)
                        memory_reserve = memory_reserve - math.pow(2,(i-1)/3)*2
                        flavor[i]+=1
                
                while i in range(14,2,-3):
                    while Vm_list[i]!=0 and  math.pow(2,(i-2)/3) <= cpu_reserve and  math.pow(2,(i-2)/3)*4 <= memory_reserve:
                        cpu_reserve = cpu_reserve - math.pow(2,(i-2)/3)
                        memory_reserve = memory_reserve - math.pow(2,(i-2)/3)*4
                        flavor[i]+=1
        #end_time = time.time()
        #print('time:',end_time - start_time)       
        # cpu_all=0
        # memory_all=0
        # k=0
        # for cpu_types in range(5):             # cal least servel
        #     for memory_types in range(3):
        #         cpu_all=cpu_all + math.pow(2,cpu_types)*flavor[k]
        #         memory_all=memory_all + math.pow(2,cpu_types)*math.pow(2,memory_types)*flavor[k]
        #         k+=1
        # print("add to cpu=",100*cpu_all/full_cpu1)
        # print("add to mem=",100*memory_all/full_memory1)   
        # print(memory_change)    
        # print(value) 
        # print("meme=",memory_change)
        # print("len(cpu)=",len(cpu_chanege))
        #if cpu_memory_choose==0 and 0.5<(cpu_all/(full_cpu1*1.0)):
        servel.append(flavor)
        full_computer+=1
        
        flavor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        record=[0 for k in range(len(cpu_chanege))]
        fbest = [[[0 for col in range(input_list[1]+1)] for row in range(input_list[0]+1)] for i in range(len(cpu_chanege))]
        full_cpu=full_cpu1
        full_memory=full_memory1
        # c=0
        # for i in range(len(cpu_chanege)):
        # 	c+=cpu_chanege[i]
        # if c==0:
        # 	b=0
        print(full_computer)
    return servel


a=knapsack([125,88,0,0,75,31,0,112,33,0,31,32,0,0,0],[56,128],1)

print(a)

   