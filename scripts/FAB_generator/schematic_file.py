
import port_kicad_7 as kicad 
import template_defs as template
import subprocess
import EngFlex_bom_csv_grouped_by_value_with_fp as bom_xmlTOcsv



def compile (project_dir, sch_file):
   
    # Template de diretorios
    dir_out = project_dir + "DOC\\"
    bom_dir = dir_out + "BOM\\"
    pdf_dir = dir_out + "PDF\\"

    print ("reading................................................................................." + sch_file)
    project_title = kicad.get_title(sch_file)
    project_date = kicad.get_date(sch_file)
    project_rev = kicad.get_rev(sch_file)
    project_company = kicad.get_company(sch_file)
    print (">processing")

    # Gera um diretorio de gerbers
    #
    # Documentacao do comando kicad (7.0) disponivel em: https://docs.kicad.org/7.0/en/cli/cli.html#pcb
    #
    # Resumo: kicad-cli pcb export gerbers [-h] [--output VAR] [--layers VAR] [--exclude-refdes] [--exclude-value] [--include-border-title] [--no-x2] [--no-netlist] [--subtract-soldermask] [--disable-aperture-macros] [--use-drill-file-origin] [--precision VAR] [--no-protel-ext] [--common-layers VAR] [--board-plot-params] input
    #
    print(">Starting generate BOM")
    # TODO Criar diretorio se nao existir
    # TODO backup de arquivos antigos se for sobrescrever
    bom_xml_file = bom_dir + "xml_bom_" + project_company + project_title + "_" + project_rev + "_(" + project_date + ")" + ".xml"
    bom_csv_file = bom_dir + "xml_bom_" + project_company + project_title + "_" + project_rev + "_(" + project_date + ")" + ".csv"
    cmd_generate_gerber = kicad.cli + "sch export python-bom -o " + bom_xml_file + " " + sch_file
    returned_value = subprocess.call(cmd_generate_gerber)
    bom_xmlTOcsv.run(bom_xml_file, bom_csv_file)
    print (">done")

    # Generate PDF plots
    print(">Starting generate Schematic plots in PDF")
    # TODO Criar diretorio se nao existir
    # TODO backup de arquivos antigos se for sobrescrever
    schematic_file = pdf_dir + "schematic_" + project_company + project_title + "_" + project_rev + "_(" + project_date + ")" + ".pdf"
    cmd_generate_gerber = kicad.cli + "sch export pdf -o " + schematic_file + " " + sch_file
    returned_value = subprocess.call(cmd_generate_gerber)
    print (">done")

    print ("[OK] " + sch_file)
    
