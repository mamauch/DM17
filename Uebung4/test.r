library(cluster)
getwd()

datadim032 = read.table("./data/dim032.txt")
datas2 = read.table("./data/s2.txt")
dataseeds = read.table("./data/seeds_dataset.txt")


ang1dim032 <- agnes(datadim032, metric = "euclidean", method = "complete")
ang2dim032 <- agnes(datadim032, metric = "manhattan", method = "complete")
ang3dim032 <- agnes(datadim032, metric = "euclidean", method = "average")
dv1dim032 <- diana(datadim032, metric = "manhattan")
dv2dim032 <- diana(datadim032, metric = "euclidean")

png(filename="./output")
plot(ang1dim032)
dev.off()
plot(ang2dim032)
plot(ang3dim032)
plot(dv1dim032)
plot(dv2dim032)

#ang1datas2 <- agnes(datas2, metric = "euclidean", method = "complete")
#ang2datas2 <- agnes(datas2, metric = "manhattan", method = "complete")
#ang3datas2 <- agnes(datas2, metric = "euclidean", method = "average")
#dv1datas2 <- diana(datas2, metric = "manhattan")
#dv2datas2 <- diana(datas2, metric = "euclidean")

#plot(ang1datas2)
#plot(ang2datas2)
#plot(ang3datas2)
#plot(dv1datas2)
#plot(dv2datas2)

ang1dataseeds <- agnes(dataseeds, metric = "euclidean", method = "complete")
ang2dataseeds <- agnes(dataseeds, metric = "manhattan", method = "complete")
ang3dataseeds <- agnes(dataseeds, metric = "euclidean", method = "average")
dv1dataseeds <- diana(dataseeds, metric = "manhattan")
dv2dataseeds <- diana(dataseeds, metric = "euclidean")

plot(ang1dataseeds)
plot(ang2dataseeds)
plot(ang3dataseeds)
plot(dv1dataseeds)
plot(dv2dataseeds)



