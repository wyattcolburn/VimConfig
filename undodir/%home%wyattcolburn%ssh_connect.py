Vim�UnDo� ć2o�>F])�&��i��ǅ�K�٫�y�̯   .   T    parser.add_argument('drone_ID', type=str, help='Enter ID: owl5, Drone2, Drone3')   ,         #       #   #   #    fy��    _�                            ����                                                                                                                                                                                                                                                                                                                                                             fy��     �          D       # Project: SAR with SWARM DRONES5��                                              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             fy��     �          D       # Project: SAR with SWARM DRONES5��                                                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             fy�     �          D      # Project: SAR5��                                                �                                              �                                              �                                              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             fy�"     �          D       # Project: OWL Summer, research 5��               
                 
              �                                                5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�1     �         D      N# Description: This program allows ssh into drone1 rp when connected to CP IOT5��       ,                  ~                      5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�4     �         D      O# Description: This program allows ssh into Vdrone1 rp when connected to CP IOT5��       ,                  ~                      5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�5     �         D      G# Description: This program allows ssh into rp when connected to CP IOT5��       ,                  ~                      5�_�      	                 ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�5     �         D      D# Description: This program allows ssh into when connected to CP IOT5��       ,                  ~                      5�_�      
           	      ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�5     �         D      ?# Description: This program allows ssh into connected to CP IOT5��       ,       
           ~       
               5�_�   	              
      ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�5     �         D      5# Description: This program allows ssh into to CP IOT5��       ,                  ~                      5�_�   
                    ,    ����                                                                                                                                                                                                                                                                                                                                                             fy�6     �                2# Description: This program allows ssh into CP IOT5��                          R       3               5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             fy�7     �         C      K# only portioned need to change for different rp are ip, username, password5��       .                  �                      5�_�                      -    ����                                                                                                                                                                                                                                                                                                                                                             fy�?     �         C      -# Author: Wyatt Colburn, wdcolbur@calpoly.edu5��       -                  Q                      �                       	   R               	       �                     E   X              E       �       4                  �                      �       4                  �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             fy�S     �         E      4# Description: Program allows users to remotely ssh     �         E       5��                          �                      �                          �                      �       4                  �                      5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             fy�X     �         C           �      	   D           �      
   D       5��                          +                     �                          *                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             fy�_     �         B      $def ssh_into_raspberry_pi(drone_ID):5��                         j                     �              	       	   f      	       	       5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             fy�c     �         B      )def ssh_into_raspberry_pi(raspberrye_ID):5��       #                  o                     5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             fy�l     �         B      (def ssh_into_raspberry_pi(raspberry_ID):5��              
           f      
               5�_�                            ����                                                                                                                                                                                                                                                                                                                                      "          V       fy�t     �                    if drone_ID == "Drone1":   (        raspberry_pi_ip = "10.40.126.73"           username = "sar"           password = "drone1"       elif drone_ID == "Drone2":   (        raspberry_pi_ip = "10.40.126.55"           username = "ander"           password = "drone2"       elif drone_ID == "Drone3":           username = "ander"   )        raspberry_pi_ip = "10.40.127.129"           password = "drone3"       elif drone_ID == "Summer":   !        username = "wyattcolburn"   )        raspberry_pi_ip = "10.40.107.138"            password = "A$APFerg007"       elif drone_ID == "pi3":            username = "raspberrypi"           password = "password"   )        raspberry_pi_ip = "192.168.1.214"5��                          �      �              5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                V       fy�x     �         .          elif drone_ID == "owl":5��                         �                     �                         �                     �                         �                     �                         �                     �                        �                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       fy�{     �         .          if drone_ID == "owl":5��                         �                     5�_�                    +   @    ����                                                                                                                                                                                                                                                                                                                                                V       fyʏ     �   *   ,   .      O    parser = argparse.ArgumentParser(description='SSH into Drone Raspberry Pi')5��    *   :                  )                     5�_�                    ,   @    ����                                                                                                                                                                                                                                                                                                                                                V       fyʓ     �   +   -   .      \    parser.add_argument('drone_ID', type=str, help='Enter Drone ID: Drone1, Drone2, Drone3')5��    +   :                  s                     5�_�                    ,   D    ����                                                                                                                                                                                                                                                                                                                                                V       fyʗ     �   +   -   .      V    parser.add_argument('drone_ID', type=str, help='Enter ID: Drone1, Drone2, Drone3')5��    +   >                 w                    5�_�                    ,   A    ����                                                                                                                                                                                                                                                                                                                                                V       fyʛ     �   +   -   .      S    parser.add_argument('drone_ID', type=str, help='Enter ID: owl, Drone2, Drone3')5��    +   A                  z                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       fyʥ     �         .          if ID == "owl":5��                         �                     5�_�                    .   %    ����                                                                                                                                                                                                                                                                                                                                                V       fyʲ     �   -              (    ssh_into_raspberry_pi(args.drone_ID)5��    -                     �                     5�_�                    ,       ����                                                                                                                                                                                                                                                                                                                                                V       fyʶ     �   +   -   .      T    parser.add_argument('drone_ID', type=str, help='Enter ID: owl5, Drone2, Drone3')5��    +                     S                     5�_�                     ,   =    ����                                                                                                                                                                                                                                                                                                                                                V       fyʽ     �   +   -   .      N    parser.add_argument('ID', type=str, help='Enter ID: owl5, Drone2, Drone3')5��    +   =                  w                     5�_�      !               ,   =    ����                                                                                                                                                                                                                                                                                                                                                V       fyʽ     �   +   -   .      M    parser.add_argument('ID', type=str, help='Enter ID: owl5,Drone2, Drone3')5��    +   =                  w                     5�_�       "           !   ,   =    ����                                                                                                                                                                                                                                                                                                                                                V       fyʾ     �   +   -   .      G    parser.add_argument('ID', type=str, help='Enter ID: owl5,, Drone3')5��    +   =                  w                     5�_�   !   #           "   ,   =    ����                                                                                                                                                                                                                                                                                                                                                V       fyʾ     �   +   -   .      E    parser.add_argument('ID', type=str, help='Enter ID: owl5,Drone3')5��    +   =                  w                     5�_�   "               #   ,   =    ����                                                                                                                                                                                                                                                                                                                                                V       fy��    �   +   -   .      ?    parser.add_argument('ID', type=str, help='Enter ID: owl5,')5��    +   <                  v                     5�_�                      .    ����                                                                                                                                                                                                                                                                                                                                                             fy�7     �         C      D# only portioned need to change for different ip, username, password5��       .                  �                      5�_�                        .    ����                                                                                                                                                                                                                                                                                                                                                             fy�8     �         C      B# only portioned need to change for different , username, password5��       .                  �                      5��