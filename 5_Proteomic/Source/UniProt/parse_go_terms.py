from lxml import etree, objectify
import pandas as pd

#xmlFile = "/home/ignatius/PostDoc/2022/Embryology_BMP_14/Data/UniProt/data.xml"
#output_file = '/home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/go_terms_table_python_all.tab'

# xmlFile = "/home/ignatius/PostDoc/2021/ALPK1_BMP_06/Data/UniProt/data_reviewed_only.xml"
# output_file = '/home/ignatius/PostDoc/2021/ALPK1_BMP_06/Results/UniProt/go_terms_table_python_reviewed.tab'

# xmlFile = "/home/ignatius/PostDoc/2022/EStim_Brain_Organoids_BMP_17/Data/UniProt/uniprot-proteome_UP000005640.xml"
# output_file = '/home/ignatius/PostDoc/2022/EStim_Brain_Organoids_BMP_17/Results/UniProt/go_terms_table_python_all.tab'

xmlFile = "/home/ignatius/PostDoc/2022/multiphos_igypang_bmp_10_20220531/Data/UniProt/uniprot-proteome_UP000002494.xml"
output_file = '/home/ignatius/PostDoc/2022/multiphos_igypang_bmp_10_20220531/Results/UniProt/go_terms_table_python_all.tab'


with open(xmlFile) as fobj:
	xml = fobj.read()

## need to remove UTF declaration string from the file first
root = etree.fromstring(xml, parser=etree.XMLParser(huge_tree=True)) 


namespace_x = {'x':"http://uniprot.org/uniprot" }

entries = root.xpath(".//x:entry", namespaces=namespace_x )


def parseOneGoTerm(one_go_term):
	namespace_x = {'x':"http://uniprot.org/uniprot" }

	has_go_id = one_go_term.xpath(".//@id", namespaces=namespace_x)

	if len(has_go_id ) == 0:
		return( "NA" + ";" + "NA" + ";" + "NA" + 
				";" + "NA" +  ";" + "NA" )

	go_id = has_go_id[0]

	go_term_combined = one_go_term.xpath(".//x:property[@type='term']", 
	namespaces=namespace_x )[0].xpath(".//@value", 
	namespaces=namespace_x )[0]

	go_type = go_term_combined.split(":")[0]

	go_term = go_term_combined.split(":")[1]

	go_evidence = one_go_term.xpath(".//x:property[@type='evidence']", 
	namespaces=namespace_x )[0].xpath(".//@value", 
	namespaces=namespace_x )[0]

	go_project = one_go_term.xpath(".//x:property[@type='project']", 
	namespaces=namespace_x  )[0].xpath(".//@value", 
	namespaces=namespace_x  )[0]

	return( go_id + ";" + go_type + ";" + go_term + 
	";" + go_evidence +  ";" + go_project)



def getGOTermFromOneUniprotEntry(one_entry):
	namespace_x = {'x':"http://uniprot.org/uniprot" }

	uniprot_acc = one_entry.xpath(".//x:accession", 
		namespaces=namespace_x )[0].text
	
	list_of_go_terms = one_entry.xpath(".//x:dbReference[@type='GO']", 
		namespaces=namespace_x )
	
	if len(list_of_go_terms) == 0: 
		return( [ uniprot_acc + ";NA;NA;NA;NA;NA"] )
		
	parsed_go_terms = list( map(parseOneGoTerm, list_of_go_terms) )
	
	accession_and_go_terms = list( map(lambda x: uniprot_acc + ";" + x, parsed_go_terms) )
	
	return( accession_and_go_terms)





## Go through one example for parsing 
#one_go_term = list_of_go_terms[0]

#parseOneGoTerm(one_go_term)

## Go through one entry for parsing
#one_entry = entries[0]

# getGOTermFromOneUniprotEntry( one_entry)

## Run all entries


all_go_terms = list( map( getGOTermFromOneUniprotEntry, entries))

flat_list = [item for sublist in all_go_terms for item in sublist]


df = pd.DataFrame(flat_list, columns=['go_term_string'])

df[['uniprot_acc',
'go_id', 
'go_type', 
'go_term', 
'go_evidence', 
'go_project']] = df.go_term_string.str.split(";",expand=True)

df.drop('go_term_string', axis=1, inplace=True)

df.to_csv(output_file, 
	sep="\t",
	index=False)
