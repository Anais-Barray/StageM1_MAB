library(ape)


# Open the tree files
arbreplaced<-file("/home/anaisb/resultats/restrictedtrees/M2R0-pplacer_output_restrictedTrees_placed_checked", open="r")
arbretrue<-file("/home/anaisb/resultats/restrictedtrees/M2R0-pplacer_output_restrictedTrees_true", open="r")

# Distance vector which will contain the RF distance between the two tree files
distvectorM2R0pplacer<-NULL

# Parses trees, one at a time, of each file, and realises the RF distance (dist.topo) between them
for(i in 1:5000){

  arbreplacedline<-readLines(arbreplaced,n=1)
  treeplaced<-read.tree(text=arbreplacedline)
  arbretrueline<-readLines(arbretrue,n=1)
  treetrue<-read.tree(text=arbretrueline)
  distvectorM2R0pplacer<-append(distvectorM2R0pplacer,dist.topo(treetrue,treeplaced))
  
}

close(arbreplaced)
close(arbretrue)

write.table(distvectorM2R0pplacer, file="/home/anaisb/resultats/RF/vectpplacerM2R0.txt", quote=FALSE, row.name=FALSE, col.name=FALSE)

