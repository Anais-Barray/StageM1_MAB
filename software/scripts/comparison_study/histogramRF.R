
# Open the files containing the RF distance vectors
vectorpplacer<-read.table("/home/anaisb/resultats/RF/vectpplacerM3R1.txt")
vectorEPA<-read.table("/home/anaisb/resultats/RF/vectEPAM3R1.txt")
vectorSEPP<-read.table("/home/anaisb/resultats/RF/vectSEPPM3R1.txt")

# Make histograms for the 3 tools' RF distances + visualisation
hist( as.numeric ( unlist ( vectorSEPP )  ) , col=rgb(0.7,0.1,0.5,0.5),  xlim=c(0, 60), ylim=c(0,5000), xlab="RF distance", ylab="number of trees compared", main="RF distances of M3R1 dataset (medium divergence)" )
hist( as.numeric ( unlist ( vectorEPA )  ) , col=rgb(0,1,0.5,0.5), add=T)
hist( as.numeric ( unlist ( vectorpplacer )  ) ,  col=rgb(0.2,0.5,0.85,0.6), add=T)

box()

legend("topright", c("SEPP" ,"pplacer", "EPA" ), fill=c(rgb(0.7,0.1,0.5,0.5), rgb(0.2,0.5,0.85,0.6), rgb(0,1,0.5,0.5)))
