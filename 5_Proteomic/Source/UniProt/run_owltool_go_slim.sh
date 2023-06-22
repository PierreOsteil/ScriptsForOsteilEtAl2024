


export PATH=$PATH:/home/ignatius/Programs/2022/owltools
owltools -h

owltools /home/ignatius/PostDoc/2022/Embryology_BMP_14/Data/GOSubset/go-basic.obo \
 --gaf /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/go_annotation.gaf \
 --map2slim --subset goslim_generic \
 --write-gaf /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/go_annotation.slim.gaf > \
 /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/log.txt

owltools /home/ignatius/PostDoc/2022/Embryology_BMP_14/Data/GOSubset/go-basic.obo \
 --gaf /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/go_annotation.gaf \
 --map2slim --idfile /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/GOSubset/go_slim_generic_go_id_list.tab \
 --write-gaf /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/go_annotation.slim.gaf > \
  /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/UniProt/log.txt
