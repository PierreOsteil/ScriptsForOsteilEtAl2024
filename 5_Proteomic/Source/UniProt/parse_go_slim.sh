grep "^id:\|^name:\|^namespace:" /home/ignatius/PostDoc/2022/Embryology_BMP_14/Data/GOSubset/goslim_generic.obo | sed -e "s/:\s/\t/g"


grep "^id:" /home/ignatius/PostDoc/2022/Embryology_BMP_14/Data/GOSubset/goslim_generic.obo |\
 grep 'GO:' | sed -e 's/^id: //g' \
 > /home/ignatius/PostDoc/2022/Embryology_BMP_14/Results/GOSubset/go_slim_generic_go_id_list.tab








