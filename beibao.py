import math

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

    # if cpu_memory_choose==0:    #cpu optimizer
    #     for i in range(len(cpu_chanege)):
    #         value.append(cpu_chanege[i])
    # if cpu_memory_choose==1:     #memory optimizer
    #     for i in range(len(cpu_chanege)):
    #         value.append(memory_change[i])
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
    print("memchaneg=",memory_change)    
    print("valuechage=",value)  
    servel=[]
    flavor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    full_computer=0
    full_cpu=full_cpu1
    full_memory=full_memory1

    b=1

    record=[0 for k in range(len(cpu_chanege))]
    fbest = [[[0 for col in range(input_list[1]+1)] for row in range(input_list[0]+1)] for i in range(len(cpu_chanege))]  #inti the 2 array list
    while(b>0):
        for  i in range(1,len(cpu_chanege),1):
            for j in range(1,full_cpu+1,1):
                for k in range(1,full_memory+1,1):

                    if cpu_chanege[i]<=j and memory_change[i]<=k:
                        fbest[i][j][k] = max(fbest[i-1][j][k] , fbest[i-1][j-cpu_chanege[i]][k-memory_change[i]] + value[i])
                    else: 
                        fbest[i][j][k] = fbest[i-1][j][k]   


            	

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
        # print(memory_change)
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
        a=len(cpu_chanege)
        for i in range(a):
            if record[i]==1:
                # print("i=",i)
                # print("cpu_change[i]=",cpu_chanege[i])
                del cpu_chanege[i]
                del memory_change[i]
                del value[i]
                cpu_chanege.insert(i,0)
                memory_change.insert(i,0)
                value.insert(i,0)
        # print(cpu_chanege)   
        # print(memory_change)    
        # print(value) 
        servel.append(flavor)
        full_computer+=1
        flavor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        record=[0 for k in range(len(cpu_chanege))]
        fbest = [[[0 for col in range(input_list[1]+1)] for row in range(input_list[0]+1)] for i in range(len(cpu_chanege))]
        full_cpu=full_cpu1
        full_memory=full_memory1
        c=0
        for i in range(len(cpu_chanege)):
        	c+=cpu_chanege[i]
        if c==0:
        	b=0
        print(full_computer)
    return servel


a=knapsack([0,0,0,40,40,40,40,0,0,0,20,0,0,0,0],[56,128],0)
print(a)

   