import re, string
import pandas as pd
import numpy as np
from fnmatch import fnmatch
import itertools

try:
    f1 = open('G:\\Python\\dictionary1.txt', 'r', encoding = "utf-8")
    f2 = open('G:\\Python\\UniqueDescriptions1.txt', 'r', encoding = "utf-8")
    #dictWrite = open('G:\\Python\\Dictionary1.txt', 'w', encoding = "utf-8")
    #descWrite = open('G:\\Python\\Final.txt', 'w', encoding = 'utf-8')
except:
    print ('File cannot be opened:')
    exit()

KingCounts = dict()
QueenCounts = dict()
TwinCounts = dict()
DoubleCounts = dict()
SuiteCounts = dict()
JrSuiteCounts = dict()
StdCounts = dict()
SupCounts = dict()
GrCounts = dict()
DlxCounts = dict()
StudioCounts= dict()
OvwCounts = dict()
PovwCounts = dict()
WvwCounts = dict()
GvwCounts = dict()
MvwCounts= dict()
BvwCounts =dict()
smkCounts = dict()
PrkCounts = dict()
InternetCounts = dict()
brkfastCounts = dict()

def clearup(s, chars):
   return re.sub('[%s]' % chars, ' ', s).upper()

def find_word(text, search):

   result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
   if len(result)>0:
      return True
   else:
      return False
    
index = []
myList = []
s_index = []
words = []
fileLine=[]

bedString1 = "K"
bedString2 = "Q"
bedString3 = "T"
bedString4 = "D"

room1 = "S"
room2 = "J"
room3 = "C"
room4 = "G"
room5 = "H"
room6 = "B"
room7 = "E"

view1 = "O"
view2 = "W"
view4 = "M"
view5 = "P"

int1 = "IN"
int2 = "HS"

for line in f2:
    line1= line.replace("\n", "")
    words = line1.split()
    line5 = " ".join(words)
    myList.append(line5.upper())


