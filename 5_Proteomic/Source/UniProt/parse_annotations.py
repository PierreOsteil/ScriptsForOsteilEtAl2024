from lxml import etree, objectify
import pandas as pd
import sys

# xmlFile = "/home/ignatius/PostDoc/2021/ALPK1_BMP_06/Data/UniProt/data.xml"
# output_file = '/home/ignatius/PostDoc/2021/ALPK1_BMP_06/Results/UniProt/gene_ids_table_python_all.tab'

# xmlFile = "/home/ignatius/PostDoc/2022/EStim_Brain_Organoids_BMP_17/Data/UniProt/uniprot-proteome_UP000005640.xml"
# output_file = '/home/ignatius/PostDoc/2022/EStim_Brain_Organoids_BMP_17/Results/UniProt/gene_id_table_python_all.tab'

# xmlFile = "/home/ignatius/PostDoc/2022/multiphos_igypang_bmp_10_20220531/Data/UniProt/uniprot-proteome_UP000002494.xml"
# output_file = '/home/ignatius/PostDoc/2022/multiphos_igypang_bmp_10_20220531/Data/UniProt/annotations_table_python_all.tab'

xmlFile = sys.argv[1] # "/home/ignatius/PostDoc/2022/pml_apex_tony_cesare_pml_20220822/Data/UniProt/data_updated.xml"
output_file = sys.argv[2] # '/home/ignatius/PostDoc/2022/pml_apex_tony_cesare_pml_20220822/Data/UniProt/annotations_table_python_all.tab'

with open(xmlFile) as fobj:
	xml = fobj.read()

## need to remove UTF declaration string from the file first
root = etree.fromstring(xml, parser=etree.XMLParser(huge_tree=True)) 


namespace_x = {'x':"http://uniprot.org/uniprot" }

entries = root.xpath(".//x:entry", namespaces=namespace_x )


def parseOneGneId(one_gene_id):
	namespace_x = {'x':"http://uniprot.org/uniprot" }

	has_gene_id = one_gene_id.xpath(".//@id", namespaces=namespace_x)

	if len(has_gene_id ) == 0:
		return( "NA" )

	gene_id = has_gene_id[0]


	return( gene_id )



def getGeneIdFromOneUniprotEntry(one_entry):
	namespace_x = {'x':"http://uniprot.org/uniprot" }

	uniprot_acc = one_entry.xpath(".//x:accession", 
		namespaces=namespace_x )[0].text
	
	list_of_kegg_id = one_entry.xpath(".//x:dbReference[@type='GeneID']", 
		namespaces=namespace_x )
	
	if len(list_of_kegg_id) == 0: 
		return( [ uniprot_acc + ";NA"] )
		
	parsed_gene_id = list( map(parseOneGneId, list_of_kegg_id) )
	
	accession_and_gene_ids = list( map(lambda x: uniprot_acc + ";" + x, parsed_gene_id) )
	
	return( accession_and_gene_ids)

## Run all entries
all_gene_ids = list( map( getGeneIdFromOneUniprotEntry, entries))

flat_list = [item for sublist in all_gene_ids for item in sublist]

df = pd.DataFrame(flat_list, columns=['gene_id_string'])

df[['uniprot_acc',
'gene_id']] = df.gene_id_string.str.split(";",expand=True)

df.drop('gene_id_string', axis=1, inplace=True)

df.to_csv(output_file, 
	sep="\t",
	index=False)
