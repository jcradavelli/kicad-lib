# 
# Script para geracao de documentacao de placa em kicad
#
# Autor: Julio Cesar Radavelli
# Data: Maio/2024
#
# -----------------------------------------------------------------------
# 
#
# =======================================================================


import subprocess
import sys
import os
import board_file as board_file
import schematic_file as schematic_file
import port_kicad_7 as kicad


      
#=====================================================================================================
# parametro de entrada
project_dir = "C:\\kicad_7_project_template\\"


#=====================================================================================================
# Trabalha na leitura dos arquivos



print("                                   ")
print("     ..........                    ")
print("    .............                  ")
print("   ..............                  ")
print("  .......    ......                 _    _               _                              _             ")
print("  .......       ... .........      | |  (_)             | |                            | |            ")
print("   ......          ...........     | | ___  ___ __ _  __| |   _____  ___ __   ___  _ __| |_ ___ _ __  ")
print("    .....             .........    | |/ / |/ __/ _` |/ _` |  / _ \\ \\/ / '_ \\ / _ \\| '__| __/ _ \\ '__| ")
print("     ....                .......   |   <| | (_| (_| | (_| | |  __/>  <| |_) | (_) | |  | ||  __/ |    ")
print("      ..                    .....  |_|\\_\\_|\\___\\__,_|\\__,_|  \\___/_/\\_\\ .__/ \\___/|_|   \\__\\___|_|    ")
print("     ....                 ......                                      | |                             ")
print("    .....              ........                                       |_|                             ")
print("  .......           ..........      _____           ______ _                                          ")
print("  .......       ...                |  ___|          |  ___| |                                         ")
print("  .......     .....                | |__ _ __   __ _| |_  | | _____  __                               ")
print("   ...... .......                  |  __| '_ \\ / _` |  _| | |/ _ \\ \\/ /                               ")
print("    ............                   | |__| | | | (_| | |   | |  __/>  <                                ")
print("      .........                    \\____/_| |_|\\__, \\_|   |_|\\___/_/\\_\\                               ")
print("                                                __/ |                                                 ")
print("                                               |___/                                         rev 0.0  ")
print("                                   ")
print("                                   ")
print("                                   ")

                                   
                                   
                                   
                                   
                                   
                                   


#
# Get git hash
#

try:
    hash_commit = subprocess.check_output(['git','--git-dir=' + project_dir + ".git", 'describe', '--always' , '--abbrev=40', '--dirty']).decode('utf-8').strip()
    print ("directory hash: " + hash_commit)
    print ("")
except subprocess.CalledProcessError as e:
    print(f"Erro ao obter o hash do ultimo commit: {e}")
    sys.exit(f"Erro ao obter o hash do ultimo commit: \r\n\t{e}")


# procura o arquivo de projeto kicad 7
found_project_file = False
found_pcb_file = False
found_sch_file = False
for x in os.listdir(project_dir):
    if x.endswith(kicad.project_file_extension):
        print("found " + x)
        found_project_file = True
        project_name = x.partition(kicad.project_file_extension)[0]
        print("get project_name: " + project_name)
    if x.endswith(kicad.pcb_file_extension):
        print("found " + x)
        found_pcb_file = True
    if x.endswith(kicad.sch_file_extension):
        print("found " + x)
        found_sch_file = True


if found_project_file == False :
    sys.exit("project file not found")    
if found_pcb_file == False :
    sys.exit("pcb file not found")    
if found_sch_file == False :
    sys.exit("sch file not found")            






# TODO Trata o arquivo projeto
# TODO Trata o arquivo esquematico

# Trata o arquivo pcb
# TODO Pode existir mais de um arquivo
pcb_file = project_dir + project_name + kicad.pcb_file_extension
board_file.compile(project_dir, pcb_file)


sch_file = project_dir + project_name + kicad.sch_file_extension
schematic_file.compile(project_dir, sch_file)



