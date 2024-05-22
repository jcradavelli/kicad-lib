#
# Constantes kicad7
#
import sys


cli = "kicad-cli " # path para o executavel kicad-cli
project_file_extension = ".kicad_pro"
pcb_file_extension = ".kicad_pcb"
sch_file_extension = ".kicad_sch"


#
# Funcoes kicad7
#
def get_struct_2_levels(pcb_file, srt_struct_lv_1, srt_struct_lv_2):
    interetaion_level = 0
    # string to search in file
    with open(pcb_file, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            srt_struct_lv_1
            #print(row.find(word))
            # find() method returns -1 if the value is not found,
            # if found it returns index of the first occurrence of the substring
            if row.find(srt_struct_lv_1) != -1 and interetaion_level == 0 :
                interetaion_level+=1
                # print(srt_struct_lv_1 +" exists on linenumber ", lines.index(row))
            if row.find(srt_struct_lv_2) != -1 and interetaion_level == 1 :
                interetaion_level+=1
                # print(srt_struct_lv_2 +" exists on linenumber ", lines.index(row))
                titles = row.partition("\"")
                if (len(titles) < 3):
                    sys.exit("Erro ao ler titulo do projeto no arquivo " + pcb_file) 
                return titles[2].partition("\"")[0]
        
        sys.exit("Erro no formato do arquivo " + pcb_file) 
                
def get_title(pcb_file):
    get_val = get_struct_2_levels(pcb_file,"(title_block", "  (title ")
    print ("get_val: ", get_val)
    return get_val

def get_date(pcb_file):
    get_val = get_struct_2_levels(pcb_file,"(title_block", "  (date ")
    print ("get_val: ", get_val)
    return get_val

def get_rev(pcb_file):
    get_val = get_struct_2_levels(pcb_file,"(title_block", "  (rev ") 
    print ("get_val: ", get_val)   
    return get_val

def get_company(pcb_file):
    get_val = get_struct_2_levels(pcb_file,"(title_block", "  (company ") 
    print ("get_val: ", get_val)   
    return get_val