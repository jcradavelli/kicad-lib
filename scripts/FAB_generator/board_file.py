
import port_kicad_7 as kicad 
import template_defs as template
import subprocess



def compile (project_dir, pcb_file):
   
    # Template de diretorios
    dir_out = project_dir + "DOC\\"
    gerber_dir = dir_out + "GERBER\\"
    step3d_dir = dir_out + "STEP3D\\"

    print ("reading................................................................................." + pcb_file)
    project_title = kicad.get_title(pcb_file)
    project_date = kicad.get_date(pcb_file)
    project_rev = kicad.get_rev(pcb_file)
    project_company = kicad.get_company(pcb_file)
    print (">processing")

    # Gera um diretorio de gerbers
    #
    # Documentacao do comando kicad (7.0) disponivel em: https://docs.kicad.org/7.0/en/cli/cli.html#pcb
    #
    # Resumo: kicad-cli pcb export gerbers [-h] [--output VAR] [--layers VAR] [--exclude-refdes] [--exclude-value] [--include-border-title] [--no-x2] [--no-netlist] [--subtract-soldermask] [--disable-aperture-macros] [--use-drill-file-origin] [--precision VAR] [--no-protel-ext] [--common-layers VAR] [--board-plot-params] input
    #
    print(">Starting generate gerber files")
    # TODO Criar diretorio se nao existir
    # TODO backup de arquivos antigos se for sobrescrever
    cmd_generate_gerber = kicad.cli + "pcb export gerbers -o " + gerber_dir + " --layers " + template.gerber_layers_files + " --ibt " + "--no-protel-ext " + "--cl " + template.gerber_layers_common + " " + pcb_file
    returned_value = subprocess.call(cmd_generate_gerber)
    print (">done")



    # TODO Gerar arquivos de furacao "pcb export drill"
    # TODO Gerar arquivos de posicao "pcb export pos"
    
    # Gerar 3D da placa
    print(">Starting generate step files")
    
    file_name = step3d_dir + "filled" + project_company + project_title + "_" + project_rev + "_(" + project_date + ")" + ".step"
    cmd_generate_gerber = kicad.cli + "pcb export step --grid-origin --subst-models -f -o " + file_name + " " + pcb_file
    returned_value = subprocess.call(cmd_generate_gerber)

    file_name = step3d_dir + "outline" + project_company + project_title + "_" + project_rev + "_(" + project_date + ")" + ".step"
    cmd_generate_gerber = kicad.cli + "pcb export step --grid-origin --board-only -f -o " + file_name + " " + pcb_file
    returned_value = subprocess.call(cmd_generate_gerber)

    print (">done")

    print ("[OK] " + pcb_file)
    
