Vim�UnDo� �h-��t\<�S��D���Rl������~��lr                                     fB��    _�                     =   S    ����                                                                                                                                                                                                                                                                                                                            h           t           V        f?�     �   <   ?        S        data_message = ser.readline().decode('utf-8').strip() # this is the message5��    <   S                 R              	       �    =                     [                     5�_�                    >       ����                                                                                                                                                                                                                                                                                                                            i           u           V        f?�E     �   =   ?                if data_message 5��    =                     k                     5�_�                    >       ����                                                                                                                                                                                                                                                                                                                            i           u           V        f?�F     �   =   ?                if data_message == 5��    =                     n                     5�_�                    >       ����                                                                                                                                                                                                                                                                                                                            i           u           V        f?�G     �   =   ?                if data_message == ""5��    =                     o                     �    =                      s                     5�_�                    >        ����                                                                                                                                                                                                                                                                                                                            i           u           V        f?�b     �   =   ?        !        if data_message == "AT+C"5��    =                      s                     �    =   %                 x                    5�_�                    >   '    ����                                                                                                                                                                                                                                                                                                                            i           u           V        f?�f     �   =   @        '        if data_message == "AT+CRFOP=5"5��    =   '                  z                     �    =   (                 {              	       �    >                     |                    �    >                      |                     5�_�                    @       ����                                                                                                                                                                                                                                                                                                                            j           v           V        f?�k     �   ?   A        %        if samples < DATA_ARRAY_SIZE:5��    ?                 
   �             
       �    ?                     �                     5�_�      	              B       ����                                                                                                                                                                                                                                                                                                                            j           v           V        f?�x     �   A   C        ;            data_message_filtered = data_message.split(',')5��    A                                          5�_�      
           	   D       ����                                                                                                                                                                                                                                                                                                                            j           v           V        f?�z     �   C   E        B            time_stamp = datetime.now().strftime("%m/%d/%H:%M:%S")5��    C                     U                     5�_�   	              
   D       ����                                                                                                                                                                                                                                                                                                                            j           v           V        f?�|     �   C   E        C            Vtime_stamp = datetime.now().strftime("%m/%d/%H:%M:%S")5��    C                     T                     5�_�   
                 D       ����                                                                                                                                                                                                                                                                                                                            j           v           V        f?�}     �   C   E        B           Vtime_stamp = datetime.now().strftime("%m/%d/%H:%M:%S")5��    C                     T                     5�_�                    D       ����                                                                                                                                                                                                                                                                                                                            j           v           V        f?�     �   C   E        A           time_stamp = datetime.now().strftime("%m/%d/%H:%M:%S")5��    C                     T                     5�_�                    D        ����                                                                                                                                                                                                                                                                                                                            D          J          V       f?��     �   C   K        B            time_stamp = datetime.now().strftime("%m/%d/%H:%M:%S")   T            data_array[time_stamp] = int(data_message_filtered[-2]) #was a str-->int               samples += 1   B            print(f"Num of samples {samples} > {DATA_ARRAY_SIZE}")           else:               print(data_array)               return data_array5��    C                     I                    �    D                     �                    �    E                     �                    �    F                                         �    G                     M                    �    H                     _                    �    I                     �                    5�_�                    H        ����                                                                                                                                                                                                                                                                                                                            H          J          V       f?��     �   G   K                    else:   !                print(data_array)   !                return data_array5��    G                     M                    �    H                     [                    �    I                     y                    5�_�                    H       ����                                                                                                                                                                                                                                                                                                                            5           J           V        f?��     �   G   I                else:5��    G                     U                     5�_�                    I       ����                                                                                                                                                                                                                                                                                                                            5           J           V        f?��     �   H   J                    print(data_array)5��    H                     k                     5�_�                    J       ����                                                                                                                                                                                                                                                                                                                            5           J           V        f?��    �   I   K                    return data_array5��    I                     �                     5�_�                     7       ����                                                                                                                                                                                                                                                                                                                                                             fB��    �   6   9            5��    6                     [                     �    6                    [                    �    6                 :   ]             :       �    6   ?                �                    �    7                     �                     �    7   
                  �                     5��