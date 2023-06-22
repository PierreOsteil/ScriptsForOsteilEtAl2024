

clean_proteins_cmd.R -c config_prot.ini -t ../../Results/TMT/cache

Rscript -e "rmarkdown::render('remove_FA2_samples.Rmd')"

de_analysis_cmd.R -c config_prot.ini

annot_proteins_cmd.R -c config_prot.ini -t ../../Results/TMT/cache

# de_analysis_cmd.R -c config_prot_remove_outliers.ini

publication_graphs.R -c config_prot.ini

# enrich_camera_proteins_v2.R -c config_prot.ini
# 
# enrich_camera_proteins_v2.R -c config_prot.ini -o ../../Results/TMT/enrich_camera_proteome_reactome \
#   --annotation_type  reactome \
#   --annotation_file  ../../Results/Reactome/reactome_data_with_header.txt \
#   --dictionary_file  ../../Results/Reactome/reactome_data_with_header.txt \
#   --protein_id  uniprot_acc \
#   --annotation_id reactome_id \
#   --annotation_column pathway_name \
#   --aspect_column NULL \
#   --annotation_type reactome_enrichment
# 
# enrich_camera_proteins_v2.R -c config_prot.ini -o ../../Results/TMT/enrich_camera_proteome_kegg \
#   --annotation_type  reactome \
#   --annotation_file  ../../Data/KEGG/gene_sets.tab \
#   --dictionary_file  ../../Data/KEGG/gene_sets.tab \
#   --protein_id  uniprot_acc \
#   --annotation_id pathway_id \
#   --annotation_column pathway_name \
#   --aspect_column NULL \
#   --annotation_type kegg_enrichment
  
proteins_pathways_enricher.R -c config_prot.ini -o ../../Results/TMT/de_proteins_go_list

proteins_pathways_enricher.R -c config_prot.ini -o ../../Results/TMT/de_proteins_reactome_list \
  --annotation_type  reactome \
  --annotation_file  ../../Results/Reactome/reactome_data_with_header.txt \
  --dictionary_file  ../../Results/Reactome/reactome_data_with_header.txt \
  --protein_id  uniprot_acc \
  --annotation_id reactome_id \
  --annotation_column pathway_name \
  --aspect_column NULL \
  --annotation_type reactome

proteins_pathways_enricher.R -c config_prot.ini -o ../../Results/TMT/de_proteins_kegg_list \
  --annotation_file  ../../Data/KEGG/gene_sets.tab \
  --dictionary_file  ../../Data/KEGG/gene_sets.tab \
  --protein_id  uniprot_acc \
  --annotation_id pathway_id \
  --annotation_column pathway_name \
  --aspect_column NULL \
  --annotation_type KEGG
  
Rscript -e "rmarkdown::render('collate_proteins_go_enrichment_v2.Rmd')"
Rscript -e "rmarkdown::render('collate_proteins_reactome_enrichment.Rmd')"
Rscript -e "rmarkdown::render('collate_proteins_kegg_enrichment.Rmd')" 


enrich_custom_proteins_list.R -c config_prot.ini -o ../../Results/TMT/clustering_enrichment_go

enrich_custom_proteins_list.R -c config_prot.ini -o ../../Results/TMT/clustering_enrichment_reactome \
  --annotation_type  reactome \
  --annotation_file  ../../Results/Reactome/reactome_data_with_header.txt \
  --dictionary_file  ../../Results/Reactome/reactome_data_with_header.txt \
  --protein_id  uniprot_acc \
  --annotation_id reactome_id \
  --annotation_column pathway_name \
  --aspect_column NULL \
  --annotation_type reactome


enrich_custom_proteins_list.R -c config_prot.ini -o ../../Results/TMT/clustering_enrichment_kegg \
  --annotation_file  ../../Data/KEGG/gene_sets.tab \
  --dictionary_file  ../../Data/KEGG/gene_sets.tab \
  --protein_id  uniprot_acc \
  --annotation_id pathway_id \
  --annotation_column pathway_name \
  --aspect_column NULL \
  --annotation_type KEGG  

  
Rscript -e "rmarkdown::render('collate_proteins_soms_go_enrichment.Rmd')"
Rscript -e "rmarkdown::render('collate_proteins_soms_kegg_enrichment.Rmd')"
Rscript -e "rmarkdown::render('collate_proteins_soms_reactome_enrichment.Rmd')" 