for line0 in f1:
    line = line0.split("|")[0]  
  
    
    """KINGS:
    """

    if bedString1 in line:
        for m in re.finditer(bedString1, line):
            
            index.append(m.start())
    
      
    if len(index) > 0:
        for i in range(0, len(index)):            
            if (re.match("K", line[0:]) or re.match(" K",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
                    
                    

            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:] 
                    
                    
                        

            if(words):
                newEntry =""
                
                if (re.match(r"^[0-9]K", words[0]) and not re.match(r"^[0-9]KIT", words[0]) 
                    or re.match(r"^KII", words[0]) 
                    or re.match(r"^KB", words[0]) or re.match(r"^KG", words[0]) or re.match(r"^KIG", words[0])
                    or re.match(r"^KI$", words[0])
                    or fnmatch(words[0], "KIN") or re.match(r"^KNG*", words[0]) or re.match(r"^KS", words[0])
                    or words[0].startswith("KING")
                    or re.match("[0-9]KING", words[0]) or
                    re.match(r"^K$", words[0]) or fnmatch(words[0], "*ORKING")
                    and not fnmatch(words[0], "W*")
                    and not (fnmatch(words[0], "KINGST*") or fnmatch(words[0],"KINGSP*") or fnmatch(words[0], "KIND"))
                    and not re.match(r"SM[KO]", " ".join(words))) or fnmatch(words[len(words)-1], "K[ING][NG]*") or fnmatch(words[len(words)-1], "K"):
                         
                                  
                         newEntry = line.split("\n")[0]
                         
                    
                         if (newEntry not in KingCounts):
                            
                            KingCounts[newEntry] = 1
                            
                                               
                         else:
                            KingCounts[newEntry]+= 1
            
    del index[:]

    """Queens
    """
    
    if bedString2 in line:
        for m in re.finditer(bedString2, line):            
            index.append(m.start())
    
      
    if len(index) > 0:
        
        for i in range(0, len(index)):            
            if (re.match("Q", line[0:]) or re.match(" Q",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
                    
                    

            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:]       
                    
                     

            if(words):
               
                newEntry =""
                
            
                
                if (re.match(r"^[0-9]Q", words[0]) or fnmatch(words[0], "*[0-9]Q*") and not fnmatch(words[0], "*[0-9][0-9]Q*")
                    and not fnmatch(words[0], "*[0-9]QM*") or fnmatch(words[0], "QN*") or fnmatch(words[0], "QUEENS*")
                    or fnmatch(words[0], "Q[WU][UNE]*") and not fnmatch(words[0], "QUEN*") and not fnmatch(words[0], "QUEST*")
                    or re.match(r"[0-9] Q$", line)):
                         
                                  
                         newEntry = line.split("\n")[0]
                         
                    
                         if (newEntry not in QueenCounts):
                            
                            QueenCounts[newEntry] = 1
                            
                                               
                         else:
                            QueenCounts[newEntry]+= 1
            
    del index[:]
    
    """Twins
    """


    if bedString3 in line:
        for m in re.finditer(bedString3, line):            
            index.append(m.start())
    
      
    if len(index) > 0:
        
        for i in range(0, len(index)):            
            if (re.match("T", line[0:]) or re.match(" T",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
                    
                    

            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:]       
                    
            
                       
                    
                    
                        

            if(words):
               
                newEntry =""
                
            
                
                if (fnmatch(words[0], "*[0-9]T[W]*") or re.match(r"[0-9]T$", words[0]) or fnmatch(words[0], "TWI*") and not
                    fnmatch(words[0], "TWIT*") and not fnmatch(words[0], "TWIC*") and not fnmatch(words[0], "TWIS*") and not
                    fnmatch(words[0], "TWINT[O]*") and not fnmatch(words[0], "TWIL*") or fnmatch(words[0], "TWN*") and not fnmatch(words[0],"TWNH*")
                    or fnmatch(words[0], "TIWN*") or words[0].startswith("TWWI") or re.match(r"[0-9] T$", line)):
                         
                                  
                         newEntry = line.split("\n")[0]
                         
                    
                         if (newEntry not in TwinCounts):
                            
                            TwinCounts[newEntry] = 1
                            
                                               
                         else:
                            TwinCounts[newEntry]+= 1
    del index[:]
    
  
    """
    Double
    """

    if bedString4 in line:
        for m in re.finditer(bedString4, line):            
            index.append(m.start())
    
      
    if len(index) > 0:
        
        for i in range(0, len(index)):            
            if (re.match("D", line[0:]) or re.match(" D",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
                    
                    

            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:]       
                    
            
                       
                    
                    
                        

            if(words):
               
                newEntry =""
                
            
                
                if (fnmatch(words[0], "*[0-9]D*") and not fnmatch(words[0], "*DR*") and not fnmatch(words[0], "*DL*")
                    and not fnmatch(words[0], "*[0-9]DOL*") and not fnmatch(words[0], "*[0-9]DA*")
                    and not  fnmatch(words[0], "*[0-9]DE*") and not fnmatch(words[0], "*DIN*") and not fnmatch(words[0], "*[0-9][0-9]D*")
                    and not fnmatch(words[0], "*4DVD*")
                    and not fnmatch(words[0], "*3DX*") and not fnmatch(words[0], "*MP3*") and not fnmatch(words[0], "*LCD3*")
                    and not fnmatch(words[0], "*4DIA*") or fnmatch(words[0], "DB") or re.match(r"DO$", words[0]) or re.match(r"[0-9] D$", line)
                    or fnmatch(words[0], "*DBL*") or re.match(r"[0-9]D$", words[0]) or fnmatch(words[0], "[D]DBL*")
                    or fnmatch(words[0], "DLB[SE]*") or fnmatch(words[0], "DOUBL*") or re.match(r"DOU$", words[0])):
                         
                                  
                         newEntry = line.split("\n")[0]
                         
                    
                         if (newEntry not in DoubleCounts and not fnmatch(newEntry, "DBL CLUB") and not fnmatch(newEntry,"DBL PTS")):
                            
                            DoubleCounts[newEntry] = 1
                            
                                               
                         elif (newEntry in DoubleCounts):
                            DoubleCounts[newEntry]+= 1

            if (re.match("^DELUXE$", words[0]) or fnmatch(words[0], "*DEL[\sU]*") and not fnmatch(words[0], "*DELS*") or fnmatch(words[0], "DLE*")
                    or re.match("DX", words[0]) or fnmatch(words[0], "DL[UX]*")
                    or fnmatch(words[0], "*DEU[X]*")):

                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in DlxCounts):
                            
                           DlxCounts[newEntry] = 1
                            
                                               
                        else:
                           DlxCounts[newEntry]+= 1

    del index[:]
    

    
    """
    Standard, Suite, Superior, Studio, Smoking, Breakfast, Beachfront, Junior Suite
    """

    if room1 in line:
        for m in re.finditer(room1, line):
            index.append(m.start())
    if room2 in line:
        for m in re.finditer(room2, line):
            index.append(m.start())
    if room3 in line:
        for m in re.finditer(room3, line):
            index.append(m.start())
    if room5 in line:
        for m in re.finditer(room5, line):
            index.append(m.start())
    if room6 in line:
        for m in re.finditer(room6, line):
            index.append(m.start())
    if room7 in line:
        for m in re.finditer(room7, line):
            index.append(m.start())
    
      
    if len(index) > 0:
        
        for i in range(0, len(index)):            
            if (re.match("S", line[0:]) or re.match(" S",line[index[i]-1:]) or re.match("C", line[0:]) or re.match(" C",line[index[i]-1:])
                or re.match("H", line[0:]) or re.match(" H",line[index[i]-1:]) or re.match("B", line[0:]) or re.match(" B",line[index[i]-1:]) or
                re.match("E", line[0:]) or re.match(" E",line[index[i]-1:]) or re.match("J", line[0:]) or re.match(" J",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
                    
                    

            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:]       
                    
            
            if(words):
               
                newEntry =""
                
                if (fnmatch(words[0], "*J[NR]*") and not fnmatch(words[0], "JRSLM")
                and not fnmatch(words[0], "JNRP*") or fnmatch(words[0], "*JURI*") or fnmatch(words[0], "*JUN[IO]*")):
                         newEntry = line.split("\n")[0]
                         if (newEntry not in JrSuiteCounts):
                            
                             JrSuiteCounts[newEntry] = 1
                         else:
                             JrSuiteCounts[newEntry]+= 1  
                
                if (fnmatch(words[0], "*SUI*") and not fnmatch(words[0], "ENSUITE") and not fnmatch(words[0], "SUI[ST][SCA]*")
                    and not fnmatch(words[0], "J[NUR][RN]*")
                    and not fnmatch(words[0], "JS*") and not fnmatch(words[0], "PURSUI*") and not fnmatch(words[0], "NONSU*")
                    or fnmatch(words[0], "STE") or re.match(r"H[OM][ME][\sE]$", words[0])
                    or fnmatch(words[0], "*NHM*") or fnmatch(words[0], "BUNG*") or fnmatch(words[0], "BG*")
                    or re.match(r"STE$", words[0]) and not fnmatch(words[0], "TERSTE") and not fnmatch(words[0], "KURFUR*")
                    or fnmatch(words[0], "EXEC*") or fnmatch(words[0], "EXE*") and not fnmatch(words[0], "EXE[MTPLR]*")
                    and not fnmatch(words[0],"EXECUJET") and not fnmatch(line, "EXEC*CLUB") or fnmatch(words[0], "*CABIN[\sSV]*")):
                          newEntry = line.split("\n")[0]
                         
                    
                          if (newEntry not in SuiteCounts and newEntry not in JrSuiteCounts and line.find("TO HOME")==-1 and line.find("EN SUITE")==-1):
                            
                            SuiteCounts[newEntry] = 1
                          elif newEntry in SuiteCounts:
                            SuiteCounts[newEntry]+= 1


            if (fnmatch(words[0], "*STAND*") and not fnmatch(words[0], "STANDU*") and not fnmatch(words[0], "UNDER*")
                    and not fnmatch(words[0], "*[UEHS][THE]STAND*") or fnmatch(words[0], "ST[NQD]*")):

                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in StdCounts):
                            
                           StdCounts[newEntry] = 1
                            
                                               
                        else:
                           StdCounts[newEntry]+= 1


            if (fnmatch(words[0], "STUI*") or fnmatch(words[0], "STUD*") and re.match("STU", words[0]) and not fnmatch(words[0], "STUD[LEYB]*")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in StudioCounts):
                            
                           StudioCounts[newEntry] = 1
                            
                                               
                        else:
                           StudioCounts[newEntry]+= 1
                         
                         
            if (fnmatch(words[0], "SUP*") and not fnmatch(words[0], "SUP[DEL][IYER][SFBMPTE]*") and not fnmatch(words[0], "SUPERDO*")
                    and not fnmatch(words[0], "SUPERINT**") and not fnmatch(words[0], "SUP[PL]*") and not fnmatch(words[0], "SUPR*")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in SupCounts and line.find("SUPER SAVER")==-1):
                            
                           SupCounts[newEntry] = 1
                            
                                               
                        elif newEntry in SupCounts:
                           SupCounts[newEntry]+= 1

            if (fnmatch(words[0], "*BEACH*V*") or fnmatch(words[0], "*BEACH*F*") or fnmatch(words[0], "*BEACH")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in BvwCounts):
                            
                           BvwCounts[newEntry] = 1
                            
                                               
                        else:
                           BvwCounts[newEntry]+= 1

            if (fnmatch(words[0], "*SMK*") and not re.match("^MOSMK", words[0]) and not fnmatch(words[0], "SMKH*") and not fnmatch(words[0], "*N*") and not
                    fnmatch(words[0], "*NOSMK")
                    or fnmatch(words[0], "*SM[OK]*") and not fnmatch(words[0], "*NONSM[KO]*") and not fnmatch(words[0], "*N*")
                    and not fnmatch(words[0], "SMOKY*") or fnmatch(words[0], "*SMOKING*")
                    and not fnmatch(line, "*NONSMOKING*")):

                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in smkCounts and not fnmatch(line,"*NONSMO*") and not fnmatch(line, "*NSK*") and not fnmatch(line, "*NON SMOKING*") and (line.find("NOSMK")==-1)):
                            
                           smkCounts[newEntry] = 1
                            
                                               
                        elif newEntry in smkCounts:
                           smkCounts[newEntry]+= 1

            if (fnmatch(words[0], "*BREAKF**") or fnmatch(words[0], "*BRK*") or re.match("CONTIN$", words[0]) or fnmatch(words[0], "*CONTIN[NTEB]*")
                    and not fnmatch(line, "INTER*CONTINE*") or fnmatch(words[0], "*BF*")
                    or fnmatch(words[0], "*BKF[SA]*") or fnmatch(words[0], "*BBK*") or fnmatch(line, "*BREAK BUFF*") or
                    fnmatch(words[0], "BRFST*")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in brkfastCounts and line.find("INTERCONTINENTAL")==-1):
                            
                           brkfastCounts[newEntry] = 1
                            
                                               
                        elif newEntry in brkfastCounts:
                           brkfastCounts[newEntry]+= 1
                        
        
    del index[:]
    
    if room4 in line:
        for m in re.finditer(room4, line):
            index.append(m.start())
    if view5 in line:
        for m in re.finditer(view5, line):
            index.append(m.start())
    if view2 in line:
        for m in re.finditer(view2, line):
            index.append(m.start())
    if int1 in line:
        for m in re.finditer(int1, line):
            index.append(m.start())
    if int2 in line:
        for m in re.finditer(int2, line):
            index.append(m.start())
    if view1 in line:
        for m in re.finditer(view1, line):
            index.append(m.start())
    
      
    if len(index) > 0:
        
        for i in range(0, len(index)):            
            if (re.match("G", line[0:]) or re.match(" G",line[index[i]-1:]) or re.match("P", line[0:]) or re.match(" P",line[index[i]-1:])
                or re.match("O", line[0:]) or re.match(" O",line[index[i]-1:]) or re.match("W", line[0:]) or re.match(" W",line[index[i]-1:]) or
                re.match("IN", line[0:]) or re.match(" IN",line[index[i]-1:]) or re.match("HS", line[0:]) or re.match(" HS",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
                    
                    

            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:]       
                    
            
            if(words):
               
                newEntry =""
                
                

                if (fnmatch(words[0], "*GRAND[ESVL][LITU]*") and not fnmatch(words[0], "*GRAND[EL][UI][RT]*") or fnmatch(words[0], "GRND*")):
                         newEntry = line.split("\n")[0]
                         if (newEntry not in GrCounts):
                            
                             GrCounts[newEntry] = 1
                         else:
                             GrCounts[newEntry]+= 1                         
                
                if (fnmatch(words[0], "*G[AR][RD][DN]*V[IW]*") or fnmatch(words[0], "GARDEN") or fnmatch(words[0], "PARKV*") or
                    fnmatch(words[0], "*P[AR][RK]V[IW]*") or fnmatch(words[0], "PVIEW*")):
                         newEntry = line.split("\n")[0]
                         
                         if (newEntry not in GvwCounts):
                             GvwCounts[newEntry] = 1
                         else:
                             GvwCounts[newEntry]+= 1


                if (fnmatch(words[0], "*W[AT]*[V][IW]") and not fnmatch(words[0], "M*") or fnmatch(words[0], "WATER") or fnmatch(words[0], "*WV*")
                    and not fnmatch(words[0], "*M*WV") and not fnmatch(words[0], "WM*") or fnmatch(words[0], "*WTRF*") or fnmatch(words[0], "WATERF[R]*")
                    or fnmatch(words[0], "*POOLV*") or fnmatch(line, "POOL V*") or fnmatch(words[0], "*BAYV*") or fnmatch(line, "RIVER*[SVF]*") or
                fnmatch(line, "VIEW OF WATER")):

                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in WvwCounts and not fnmatch(newEntry, "*M*WV") and not fnmatch(newEntry, "WM*")):
                            
                           WvwCounts[newEntry] = 1
                            
                                               
                        elif (newEntry in WvwCounts):
                           WvwCounts[newEntry]+= 1
                           
                if (re.match("FREE W$", line) or fnmatch(words[0], "WIFI") or fnmatch(words[0], "*WI[IFR][EIF]*") and not fnmatch(words[0], "H*WIRE*") or fnmatch(words[0], "*WLAN*")
                    or fnmatch(words[0], "*INT[RE][ER]N[ET]*") and not fnmatch(words[0], "WINTER*") or fnmatch(words[0], "*INTL*") or fnmatch(words[0], "*INT[RN]*")
                    and not fnmatch (words[0], "*INTR[AO]*")
                    or fnmatch(words[0], "*INT[RE][EN][NE]*") and not fnmatch(words[0], "WINTER*") or re.match("HSIA", words[0])
                    or fnmatch(words[0],"HISP*") or fnmatch(words[0], "*NET*") and not fnmatch(words[0], "*[WN]INE*") or re.match(r"WI+ FI", line)
                    or re.match(r"WI$", words[0]) or re.match(r"FREE W$", line) or re.match(r"INTER$", words[0]) or fnmatch(line, "HIGH SPEE*")
                    or fnmatch(line, "FREE HI*") or fnmatch(line, "FREE HIG") or fnmatch(line, "IN ROOM HBO")
                    or fnmatch(line, "*MB IN ROOM") or fnmatch(line, "MBS IN ROOM")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in InternetCounts and newEntry.find("WINTER")==-1):
                            
                           InternetCounts[newEntry] = 1
                            
                                               
                        elif (newEntry in InternetCounts):
                           InternetCounts[newEntry]+= 1
                         
                         
                if (fnmatch(words[0], "*PRKI*") or re.match(r"PARKI$", words[0]) or fnmatch(words[0], "*PARKI[NG]*")
                    and not fnmatch(words[0], "*S[LP][PRA][KR]K*") and not 
                    fnmatch(words[0], "*PARKV*") and not fnmatch(words[0], "*VA*") or fnmatch(words[0], "*PRK*") and not fnmatch(words[0], "*RPRK*")
                    and not fnmatch(words[0], "*PRKV*") and not fnmatch(words[0], "*RMPRK*") or fnmatch(words[0], "*PKNG*")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in PrkCounts and not find_word(line, "CHARGE FOR HOTEL PARKING")):
                            
                           PrkCounts[newEntry] = 1
                            
                                               
                        elif newEntry in PrkCounts:
                           PrkCounts[newEntry]+= 1

                if (fnmatch(words[0], "*OC*[SV][IW]*") and not fnmatch(words[0], "PROC*") and not fnmatch(words[0], "*ROCK*")
                    and not fnmatch(words[0], "PARTI*") and not fnmatch(words[0], "[NMFLO][OEIC][CVOT]*")
                    and not fnmatch(words[0], "OVER[VW]*") or fnmatch(words[0], "*CEAN*") and not fnmatch(words[0], "*OCEANO*")
                    and not fnmatch(words[0], "NONOC*")
                    or fnmatch(words[0], "*O[CV]*W*") and not re.match("^ROCK",words[0])
                    and not fnmatch(words[0], "*P[OR][OT]*[CV]*W*") and not fnmatch(words[0], "[NMFLO][OEIC][CVO]*") or fnmatch(line, "SEA*V*")):
                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in OvwCounts):
                            
                           OvwCounts[newEntry] = 1
                            
                                               
                        else:
                           OvwCounts[newEntry]+= 1

            if (fnmatch(words[0], "*P*OC*[SV][IW]*") and not fnmatch(words[0], "PROC*") and not fnmatch(words[0], "*ROCK*")
                    and not fnmatch(words[0], "PARTI*") and not fnmatch(words[0], "[NMFLO][OEIC][CVOT]*")
                    and not fnmatch(words[0], "OVER[VW]*") or fnmatch(words[0], "*P*CEAN*") and not fnmatch(words[0], "*OCEANO*")
                    and not fnmatch(words[0], "NONOC*") or fnmatch(words[0], "PARTIAL") 
                    or fnmatch(words[0], "*P*O[CV]*W*") and not re.match("^ROCK",words[0])
                    and not fnmatch(words[0], "[NMFLO][OEIC][CVO]*")):

                        newEntry = line.split("\n")[0]
                         
                    
                        if (newEntry not in PovwCounts):
                            
                           PovwCounts[newEntry] = 1
                            
                                               
                        else:
                           PovwCounts[newEntry]+= 1
                        
        
    del index[:]

    if view4 in line:
        for m in re.finditer(view4, line):
            index.append(m.start())
    
      
    if len(index) > 0:
        for i in range(0, len(index)):            
            if (re.match("M", line[0:]) or re.match(" M",line[index[i]-1:])):
                    words = line[index[i]:].split()
                    
            else:
                    
                    
                    for m in re.finditer(r'\s', line):
                        if m.start()< index[i]:
                            s_index.append(m.start())
                      
                    if (not s_index):
                        s_index.append(0)
                    
                    
                                            
                    index[i] = s_index[len(s_index)-1]                            
                    words = line[index[i]:].split()
                    del s_index[:]
                
           
        if (words):
                
            if (re.match("^MOUNTAIN$", words[0]) or fnmatch(words[0], "*MOU*[SV][IW]*") and not fnmatch(words[0], "LIMOU*") or fnmatch(words[0], "MOUNT*")
                    or fnmatch(words[0], "*MT*V*") and not fnmatch(words[0], "*[OSCEQ]MTV*") or fnmatch(words[0], "*MT*SI*")):
                     newEntry = line.split("\n")[0]
                     if (newEntry not in MvwCounts):
                            
                             MvwCounts[newEntry] = 1
                     else:
                             MvwCounts[newEntry]+= 1

            
    del index[:]

lstk = list(KingCounts.keys())

   
lstq = list(QueenCounts.keys())

lstt = list(TwinCounts.keys())


lstd1 = list(DoubleCounts.keys())

lsts1 = list(SuiteCounts.keys())

lsts2 = list(StdCounts.keys())

lsts3 = list(StudioCounts.keys())

lsts4 = list(SupCounts.keys())

lstj = list(JrSuiteCounts.keys())

lstg1 = list(GrCounts.keys())

lstd2 = list(DlxCounts.keys())

lsto = list(OvwCounts.keys())

lstp1 = list(PovwCounts.keys())

lstb = list(BvwCounts.keys())

lstm = list(MvwCounts.keys())

lstg2 = list(GvwCounts.keys())

lstw = list(WvwCounts.keys())

lsti = list(InternetCounts.keys())

lstp2 = list(PrkCounts.keys())

lsts5 = list(smkCounts.keys())

lstb2 = list(brkfastCounts.keys())



df = pd.DataFrame()
for a, b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u in itertools.zip_longest(lstk, lstq,lstd1, lstt, lsts1, lstj, lstg1, lsts4, lsts2, lstd2, lsts3, lsto, lstw, lstb, lstp1, lstm, lstg2, lsts5, lsti, lstp2, lstb2):
    df = pd.concat([df, pd.DataFrame({'lstk': [a] or [np.nan], 'lstq': [b] or [np.nan], 'lstd1': [c] or [np.nan], 'lstt': [d] or [np.nan], 
                                      'lsts1': [e] or [np.nan], 'lstj': [f] or [np.nan], 'lstg1': [g] or [np.nan], 'lsts4': [h] or [np.nan], 'lsts2': [i] or [np.nan], 'lstd2': [j] or [np.nan], 'lsts3': [k] or [np.nan], 
                                      'lsto': [l] or [np.nan], 'lstw': [m] or [np.nan], 'lstb': [n] or [np.nan], 'lstp1': [o] or [np.nan], 'lstm': [p] or [np.nan], 'lstg2': [q] or [np.nan],
                                      'lsts5': [r] or [np.nan], 'lsti': [s] or [np.nan], 'lstp2': [t] or [np.nan], 'lstb2': [u] or [np.nan]})])
    

df.to_csv("G:\\Final.csv", sep=',', encoding='utf-8')

f1.close()
f2.close()
#dictWrite.close()
