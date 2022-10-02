from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compression c or e for extract: ")
#@Author Jurijus pacalovas
class encypthion_class:

    def encypthion1(self):

                 
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                        
                    namea=""
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   
                    Times_compression=1
                    
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    F=0
                    
                    

                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                
                        size_after2=len(data)
                        #print(size_after2)  
                        
                        if len(data)==0 or len(data)>2**40:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        
                        lenf1=len(data)
                          
                    
                            
  
                            
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)

                                
                                    
                                
                                size_data3=size_data2
                                
                                size_data3="11111111"+size_data3
                                
                                long=len(size_data3)
                                
                                
                                number=int(size_data3,2)
                                
                                
                                info_hex=hex(number)[2:]
                        
                                string = info_hex
                                
                                #print(info_hex)
                                
                             
                                
                                #111111110
                                #11111110
                                #1111110
                                #111110
                                #11110
                                #1110
                                #110
                                #10
                                #0000
                                #0010
                                #0100
                                #0110
                                #1001
                                #1010
                                #1011
                                #1100
                                #1101
                                #1110
                                #01111
                                
                                
                                
 
                                lower="abcdef01"
                                upper="23456789"
 
                                res=""
                                res1=""
                               
                                for i in range(0,len(string)):
 
                                    if(i%2==0):
                                 
                                        if(string[i] in lower):
                                 
                                 
                                            res+="1"
                                            res+="0"*(lower.index(string[i])+1)
                                            
                                           
                                           
                                            
                                            
                                      
                                            
                                            
                                            
                                 
                                        else:
                                            
                                 
                                            #res+="0"*(upper.index(string[i])+1)
                                            res1+="0"*(upper.index(string[i])+1)
                                            long_res=len(res1)
                                            
                                            long_res=long_res-1
                                            b=format(long_res,'03b')
                                            if long_res==7:
                                                res+="01111"
                                            elif long_res<4:
                                                res+=b 
                                                res+="0"
                                            else:
                                                
                                                res+=b
                                                res+="1"
                                            res1=""
                                            
                                 
                                    else:
                                 
                                        if(string[i] in lower):
                                            
                                            res+="1"
                                 
                                            res+="0"*(lower.index(string[i])+1)
                                            
                                           
                                            
                                            
                                            
                                 
                                        else:
                                            
                                 
                                            #res+="0"*(upper.index(string[i])+1)          
                                            res1+="0"*(upper.index(string[i])+1)
                                            
                                            long_res=len(res1)
                                            long_res=long_res-1
                                            b=format(long_res,'03b')
                                            if long_res==7:
                                                res+="01111"
                                            elif long_res<4:
                                                res+=b 
                                                res+="0"
                                            else:
                                                
                                                res+=b
                                                res+="1"
                                            res1=""
                                 
                                info_hex=res

                                

                                encypthion=info_hex  
                          
                                size_data12=encypthion

                                size_data12="1"+size_data12
                            
                                lenf=len(size_data12)
                                        
                                add_bits118=""
                                count_bits=8-lenf%8
                                z=0
                                    
                                if count_bits!=8:
                                    while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                size_data12=add_bits118+size_data12
                                
                                
                                    
                                size_data11=size_data12 
                                  
                               
             
                                                                                
                                n = int(size_data11, 2)
                                
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                             
                                jl=binascii.unhexlify(qqwslenf % n)
                                
                             
                                
                                import paq
                                jl= paq.compress(jl)
                                
                                    
                                size_after=len(jl)

                                size_after=len(jl)
                                
                                   
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                            
                                assxw=assxw+1
                                if assxw==1:
                                    assx=10
                                    if assx==10:

                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)
