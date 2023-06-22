

entries[0].xpath(".//x:accession", 
		namespaces=namespace_x )[0].text


entries[0].xpath(".//x:dbReference[@type='KEGG']", 
		namespaces=namespace_x )[0].xpath(".//@id", 
	namespaces=namespace_x  )[0]
	
###################################3	
	
# "EXISTENCE"
# <proteinExistence type="evidence at protein level"/>
entries[0].xpath(".//x:proteinExistence", namespaces=namespace_x )[0].xpath(".//@type", namespaces=namespace_x)[0]
# 'evidence at transcript level'


# , "SCORE"


# , "REVIEWED"
#<entry dataset="Swiss-Prot" created="1996-10-01" modified="2022-02-23" version="196">
#<entry xmlns="http://uniprot.org/uniprot" dataset="TrEMBL" created="2011-04-05" modified="2022-08-03" version="87">
# 
# Swiss-Prot
# TrEMBL

dataset=entries[0].xpath(".//@dataset", namespaces=namespace_x )[0]

output=""
if( dataset=="Swiss-Prot"):
  output = ( "reviewed" )
else:
  output = ( "unreviewed" )

print(output)

# , "GENENAME"
genenames_list =  entries[0].xpath(".//x:gene/x:name", namespaces=namespace_x )
list ( map( lambda x: x.text,
     genenames_list)  ) 

# , "PROTEIN-NAMES"
# <protein>
# <recommendedName>
# <fullName>Tyrosine-protein kinase Blk</fullName>
# <ecNumber evidence="10">2.7.10.2</ecNumber>
# </recommendedName>
# <alternativeName>
# <fullName>B lymphocyte kinase</fullName>
# </alternativeName>
# <alternativeName>
# <fullName>p55-Blk</fullName>
# </alternativeName>
# </protein>
entries[0].xpath(".//x:protein/x:recommendedName/x:fullName", namespaces=namespace_x )[0].text

# , "LENGTH"
#<sequence length="505" mass="57706" checksum="B5F739BEF8389176" modified="2007-08-21" version="3">
entries[0].xpath(".//x:sequence//@length", namespaces=namespace_x )[0]

# , "ENSEMBL"
# <dbReference type="Ensembl" id="ENST00000259089">
# <property type="protein sequence ID" value="ENSP00000259089"/>
# <property type="gene ID" value="ENSG00000136573"/>
# </dbReference>
ensembl_list =  entries[0].xpath(".//x:dbReference[@type='Ensembl']/x:property[@type='protein sequence ID']", namespaces=namespace_x )
list ( map( lambda x: x.xpath(".//@value")[0],
     ensembl_list)  ) 

# , "GO-ID"
# <dbReference type="GO" id="GO:0031234">
go_ids_list =  entries[0].xpath(".//x:dbReference[@type='GO']", namespaces=namespace_x )
list ( map( lambda x: x.xpath(".//@id", namespaces=namespace_x)[0],
     go_ids_list)  ) 

# , "KEYWORDS"
keywrods_list =  entries[0].xpath(".//x:keyword", namespaces=namespace_x )
list ( map( lambda x: x.text,
     keywrods_list)  ) 




